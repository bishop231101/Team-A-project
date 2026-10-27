"""Guarded preparation and analysis helpers for Week 11 baseline trials.

This module deliberately does not perform platform operations.  It creates
deterministic local inputs only after an explicit repetition policy is given,
and it treats missing raw retrievals as incomplete rather than successful.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .failure_analysis import analyze_recovered_text
from .zero_width_codec import count_codec_characters, embed_secret, extract_secret


COVER_TEXT = "Team 1 compatibility test."
RECOVERY_MODE = False
PROTOCOL_VERSION = "1.0-week11-baseline"
CODEC_COMMIT = "4134cec1d23be3ae7069440a3718e09069922bdc"
REPETITIONS = (1, 2, 3)
APPROVED_REPETITION_POLICY = "reuse_encoded_input"

APPROVED_WORKFLOWS = (
    ("Gmail", "Gmail", "send_and_retrieve"),
    ("Discord", "Discord", "send_and_retrieve"),
    ("Microsoft Word", "Microsoft_Word", "save_reopen_and_retrieve"),
    ("Microsoft Outlook", "Microsoft_Outlook", "send_and_retrieve"),
    ("Telegram Web", "Telegram_Web", "send_and_retrieve"),
    ("Notepad++", "Notepad++", "paste_and_copy_back"),
    ("Browser Console", "Google_Chrome_Browser_Console", "paste_and_copy_back"),
)

APPROVED_CORPUS_IDS = ("SA01", "SA02", "SU01", "SU02", "LA01", "LA02", "LU01", "LU02")
def read_exact_utf8(path: Path) -> str:
    """Read UTF-8 without translating line endings or trimming content."""
    with path.open("r", encoding="utf-8", newline="") as handle:
        return handle.read()


def write_exact_utf8(path: Path, text: str) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def load_and_validate_corpus(path: Path) -> dict[str, dict[str, Any]]:
    """Load the frozen corpus and validate IDs, fields, and recorded hashes."""
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise ValueError("corpus must be a JSON array")
    by_id: dict[str, dict[str, Any]] = {}
    for item in raw:
        if not isinstance(item, dict):
            raise ValueError("each corpus entry must be an object")
        missing = {"id", "category", "text", "sha256"} - item.keys()
        if missing:
            raise ValueError(f"corpus entry is missing fields: {sorted(missing)}")
        identifier = item["id"]
        if identifier in by_id:
            raise ValueError(f"duplicate corpus id: {identifier!r}")
        if hashlib.sha256(item["text"].encode("utf-8")).hexdigest() != item["sha256"]:
            raise ValueError(f"corpus sha256 mismatch for {identifier}")
        by_id[identifier] = item
    if tuple(by_id) != APPROVED_CORPUS_IDS or set(by_id) != set(APPROVED_CORPUS_IDS):
        raise ValueError(
            "corpus IDs do not exactly match the approved eight-message corpus: "
            f"{sorted(by_id)}"
        )
    return by_id


def trial_id(platform_dir: str, corpus_id: str, repetition: int) -> str:
    display_slug = {
        "Gmail": "Gmail",
        "Discord": "Discord",
        "Microsoft_Word": "Word",
        "Microsoft_Outlook": "Outlook",
        "Telegram_Web": "Telegram_Web",
        "Notepad++": "Notepad++",
        "Google_Chrome_Browser_Console": "Chrome_Browser_Console",
    }[platform_dir]
    return f"W11_{display_slug}-{corpus_id}_R{repetition}"


def _trial_record(platform: str, platform_dir: str, operation: str, corpus_id: str, repetition: int) -> dict[str, Any]:
    identifier = trial_id(platform_dir, corpus_id, repetition)
    relative_trial = f"{platform_dir}/{identifier}"
    return {
        "trial_id": identifier, "status": "planned", "platform": platform,
        "platform_directory": platform_dir, "operation": operation, "corpus_id": corpus_id,
        "repetition": repetition, "repetition_policy": APPROVED_REPETITION_POLICY,
        "tester": None, "timestamp_utc": None, "codec_commit": CODEC_COMMIT,
        "protocol_version": PROTOCOL_VERSION, "cover_text": COVER_TEXT,
        "recovery_mode": RECOVERY_MODE, "repetition_factor": None,
        "sent_path": f"{relative_trial}/{identifier}_sent.txt",
        "retrieved_path": f"{relative_trial}/{identifier}_retrieved.txt",
        "record_path": f"{relative_trial}/{identifier}.json",
        "evidence_paths": [f"{relative_trial}/evidence"], "input_sha256": None,
        "local_validation": None, "measured_results": None, "notes": [],
    }


def build_manifest() -> dict[str, Any]:
    """Build the approved 168-slot plan without fabricating outcomes."""
    trials = []
    for platform, platform_dir, operation in APPROVED_WORKFLOWS:
        for corpus_id in APPROVED_CORPUS_IDS:
            for repetition in REPETITIONS:
                trials.append(_trial_record(platform, platform_dir, operation, corpus_id, repetition))
    return {
        "dataset": "week11_official_baseline_production",
        "production_root": "tests/week11_testing/production_testing",
        "preliminary_data_excluded": True,
        "protocol_version": PROTOCOL_VERSION,
        "repetition_policy": APPROVED_REPETITION_POLICY,
        "encoding_rule": "Encode once per corpus ID and reuse unchanged for all platforms and repetitions.",
        "planned_trial_count": len(trials),
        "approved_platform_operation_count": len(APPROVED_WORKFLOWS),
        "approved_corpus_count": len(APPROVED_CORPUS_IDS),
        "repetitions_per_corpus_message": len(REPETITIONS),
        "trials": trials,
    }


def _preflight(output_root: Path, manifest: dict[str, Any]) -> None:
    if not output_root.is_dir():
        raise FileNotFoundError(f"production root does not exist: {output_root}")
    missing = [platform_dir for _, platform_dir, _ in APPROVED_WORKFLOWS if not (output_root / platform_dir).is_dir()]
    if missing:
        raise FileNotFoundError(f"required existing platform folder(s) missing: {missing}")
    collisions = []
    for record in manifest["trials"]:
        trial_folder = output_root / Path(record["record_path"]).parent
        if trial_folder.exists():
            collisions.append(str(trial_folder))
    for corpus_id in APPROVED_CORPUS_IDS:
        canonical = output_root / "canonical_inputs" / f"{corpus_id}_encoded.txt"
        if canonical.exists():
            collisions.append(str(canonical))
    if collisions:
        raise FileExistsError("preparation stopped; existing trial/canonical data would be overwritten: " + ", ".join(collisions[:5]))


def prepare_inputs(output_root: Path, corpus_path: Path) -> dict[str, Any]:
    """Create the existing-folder layout using one encode call per corpus ID."""
    corpus = load_and_validate_corpus(corpus_path)
    manifest = build_manifest()
    _preflight(output_root, manifest)
    encoded_by_id: dict[str, str] = {}
    for corpus_id in APPROVED_CORPUS_IDS:
        encoded = embed_secret(COVER_TEXT, corpus[corpus_id]["text"], recovery_mode=RECOVERY_MODE)
        if extract_secret(encoded) == corpus[corpus_id]["text"]:
            encoded_by_id[corpus_id] = encoded
    canonical_root = output_root / "canonical_inputs"
    canonical_root.mkdir()
    for corpus_id, encoded in encoded_by_id.items():
        write_exact_utf8(canonical_root / f"{corpus_id}_encoded.txt", encoded)
    for record in manifest["trials"]:
        encoded = encoded_by_id.get(record["corpus_id"])
        trial_root = output_root / Path(record["record_path"]).parent
        trial_root.mkdir(parents=True)
        (trial_root / "evidence").mkdir()
        if encoded is None:
            record["status"] = "blocked_local_validation"
            record["local_validation"] = {"passed": False, "exact_round_trip": False}
            record["input_sha256"] = None
            sent = ""
        else:
            record["status"] = "ready_for_manual_transfer"
            record["local_validation"] = {"passed": True, "exact_round_trip": True}
            record["input_sha256"] = hashlib.sha256(encoded.encode("utf-8")).hexdigest()
            sent = encoded
        write_exact_utf8(output_root / record["sent_path"], sent)
        write_exact_utf8(output_root / record["retrieved_path"], "")
        write_exact_utf8(output_root / record["record_path"], json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    manifest["prepared_trial_count"] = len(manifest["trials"])
    write_exact_utf8(output_root.parent / "production_manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    return manifest


def analyze_trial(record: dict[str, Any], corpus: dict[str, dict[str, Any]], root: Path, write_result: bool = True) -> dict[str, Any]:
    """Analyze one trial and persist the result beside its raw files."""
    errors: list[str] = []
    record_status = record.get("status")
    sent_path = root / record.get("sent_path", "")
    retrieved_path = root / record.get("retrieved_path", "")
    if record_status not in {"completed", "failed"}:
        errors.append("trial status must be completed or failed after manual transfer")
    if not sent_path.is_file() or not retrieved_path.is_file():
        errors.extend(f"missing raw file: {path}" for path in (sent_path, retrieved_path) if not path.is_file())
        result = {"trial_id": record.get("trial_id"), "analysis_status": "incomplete", "valid": False,
                  "validation_errors": errors}
        return _persist_result(record, result, root, write_result)
    sent, retrieved = read_exact_utf8(sent_path), read_exact_utf8(retrieved_path)
    if not retrieved:
        errors.append("retrieved file is empty; no platform result has been supplied")
        result = {"trial_id": record.get("trial_id"), "analysis_status": "incomplete", "valid": False,
                  "validation_errors": errors}
        return _persist_result(record, result, root, write_result)
    if record_status not in {"completed", "failed"}:
        result = {"trial_id": record.get("trial_id"), "analysis_status": "incomplete", "valid": False,
                  "validation_errors": errors}
        return _persist_result(record, result, root, write_result)
    corpus_id = record.get("corpus_id")
    if corpus_id not in corpus:
        errors.append(f"unknown corpus_id: {corpus_id!r}")
        measured = None
    else:
        measured = analyze_recovered_text(sent, retrieved, corpus[corpus_id]["text"])
    if record.get("input_sha256") and hashlib.sha256(sent.encode("utf-8")).hexdigest() != record["input_sha256"]:
        errors.append("sent input SHA-256 does not match the trial record")
    result = {"trial_id": record.get("trial_id"), "analysis_status": "completed", "valid": not errors,
              "validation_errors": errors, "measured": measured}
    return _persist_result(record, result, root, write_result)


def _persist_result(record: dict[str, Any], result: dict[str, Any], root: Path, write_result: bool) -> dict[str, Any]:
    record["measured_results"] = result.get("measured")
    record["analysis_status"] = result["analysis_status"]
    record["analysis_errors"] = result["validation_errors"]
    if write_result:
        record_path = root / record["record_path"]
        if record_path.parent.is_dir():
            write_exact_utf8(record_path, json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    return result


def planned_count() -> int:
    return len(APPROVED_WORKFLOWS) * len(APPROVED_CORPUS_IDS) * len(REPETITIONS)
