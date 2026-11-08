"""Prepare and run the single-repetition Week 12 SA01 comparison pilot.

This script is intentionally separate from the codec and from existing trial
evidence.  It writes a new output directory and refuses to write if that
directory already contains files.  Henry must review this script before the
planned execution command is run.

The corruption schedule is defined in logical coordinates.  A bit corruption
uses one frame-byte index and one or two data-bit positions (0 through 7),
then maps those coordinates to the standard byte block or to the Hamming
codeword's data positions.  Deletion sampling is performed separately for
each encoded representation with the same fixed seed.  Only ZERO and ONE
symbols are eligible; separators and the two-symbol Hamming prefix are not.
"""

from __future__ import annotations

import hashlib
import json
import math
import random
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.failure_analysis import analyze_recovered_text
from src.week11_production import load_and_validate_corpus
from src.zero_width_codec import (
    ONE,
    SEPARATOR,
    ZERO,
    count_codec_characters,
    encode_secret,
)


CORPUS_PATH = ROOT / "tests" / "fixtures" / "week9_corpus.json"
DEFAULT_OUTPUT = ROOT / "tests" / "week12_testing" / "comparative_pilot_output"
CORPUS_ID = "SA01"
REPETITION = 1
BIT_SEED = 481201
DELETION_SEED = 481202
DELETION_PERCENTAGES = (0.01, 0.05)
HAMMING_DATA_POSITIONS = (3, 5, 6, 7, 9, 10, 11, 12)  # one-based codeword positions


def _flip(symbol: str) -> str:
    if symbol == ZERO:
        return ONE
    if symbol == ONE:
        return ZERO
    raise ValueError("only ZERO and ONE symbols can be flipped")


def _round_half_up(value: float) -> int:
    """Round a non-negative deletion target to the nearest integer, half up."""
    return math.floor(value + 0.5)


def _logical_bit_schedule(frame_byte_count: int) -> dict[str, Any]:
    rng = random.Random(BIT_SEED)
    frame_byte_index = rng.randrange(frame_byte_count)
    single_bit = rng.randrange(8)
    double_bits = tuple(sorted(rng.sample(range(8), 2)))
    return {
        "seed": BIT_SEED,
        "frame_byte_count": frame_byte_count,
        "frame_byte_index": frame_byte_index,
        "single_bit_position": single_bit,
        "double_bit_positions": list(double_bits),
        "coordinate_definition": "frame byte index and UTF-8 frame data bit position, zero-based",
    }


def _bit_locations(encoded: str, mode: str) -> dict[tuple[int, int], dict[str, Any]]:
    locations: dict[tuple[int, int], dict[str, Any]] = {}
    if mode == "baseline":
        frame_byte = 0
        bit = 0
        for physical_index, symbol in enumerate(encoded):
            if symbol == SEPARATOR:
                frame_byte += 1
                bit = 0
            elif symbol in (ZERO, ONE):
                locations[(frame_byte, bit)] = {
                    "physical_index": physical_index,
                    "frame_byte_index": frame_byte,
                    "data_bit_position": bit,
                    "physical_position": bit,
                }
                bit += 1
        return locations

    if mode != "hamming":
        raise ValueError(f"unknown mode: {mode}")

    codeword_index = 0
    codeword_position = 0
    prefix_remaining = 2
    for physical_index, symbol in enumerate(encoded):
        if prefix_remaining:
            prefix_remaining -= 1
            continue
        if symbol == SEPARATOR:
            codeword_index += 1
            codeword_position = 0
        elif symbol in (ZERO, ONE):
            if codeword_position in (position - 1 for position in HAMMING_DATA_POSITIONS):
                data_bit = tuple(position - 1 for position in HAMMING_DATA_POSITIONS).index(
                    codeword_position
                )
                locations[(codeword_index, data_bit)] = {
                    "physical_index": physical_index,
                    "frame_byte_index": codeword_index,
                    "data_bit_position": data_bit,
                    "codeword_position": codeword_position,
                    "codeword_position_one_based": codeword_position + 1,
                }
            codeword_position += 1
    return locations


def _flip_logical_bits(
    encoded: str,
    mode: str,
    frame_byte_index: int,
    bit_positions: list[int],
) -> tuple[str, list[dict[str, Any]]]:
    locations = _bit_locations(encoded, mode)
    chars = list(encoded)
    physical_locations = []
    for bit_position in bit_positions:
        location = locations[(frame_byte_index, bit_position)]
        physical_locations.append(dict(location))
        index = location["physical_index"]
        chars[index] = _flip(chars[index])
    return "".join(chars), physical_locations


def _eligible_deletion_locations(encoded: str, mode: str) -> list[dict[str, Any]]:
    locations: list[dict[str, Any]] = []
    if mode == "baseline":
        byte_index = 0
        bit_position = 0
        for physical_index, symbol in enumerate(encoded):
            if symbol == SEPARATOR:
                byte_index += 1
                bit_position = 0
            elif symbol in (ZERO, ONE):
                locations.append({
                    "physical_index": physical_index,
                    "symbol": symbol,
                    "frame_byte_index": byte_index,
                    "data_bit_position": bit_position,
                })
                bit_position += 1
        return locations

    codeword_index = 0
    codeword_position = 0
    prefix_remaining = 2
    for physical_index, symbol in enumerate(encoded):
        if prefix_remaining:
            prefix_remaining -= 1
            continue
        if symbol == SEPARATOR:
            codeword_index += 1
            codeword_position = 0
        elif symbol in (ZERO, ONE):
            locations.append({
                "physical_index": physical_index,
                "symbol": symbol,
                "frame_byte_index": codeword_index,
                "codeword_position": codeword_position,
                "codeword_position_one_based": codeword_position + 1,
                "logical_data_bit_position": (
                    tuple(position - 1 for position in HAMMING_DATA_POSITIONS).index(codeword_position)
                    if codeword_position in tuple(position - 1 for position in HAMMING_DATA_POSITIONS)
                    else None
                ),
            })
            codeword_position += 1
    return locations


def _delete_symbols(
    encoded: str, mode: str, percentage: float
) -> tuple[str, dict[str, Any]]:
    eligible = _eligible_deletion_locations(encoded, mode)
    target_count = _round_half_up(len(eligible) * percentage)
    rng = random.Random(DELETION_SEED)
    selected = sorted(rng.sample(range(len(eligible)), target_count))
    removed = [eligible[index] for index in selected]
    removed_indices = {item["physical_index"] for item in removed}
    damaged = "".join(
        symbol for index, symbol in enumerate(encoded) if index not in removed_indices
    )
    details = {
        "seed": DELETION_SEED,
        "eligible_symbol_count_before": len(eligible),
        "target_deletion_percentage": percentage * 100,
        "rounding_rule": "nearest integer, ties rounded up (floor(n * percentage + 0.5))",
        "target_symbol_removal_count": target_count,
        "affected_symbol_count": len(removed),
        "actual_deletion_percentage": (len(removed) / len(eligible) * 100) if eligible else None,
        "removed_symbols": removed,
        "eligible_symbol_count_after": len(eligible) - len(removed),
        "denominator_definition": "ZERO and ONE symbols only; separators and Hamming prefix excluded",
    }
    return damaged, details


def _measure(
    *,
    corpus: dict[str, Any],
    mode: str,
    condition: str,
    original_encoded: str,
    damaged_encoded: str,
    corruption: dict[str, Any],
    baseline_count: int,
) -> dict[str, Any]:
    # Expected DecodeError instances are captured by analyze_recovered_text().
    # Unexpected programming or analysis exceptions are deliberately allowed to
    # propagate with their traceback instead of becoming trial records.
    analysis = analyze_recovered_text(original_encoded, damaged_encoded, corpus["text"])

    recovered = analysis.get("recovered_secret")
    decoder_returned = bool(analysis.get("decoder_returned"))
    exact = decoder_returned and recovered == corpus["text"]
    detected_failure = not decoder_returned
    undetected_incorrect = decoder_returned and not exact
    outcome = (
        "successful_recovery" if exact else
        "undetected_error" if undetected_incorrect else
        "detected_failure"
    )
    return {
        "corpus_id": corpus["id"],
        "expected_secret": corpus["text"],
        "encoding_mode": mode,
        "corruption_condition": condition,
        "repetition": REPETITION,
        "original_encoded_zero_width_character_count": count_codec_characters(original_encoded),
        "encoded_length_overhead_relative_to_baseline_percent": (
            (count_codec_characters(original_encoded)["total"] / baseline_count - 1) * 100
        ),
        "corruption": corruption,
        "decoder_result": analysis,
        "outcome": outcome,
        "recovery_exact": exact,
        "failure_detected": detected_failure,
        "incorrect_recovery_without_detection": undetected_incorrect,
    }


def run_pilot(output: Path = DEFAULT_OUTPUT) -> None:
    if output.exists() and any(output.iterdir()):
        raise FileExistsError(f"refusing to overwrite non-empty output directory: {output}")
    output.mkdir(parents=True, exist_ok=True)

    corpus = load_and_validate_corpus(CORPUS_PATH)[CORPUS_ID]
    frame_byte_count = 12 + len(corpus["text"].encode("utf-8"))
    schedule = _logical_bit_schedule(frame_byte_count)
    encoded = {
        "baseline": encode_secret(corpus["text"]),
        "hamming": encode_secret(corpus["text"], error_correction="hamming"),
    }
    baseline_count = count_codec_characters(encoded["baseline"])["total"]
    trials: list[dict[str, Any]] = []

    plans = [
        ("no_corruption", None),
        ("single_bit_corruption", "single"),
        ("double_bit_corruption", "double"),
        ("deletion_1_percent", DELETION_PERCENTAGES[0]),
        ("deletion_5_percent", DELETION_PERCENTAGES[1]),
    ]
    for mode, original in encoded.items():
        for condition, parameter in plans:
            corruption: dict[str, Any]
            damaged = original
            if parameter == "single":
                damaged, locations = _flip_logical_bits(
                    original, mode, schedule["frame_byte_index"], [schedule["single_bit_position"]]
                )
                corruption = {"schedule": schedule, "affected_symbol_count": 1, "mapped_locations": locations}
            elif parameter == "double":
                damaged, locations = _flip_logical_bits(
                    original, mode, schedule["frame_byte_index"], schedule["double_bit_positions"]
                )
                corruption = {"schedule": schedule, "affected_symbol_count": 2, "mapped_locations": locations}
            elif isinstance(parameter, float):
                damaged, deletion = _delete_symbols(original, mode, parameter)
                corruption = deletion
            else:
                corruption = {"seed": None, "affected_symbol_count": 0}

            trial = _measure(
                corpus=corpus, mode=mode, condition=condition,
                original_encoded=original, damaged_encoded=damaged,
                corruption=corruption, baseline_count=baseline_count,
            )
            trial["encoded_sha256"] = hashlib.sha256(original.encode("utf-8")).hexdigest()
            trial["damaged_encoded_sha256"] = hashlib.sha256(damaged.encode("utf-8")).hexdigest()
            trial["pilot_protocol"] = "Week 12 comparative experiment pilot; SA01; one repetition"
            trials.append(trial)

    for number, trial in enumerate(trials, start=1):
        name = f"trial_{number:02d}_{trial['encoding_mode']}_{trial['corruption_condition']}.json"
        (output / name).write_text(json.dumps(trial, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    outcome_categories = (
        "successful_recovery",
        "detected_failure",
        "undetected_error",
    )
    outcome_counts = {
        category: sum(trial["outcome"] == category for trial in trials)
        for category in outcome_categories
    }
    outcome_counts_by_mode = {
        mode: {
            category: sum(
                trial["encoding_mode"] == mode and trial["outcome"] == category
                for trial in trials
            )
            for category in outcome_categories
        }
        for mode in ("baseline", "hamming")
    }
    summary = {
        "pilot_protocol": "Week 12 comparative experiment pilot; SA01; one repetition",
        "corpus_source": str(CORPUS_PATH.relative_to(ROOT)),
        "corpus_id": CORPUS_ID,
        "expected_secret": corpus["text"],
        "modes": ["baseline", "hamming"],
        "conditions": [condition for condition, _ in plans],
        "fixed_seeds": {"bit_schedule": BIT_SEED, "deletion_sampling": DELETION_SEED},
        "logical_bit_schedule": schedule,
        "deletion_denominator": "ZERO and ONE symbols only; separators and Hamming prefix excluded",
        "outcome_categories": list(outcome_categories),
        "outcome_counts": outcome_counts,
        "outcome_counts_by_mode": outcome_counts_by_mode,
        "trials": trials,
    }
    (output / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    run_pilot()
