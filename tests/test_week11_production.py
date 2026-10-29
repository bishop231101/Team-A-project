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
    def _expected(self, record: dict, root: Path | None = None) -> dict:
        manifest = build_manifest()
        if root is not None and (root.parent / "production_manifest.json").is_file():
            manifest = json.loads((root.parent / "production_manifest.json").read_text(encoding="utf-8"))
        return next(item for item in manifest["trials"] if item["trial_id"] == record["trial_id"])

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
            incomplete = analyze_trial(record, corpus, root, self._expected(record, root))
            self.assertEqual(incomplete["analysis_status"], "incomplete")
            with (root / record["retrieved_path"]).open("w", encoding="utf-8", newline="") as handle:
                handle.write("retrieved but not yet marked complete")
            still_incomplete = analyze_trial(record, corpus, root, self._expected(record, root))
            self.assertEqual(still_incomplete["analysis_status"], "incomplete")
            record["status"] = "failed"
            retrieved = root / record["retrieved_path"]
            with retrieved.open("w", encoding="utf-8", newline="") as handle:
                handle.write("Team 1 compatibility test.\r\n")
            result = analyze_trial(record, corpus, root, self._expected(record, root))
            self.assertEqual(result["analysis_status"], "completed")
            self.assertFalse(result["measured"]["decoder_returned"])
            saved = json.loads((root / record["record_path"]).read_text(encoding="utf-8"))
            self.assertEqual(saved["analysis_status"], "completed")

    def test_completed_trial_with_captured_empty_retrieval_is_analyzed(self):
        corpus = load_and_validate_corpus(CORPUS)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "production_testing"
            self._empty_production_root(root)
            prepare_inputs(root, CORPUS)
            record_path = root / "Gmail/W11_Gmail-SA01_R1/W11_Gmail-SA01_R1.json"
            record = json.loads(record_path.read_text(encoding="utf-8"))
            record["status"] = "completed"
            record["tester"] = "Tristan Koch"
            record["timestamp_utc"] = "2026-10-28T15:00:00Z"
            evidence = root / "Gmail/W11_Gmail-SA01_R1/evidence/gmail-empty.png"
            evidence.write_bytes(b"captured evidence")
            record["evidence_paths"] = ["Gmail/W11_Gmail-SA01_R1/evidence/gmail-empty.png"]
            record_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            result = analyze_trial(record, corpus, root, self._expected(record, root))
            self.assertTrue(result["valid"])
            self.assertEqual(result["analysis_status"], "completed")
            self.assertEqual(result["measured"]["retrieved_counts"]["total"], 0)
            self.assertEqual(result["measured"]["retention_percentage"], 0.0)
            self.assertFalse(result["measured"]["decoder_returned"])
            self.assertIsNotNone(result["measured"]["decoder_error"])

    def test_completed_metadata_is_required_and_valid_metadata_is_accepted(self):
        corpus = load_and_validate_corpus(CORPUS)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "production_testing"
            self._empty_production_root(root)
            prepare_inputs(root, CORPUS)
            record_path = root / "Gmail/W11_Gmail-SA01_R1/W11_Gmail-SA01_R1.json"
            record = json.loads(record_path.read_text(encoding="utf-8"))
            record["status"] = "completed"
            for field in ("tester", "timestamp_utc", "evidence_paths"):
                candidate = dict(record)
                candidate[field] = None if field != "evidence_paths" else []
                result = analyze_trial(candidate, corpus, root, self._expected(record, root), write_result=False)
                self.assertTrue(any(field in error or "evidence" in error for error in result["validation_errors"]))
            invalid_timestamp = dict(record, tester="Tristan Koch", timestamp_utc="2026-10-28T15:00:00-04:00", evidence_paths=[])
            result = analyze_trial(invalid_timestamp, corpus, root, self._expected(record, root), write_result=False)
            self.assertTrue(any("UTC timestamp" in error for error in result["validation_errors"]))
            valid = dict(record, tester="Tristan Koch", timestamp_utc="2026-10-28T15:00:00Z", evidence_paths=["Gmail/W11_Gmail-SA01_R1/evidence/valid.png"])
            (root / valid["evidence_paths"][0]).write_bytes(b"evidence")
            result = analyze_trial(valid, corpus, root, self._expected(record, root), write_result=False)
            self.assertTrue(result["valid"])

    def test_completed_evidence_references_cannot_escape_production_root(self):
        corpus = load_and_validate_corpus(CORPUS)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "production_testing"
            self._empty_production_root(root)
            prepare_inputs(root, CORPUS)
            record_path = root / "Gmail/W11_Gmail-SA01_R1/W11_Gmail-SA01_R1.json"
            record = json.loads(record_path.read_text(encoding="utf-8"))
            record.update({"status": "completed", "tester": "Tristan Koch", "timestamp_utc": "2026-10-28T15:00:00Z"})
            outside = Path(directory) / "outside-evidence.png"
            outside.write_bytes(b"evidence")
            for evidence_path in (str(outside), "../outside-evidence.png"):
                candidate = dict(record, evidence_paths=[evidence_path])
                result = analyze_trial(candidate, corpus, root, self._expected(record, root), write_result=False)
                self.assertFalse(result["valid"])
                self.assertTrue(any("escapes production root" in error for error in result["validation_errors"]))

    def test_manifest_tampering_is_rejected(self):
        corpus = load_and_validate_corpus(CORPUS)
        fields = ("trial_id", "platform", "operation", "corpus_id", "repetition", "sent_path", "retrieved_path", "input_sha256", "protocol_version", "codec_commit", "cover_text", "recovery_mode", "repetition_policy")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "production_testing"
            self._empty_production_root(root)
            prepare_inputs(root, CORPUS)
            record_path = root / "Gmail/W11_Gmail-SA01_R1/W11_Gmail-SA01_R1.json"
            record = json.loads(record_path.read_text(encoding="utf-8"))
            expected = self._expected(record, root)
            for field in fields:
                tampered = dict(record)
                tampered[field] = "tampered" if field not in {"repetition", "recovery_mode"} else (99 if field == "repetition" else True)
                result = analyze_trial(tampered, corpus, root, expected, write_result=False)
                self.assertFalse(result["valid"], field)
                self.assertTrue(any(field in error for error in result["validation_errors"]), field)

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
                if status in {"completed", "failed"}:
                    record["tester"] = "Tristan Koch"
                    record["timestamp_utc"] = "2026-10-28T15:00:00Z"
                    evidence = root / item["platform_directory"] / item["trial_id"] / "evidence" / "batch.png"
                    evidence.write_bytes(b"batch evidence")
                    record["evidence_paths"] = [str(evidence.relative_to(root)).replace("\\", "/")]
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
            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            summary = json.loads((root / "analysis/batch_analysis.json").read_text(encoding="utf-8"))["summary"]
            self.assertEqual(summary["planned_records"], 168)
            self.assertEqual(summary["complete_records"], 2)
            self.assertEqual(summary["incomplete_records"], 166)
            self.assertEqual(summary["invalid_records"], 0)
            self.assertEqual(summary["exact_recoveries"], 1)

    def test_failed_trial_requires_terminal_metadata_and_accepts_valid_metadata(self):
        corpus = load_and_validate_corpus(CORPUS)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "production_testing"
            self._empty_production_root(root)
            prepare_inputs(root, CORPUS)
            record_path = root / "Gmail/W11_Gmail-SA01_R1/W11_Gmail-SA01_R1.json"
            record = json.loads(record_path.read_text(encoding="utf-8"))
            record["status"] = "failed"
            retrieved = root / record["retrieved_path"]
            retrieved.write_text("Team 1 compatibility test.", encoding="utf-8")
            expected = self._expected(record, root)

            cases = (
                ("missing tester", dict(tester=None, timestamp_utc="2026-10-28T15:00:00Z", evidence_paths=["Gmail/W11_Gmail-SA01_R1/evidence/valid.png"])),
                ("invalid timestamp", dict(tester="Tristan Koch", timestamp_utc="not-utc", evidence_paths=["Gmail/W11_Gmail-SA01_R1/evidence/valid.png"])),
                ("missing evidence references", dict(tester="Tristan Koch", timestamp_utc="2026-10-28T15:00:00Z", evidence_paths=[])),
                ("missing evidence file", dict(tester="Tristan Koch", timestamp_utc="2026-10-28T15:00:00Z", evidence_paths=["Gmail/W11_Gmail-SA01_R1/evidence/missing.png"])),
            )
            for label, updates in cases:
                candidate = dict(record, **updates)
                result = analyze_trial(candidate, corpus, root, expected, write_result=False)
                self.assertFalse(result["valid"], label)
            empty_evidence = root / "Gmail/W11_Gmail-SA01_R1/evidence/empty.png"
            empty_evidence.write_bytes(b"")
            empty_candidate = dict(record, tester="Tristan Koch", timestamp_utc="2026-10-28T15:00:00Z", evidence_paths=["Gmail/W11_Gmail-SA01_R1/evidence/empty.png"])
            self.assertFalse(analyze_trial(empty_candidate, corpus, root, expected, write_result=False)["valid"])
            valid_evidence = root / "Gmail/W11_Gmail-SA01_R1/evidence/valid.png"
            valid_evidence.write_bytes(b"failed trial evidence")
            valid_candidate = dict(record, tester="Tristan Koch", timestamp_utc="2026-10-28T15:00:00Z", evidence_paths=["Gmail/W11_Gmail-SA01_R1/evidence/valid.png"])
            result = analyze_trial(valid_candidate, corpus, root, expected, write_result=False)
            self.assertTrue(result["valid"])
            self.assertEqual(result["analysis_status"], "completed")

    def test_failed_trial_with_missing_timestamp_is_rejected(self):
        corpus = load_and_validate_corpus(CORPUS)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "production_testing"
            self._empty_production_root(root)
            prepare_inputs(root, CORPUS)
            record_path = root / "Gmail/W11_Gmail-SA01_R1/W11_Gmail-SA01_R1.json"
            record = json.loads(record_path.read_text(encoding="utf-8"))
            record["status"] = "failed"
            retrieved = root / record["retrieved_path"]
            retrieved.write_text("Team 1 compatibility test.", encoding="utf-8")
            evidence = root / "Gmail/W11_Gmail-SA01_R1/evidence/valid.png"
            evidence.write_bytes(b"failed trial evidence")
            candidate = dict(
                record,
                tester="Tristan Koch",
                timestamp_utc=None,
                evidence_paths=["Gmail/W11_Gmail-SA01_R1/evidence/valid.png"],
            )
            result = analyze_trial(candidate, corpus, root, self._expected(record, root), write_result=False)
            self.assertFalse(result["valid"])
            self.assertTrue(any("UTC timestamp" in error for error in result["validation_errors"]))

    def test_batch_analysis_reports_manifest_mismatch_as_invalid(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "production_testing"
            self._empty_production_root(root)
            prepare_inputs(root, CORPUS)
            manifest_path = Path(directory) / "production_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            target = manifest["trials"][0]
            record_path = root / target["record_path"]
            record = json.loads(record_path.read_text(encoding="utf-8"))
            record["platform"] = "Discord"
            record_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, "tests/week11_testing/production_workflow.py", "analyze-batch", "--root", str(root), "--manifest", str(manifest_path)],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(completed.returncode, 1, completed.stderr + completed.stdout)
            summary = json.loads((root / "analysis/batch_analysis.json").read_text(encoding="utf-8"))["summary"]
            self.assertEqual(summary["invalid_records"], 1)
            self.assertEqual(summary["incomplete_records"], 168)


if __name__ == "__main__":
    unittest.main()
