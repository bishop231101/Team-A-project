"""PowerShell-friendly CLI for the official Week 11 baseline workflow."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.week11_production import (  # noqa: E402
    build_manifest,
    analyze_trial,
    load_and_validate_corpus,
    prepare_inputs,
)

CORPUS = ROOT / "tests" / "fixtures" / "week9_corpus.json"


def _is_record_invalid(result: dict) -> bool:
    if result["valid"]:
        return False
    if result.get("analysis_status") != "incomplete":
        return True
    operational_incomplete = (
        "trial status must be completed or failed after manual transfer",
        "retrieved file is empty; no platform result has been supplied",
    )
    return any(
        not (error in operational_incomplete or error.startswith("missing raw file:"))
        for error in result.get("validation_errors", [])
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare or analyze Week 11 official trials.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    manifest_parser = subparsers.add_parser("manifest", help="write the approved 168-slot plan")
    manifest_parser.add_argument("--output", type=Path, required=True)

    prepare_parser = subparsers.add_parser("prepare", help="populate existing production_testing folders")
    prepare_parser.add_argument("--root", type=Path, required=True)

    trial_parser = subparsers.add_parser("analyze-trial", help="analyze one completed trial")
    trial_parser.add_argument("--root", type=Path, required=True)
    trial_parser.add_argument("--record", type=Path, required=True)

    batch_parser = subparsers.add_parser("analyze-batch", help="analyze every record in a manifest")
    batch_parser.add_argument("--root", type=Path, required=True)
    batch_parser.add_argument("--manifest", type=Path, required=True)

    args = parser.parse_args()
    if args.command == "manifest":
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(build_manifest(), indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"planned_trial_count": 168, "output": str(args.output)}, indent=2))
    elif args.command == "prepare":
        result = prepare_inputs(args.root, CORPUS)
        print(json.dumps({"prepared_trial_count": len(result["trials"]), "output": str(args.root)}, indent=2))
    elif args.command == "analyze-trial":
        record = json.loads(args.record.read_text(encoding="utf-8"))
        manifest_path = args.root.parent / "production_manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        expected = next(item for item in manifest["trials"] if item["trial_id"] == record.get("trial_id"))
        result = analyze_trial(record, load_and_validate_corpus(CORPUS), args.root, expected)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        raise SystemExit(0 if result["valid"] else 1)
    else:
        manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
        corpus = load_and_validate_corpus(CORPUS)
        results = []
        for manifest_record in manifest.get("trials", []):
            record = manifest_record
            record_path = args.root / manifest_record["record_path"]
            if record_path.is_file():
                record = json.loads(record_path.read_text(encoding="utf-8"))
            results.append(analyze_trial(record, corpus, args.root, manifest_record))
        summary = {
            "planned_records": len(results),
            "valid_records": sum(item["valid"] for item in results),
            "invalid_records": sum(_is_record_invalid(item) for item in results),
            "complete_records": sum(item.get("analysis_status") == "completed" for item in results),
            "incomplete_records": sum(item.get("analysis_status") == "incomplete" for item in results),
            "exact_recoveries": sum(item.get("measured", {}).get("exact_match", False) for item in results),
        }
        output = args.root / "analysis" / "batch_analysis.json"
        output.parent.mkdir(exist_ok=True)
        output.write_text(json.dumps({"summary": summary, "results": results}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"summary": summary, "output": str(output)}, ensure_ascii=False, indent=2))
        raise SystemExit(0 if summary["invalid_records"] == 0 else 1)


if __name__ == "__main__":
    main()
