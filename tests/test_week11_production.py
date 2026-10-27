import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src.week11_production import (
    COVER_TEXT,
    APPROVED_WORKFLOWS,
    build_manifest,
    load_and_validate_corpus,
    prepare_inputs,
    analyze_trial,
)
ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "tests" / "fixtures" / "week9_corpus.json"


class Week11ProductionWorkflowTests(unittest.TestCase):
    def test_manifest_has_exact_168_slots_and_existing_platform_paths(self):
        manifest = build_manifest()
        self.assertEqual(manifest["planned_trial_count"], 168)
        self.assertEqual(len(manifest["trials"]), 168)
        self.assertTrue(all(item["status"] == "planned" for item in manifest["trials"]))
        self.assertTrue(all(item["repetition_policy"] == "reuse_encoded_input" for item in manifest["trials"]))
        self.assertTrue(manifest["preliminary_data_excluded"])
        self.assertEqual({item["platform_directory"] for item in manifest["trials"]}, {item[1] for item in APPROVED_WORKFLOWS})

    def _empty_production_root(self, root: Path, preserve_evidence: bool = False) -> dict[str, bytes]:
        markers: dict[str, bytes] = {}
        for _, platform_dir, _ in APPROVED_WORKFLOWS:
            evidence = root / platform_dir / "evidence"
            evidence.mkdir(parents=True)
            if preserve_evidence:
                marker = f"existing-{platform_dir}.png"
                markers[platform_dir] = f"preserve {platform_dir}".encode("utf-8")
                (evidence / marker).write_bytes(markers[platform_dir])
        return markers

    def test_prepare_encodes_once_per_corpus_and_creates_all_required_trial_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "production_testing"
            markers = self._empty_production_root(root, preserve_evidence=True)
            with patch("src.week11_production.embed_secret", wraps=__import__("src.zero_width_codec", fromlist=["embed_secret"]).embed_secret) as encoder:
                result = prepare_inputs(root, CORPUS)
            self.assertEqual(len(result["trials"]), 168)
            self.assertEqual(encoder.call_count, 8)
            self.assertEqual({item["platform_directory"] for item in result["trials"]}, {item[1] for item in APPROVED_WORKFLOWS})
            self.assertEqual({item["corpus_id"] for item in result["trials"]}, set(("SA01", "SA02", "SU01", "SU02", "LA01", "LA02", "LU01", "LU02")))
            for corpus_id in ("SA01", "SA02", "SU01", "SU02", "LA01", "LA02", "LU01", "LU02"):
                corpus_trials = [item for item in result["trials"] if item["corpus_id"] == corpus_id]
                self.assertEqual(len(corpus_trials), 21)
                self.assertEqual(len({(root / item["sent_path"]).read_bytes() for item in corpus_trials}), 1)
                self.assertEqual(len({item["input_sha256"] for item in corpus_trials}), 1)
            for item in result["trials"]:
                trial_root = root / Path(item["record_path"]).parent
                self.assertTrue(trial_root.is_dir())
                self.assertTrue((root / item["sent_path"]).is_file())
                self.assertTrue((root / item["retrieved_path"]).is_file())
                self.assertEqual((root / item["retrieved_path"]).read_bytes(), b"")
                self.assertTrue((root / item["record_path"]).is_file())
                self.assertTrue((trial_root / "evidence").is_dir())
            for platform_dir, marker_bytes in markers.items():
                marker = root / platform_dir / "evidence" / f"existing-{platform_dir}.png"
                self.assertEqual(marker.read_bytes(), marker_bytes)

    def test_existing_trial_folder_stops_without_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "production_testing"
            self._empty_production_root(root)
            existing = root / "Gmail" / "W11_Gmail-SA01_R1"
            existing.mkdir()
            marker = existing / "marker.txt"
            marker.write_text("preserve", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                prepare_inputs(root, CORPUS)
            self.assertEqual(marker.read_text(encoding="utf-8"), "preserve")

    def test_existing_canonical_input_stops_without_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "production_testing"
            self._empty_production_root(root)
            canonical = root / "canonical_inputs"
            canonical.mkdir()
            marker = canonical / "SA01_encoded.txt"
            marker.write_text("preserve", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                prepare_inputs(root, CORPUS)
            self.assertEqual(marker.read_text(encoding="utf-8"), "preserve")

    def test_empty_retrieval_is_incomplete_and_completed_failure_is_analyzed(self):
        corpus = load_and_validate_corpus(CORPUS)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "production_testing"
            self._empty_production_root(root)
            prepare_inputs(root, CORPUS)
            record = json.loads((root / "Gmail/W11_Gmail-SA01_R1/W11_Gmail-SA01_R1.json").read_text(encoding="utf-8"))
            incomplete = analyze_trial(record, corpus, root)
            self.assertEqual(incomplete["analysis_status"], "incomplete")
            with (root / record["retrieved_path"]).open("w", encoding="utf-8", newline="") as handle:
                handle.write("retrieved but not yet marked complete")
            still_incomplete = analyze_trial(record, corpus, root)
            self.assertEqual(still_incomplete["analysis_status"], "incomplete")
            record["status"] = "failed"
            retrieved = root / record["retrieved_path"]
            with retrieved.open("w", encoding="utf-8", newline="") as handle:
                handle.write("Team 1 compatibility test.\r\n")
            result = analyze_trial(record, corpus, root)
            self.assertEqual(result["analysis_status"], "completed")
            self.assertFalse(result["measured"]["decoder_returned"])
            saved = json.loads((root / record["record_path"]).read_text(encoding="utf-8"))
            self.assertEqual(saved["analysis_status"], "completed")

    def test_batch_analysis_distinguishes_incomplete_success_and_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "production_testing"
            self._empty_production_root(root)
            prepare_inputs(root, CORPUS)
            manifest_path = Path(directory) / "production_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            success = next(item for item in manifest["trials"] if item["trial_id"] == "W11_Gmail-SA01_R1")
            failure = next(item for item in manifest["trials"] if item["trial_id"] == "W11_Gmail-SA01_R2")
            for item, retrieved_text, status in (
                (success, (root / success["sent_path"]).read_text(encoding="utf-8"), "completed"),
                (failure, "Team 1 compatibility test.", "failed"),
            ):
                record_path = root / item["record_path"]
                record = json.loads(record_path.read_text(encoding="utf-8"))
                record["status"] = status
                with (root / item["retrieved_path"]).open("w", encoding="utf-8", newline="") as handle:
                    handle.write(retrieved_text)
                record_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, "tests/week11_testing/production_workflow.py", "analyze-batch", "--root", str(root), "--manifest", str(manifest_path)],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            summary = json.loads((root / "analysis/batch_analysis.json").read_text(encoding="utf-8"))["summary"]
            self.assertEqual(summary["planned_records"], 168)
            self.assertEqual(summary["complete_records"], 2)
            self.assertEqual(summary["incomplete_records"], 166)
            self.assertEqual(summary["invalid_records"], 0)
            self.assertEqual(summary["exact_recoveries"], 1)


if __name__ == "__main__":
    unittest.main()
