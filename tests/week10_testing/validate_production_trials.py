"""Validate Week 10 production logs against their raw UTF-8 text files."""

import argparse
import json
from pathlib import Path
import sys


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from src.production_trial_validation import analyze_trial_record, duplicate_errors


CORPUS_PATH = REPOSITORY_ROOT / "tests" / "fixtures" / "week9_corpus.json"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Recalculate Week 10 trial metrics and verify recorded claims."
    )
    parser.add_argument("batch", type=Path, help="JSON array of production records")
    arguments = parser.parse_args()

    batch_path = arguments.batch.resolve()
    records = json.loads(batch_path.read_text(encoding="utf-8"))
    if not isinstance(records, list):
        raise SystemExit("batch file must contain a JSON array")
    corpus = {
        item["id"]: item
        for item in json.loads(CORPUS_PATH.read_text(encoding="utf-8"))
    }
    duplicate_findings = duplicate_errors(records)
    results = []

    for index, record in enumerate(records):
        corpus_id = record.get("corpus_id")
        if corpus_id not in corpus:
            results.append(
                {
                    "trial_id": record.get("trial_id"),
                    "valid": False,
                    "validation_errors": [f"unknown corpus_id: {corpus_id!r}"],
                }
            )
            continue

        try:
            sent_text = (batch_path.parent / record["sent_path"]).read_text(
                encoding="utf-8"
            )
            retrieved_text = (batch_path.parent / record["retrieved_path"]).read_text(
                encoding="utf-8"
            )
        except (KeyError, OSError) as error:
            results.append(
                {
                    "trial_id": record.get("trial_id"),
                    "valid": False,
                    "validation_errors": [f"raw text file error: {error}"],
                }
            )
            continue

        result = analyze_trial_record(
            record,
            sent_text,
            retrieved_text,
            corpus[corpus_id]["text"],
            evidence_root=batch_path.parent,
        )
        result["validation_errors"].extend(duplicate_findings.get(index, []))
        result["valid"] = not result["validation_errors"]
        results.append(result)

    summary = {
        "records": len(results),
        "valid_records": sum(result["valid"] for result in results),
        "invalid_records": sum(not result["valid"] for result in results),
        "exact_recoveries": sum(
            bool(result.get("measured", {}).get("exact_match")) for result in results
        ),
    }
    print(json.dumps({"summary": summary, "results": results}, indent=2))
    if summary["invalid_records"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
