"""Validate Week 10 production-trial metadata and measured codec results."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from .failure_analysis import analyze_recovered_text


APPROVED_WORKFLOWS = {
    "Gmail": "send_and_retrieve",
    "Discord": "send_and_retrieve",
    "Microsoft Word": "save_reopen_and_retrieve",
    "Microsoft Outlook": "send_and_retrieve",
    "Telegram Web": "send_and_retrieve",
    "Notepad++": "paste_and_copy_back",
    "Browser Console": "paste_and_copy_back",
}

REQUIRED_FIELDS = (
    "trial_id",
    "platform",
    "operation",
    "corpus_id",
    "repetition",
    "tester",
    "timestamp_utc",
    "codec_commit",
    "recovery_mode",
    "sent_path",
    "retrieved_path",
    "evidence_paths",
    "claimed_metrics",
)


def _valid_utc_timestamp(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed.tzinfo is not None and parsed.utcoffset() is not None


def validate_trial_metadata(record: dict[str, Any]) -> list[str]:
    """Return reproducibility and protocol errors in one trial record."""
    errors = [f"missing required field: {field}" for field in REQUIRED_FIELDS if field not in record]
    if errors:
        return errors

    platform = record["platform"]
    operation = record["operation"]
    if platform not in APPROVED_WORKFLOWS:
        errors.append(f"platform is outside approved matrix: {platform!r}")
    elif operation != APPROVED_WORKFLOWS[platform]:
        errors.append(
            f"operation {operation!r} does not match approved workflow for {platform}"
        )

    repetition = record["repetition"]
    if not isinstance(repetition, int) or isinstance(repetition, bool) or not 1 <= repetition <= 3:
        errors.append("repetition must be an integer from 1 through 3")
    if not _valid_utc_timestamp(record["timestamp_utc"]):
        errors.append("timestamp_utc must be an ISO-8601 timestamp with a timezone")
    if not isinstance(record["recovery_mode"], bool):
        errors.append("recovery_mode must be a boolean")
    if not isinstance(record["evidence_paths"], list) or not record["evidence_paths"]:
        errors.append("evidence_paths must be a nonempty list")
    if not isinstance(record["claimed_metrics"], dict):
        errors.append("claimed_metrics must be an object")
    return errors


def analyze_trial_record(
    record: dict[str, Any],
    sent_text: str,
    retrieved_text: str,
    expected_secret: str,
) -> dict[str, Any]:
    """Measure a trial and compare its recorded claims with reproducible results."""
    errors = validate_trial_metadata(record)
    measured = analyze_recovered_text(sent_text, retrieved_text, expected_secret)
    claims = record.get("claimed_metrics")

    if isinstance(claims, dict):
        comparisons = {
            "sent_counts": measured["sent_counts"],
            "retrieved_counts": measured["retrieved_counts"],
            "decoder_returned": measured["decoder_returned"],
            "exact_match": measured["exact_match"],
            "failure_category": measured["failure_category"],
        }
        for name, actual in comparisons.items():
            if name not in claims:
                errors.append(f"claimed_metrics is missing {name}")
            elif claims[name] != actual:
                errors.append(
                    f"claimed {name} does not match measurement: "
                    f"claimed={claims[name]!r}, measured={actual!r}"
                )

        if "retention_percentage" not in claims:
            errors.append("claimed_metrics is missing retention_percentage")
        else:
            claimed_retention = claims["retention_percentage"]
            actual_retention = measured["retention_percentage"]
            if actual_retention is None:
                if claimed_retention is not None:
                    errors.append("claimed retention must be null when sent total is zero")
            elif not isinstance(claimed_retention, (int, float)) or isinstance(
                claimed_retention, bool
            ):
                errors.append("claimed retention_percentage must be numeric")
            elif abs(float(claimed_retention) - actual_retention) > 0.01:
                errors.append(
                    "claimed retention_percentage does not match measurement: "
                    f"claimed={claimed_retention!r}, measured={actual_retention!r}"
                )

    return {
        "trial_id": record.get("trial_id"),
        "corpus_id": record.get("corpus_id"),
        "platform": record.get("platform"),
        "operation": record.get("operation"),
        "repetition": record.get("repetition"),
        "valid": not errors,
        "validation_errors": errors,
        "measured": measured,
    }


def duplicate_errors(records: list[dict[str, Any]]) -> dict[int, list[str]]:
    """Locate duplicate trial IDs and duplicate matrix/corpus repetitions."""
    errors: dict[int, list[str]] = {}
    seen_ids: dict[object, int] = {}
    seen_slots: dict[tuple[object, ...], int] = {}

    for index, record in enumerate(records):
        trial_id = record.get("trial_id")
        if trial_id in seen_ids:
            errors.setdefault(index, []).append(f"duplicate trial_id: {trial_id!r}")
            errors.setdefault(seen_ids[trial_id], []).append(
                f"duplicate trial_id: {trial_id!r}"
            )
        else:
            seen_ids[trial_id] = index

        slot = (
            record.get("platform"),
            record.get("operation"),
            record.get("corpus_id"),
            record.get("repetition"),
        )
        if slot in seen_slots:
            errors.setdefault(index, []).append(f"duplicate production slot: {slot!r}")
            errors.setdefault(seen_slots[slot], []).append(
                f"duplicate production slot: {slot!r}"
            )
        else:
            seen_slots[slot] = index
    return errors
