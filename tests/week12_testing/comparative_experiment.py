"""Run the reproducible Week 12 Baseline-versus-Hamming experiment.

The runner is separate from ``comparative_pilot.py`` and writes only to the
separate full-experiment output directory.  It refuses to overwrite a
non-empty output directory.  Unexpected programming or analysis exceptions
are allowed to propagate and are not converted into decoder failures.

The experiment matrix is four frozen corpus messages, two encoding modes, five
corruption conditions, and three repetitions: 120 trials total.  Bit targets
are fixed logical coordinates approved by the team.  Deletion positions are
sampled independently within each encoded representation using the same
repetition-specific seed for Baseline and Hamming.
"""

from __future__ import annotations

import hashlib
import json
import math
import random
import sys
from collections import Counter
from pathlib import Path
from statistics import mean
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.failure_analysis import analyze_recovered_text
from src.week11_production import load_and_validate_corpus
from src.zero_width_codec import ONE, SEPARATOR, ZERO, count_codec_characters, encode_secret


CORPUS_PATH = ROOT / "tests" / "fixtures" / "week9_corpus.json"
DEFAULT_OUTPUT = ROOT / "tests" / "week12_testing" / "comparative_experiment_output"
CORPUS_IDS = ("SA01", "SU01", "LA01", "LU01")
MODES = ("baseline", "hamming")
CONDITIONS = (
    "no_corruption",
    "single_bit_corruption",
    "double_bit_corruption",
    "deletion_1_percent",
    "deletion_5_percent",
)
REPETITIONS = (1, 2, 3)
SEED_PAIRS = {
    1: {"bit_seed": 481201, "deletion_seed": 481202},
    2: {"bit_seed": 481211, "deletion_seed": 481212},
    3: {"bit_seed": 481221, "deletion_seed": 481222},
}
LOGICAL_FRAME_BYTE_INDEX = 9
SINGLE_BIT_POSITION = 1
DOUBLE_BIT_POSITIONS = (1, 5)
DELETION_PERCENTAGES = {
    "deletion_1_percent": 0.01,
    "deletion_5_percent": 0.05,
}
HAMMING_DATA_POSITIONS = (3, 5, 6, 7, 9, 10, 11, 12)  # one-based
OUTCOME_CATEGORIES = ("successful_recovery", "detected_failure", "undetected_error")


def _flip(symbol: str) -> str:
    if symbol == ZERO:
        return ONE
    if symbol == ONE:
        return ZERO
    raise ValueError("only ZERO and ONE symbols can be flipped")


def _round_half_up(value: float) -> int:
    return math.floor(value + 0.5)


def _logical_schedule(repetition: int) -> dict[str, Any]:
    seeds = SEED_PAIRS[repetition]
    return {
        "bit_seed": seeds["bit_seed"],
        "frame_byte_index": LOGICAL_FRAME_BYTE_INDEX,
        "single_bit_position": SINGLE_BIT_POSITION,
        "double_bit_positions": list(DOUBLE_BIT_POSITIONS),
        "coordinate_definition": "frame byte index and frame data-bit position, both zero-based",
        "bit_seed_role": "recorded repetition-specific reproducibility seed; approved logical targets are fixed",
    }


def _bit_locations(encoded: str, mode: str) -> dict[tuple[int, int], dict[str, Any]]:
    locations: dict[tuple[int, int], dict[str, Any]] = {}
    if mode == "baseline":
        frame_byte = 0
        bit_position = 0
        for physical_index, symbol in enumerate(encoded):
            if symbol == SEPARATOR:
                frame_byte += 1
                bit_position = 0
            elif symbol in (ZERO, ONE):
                locations[(frame_byte, bit_position)] = {
                    "physical_index": physical_index,
                    "frame_byte_index": frame_byte,
                    "data_bit_position": bit_position,
                    "physical_position": bit_position,
                }
                bit_position += 1
        return locations

    if mode != "hamming":
        raise ValueError(f"unknown encoding mode: {mode}")

    data_positions_zero_based = tuple(position - 1 for position in HAMMING_DATA_POSITIONS)
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
            if codeword_position in data_positions_zero_based:
                data_bit = data_positions_zero_based.index(codeword_position)
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
    bit_positions: Iterable[int],
) -> tuple[str, list[dict[str, Any]]]:
    locations = _bit_locations(encoded, mode)
    chars = list(encoded)
    mapped_locations = []
    for bit_position in bit_positions:
        location = locations[(frame_byte_index, bit_position)]
        mapped_locations.append(dict(location))
        physical_index = location["physical_index"]
        chars[physical_index] = _flip(chars[physical_index])
    return "".join(chars), mapped_locations


def _eligible_deletion_locations(encoded: str, mode: str) -> list[dict[str, Any]]:
    locations: list[dict[str, Any]] = []
    if mode == "baseline":
        frame_byte = 0
        bit_position = 0
        for physical_index, symbol in enumerate(encoded):
            if symbol == SEPARATOR:
                frame_byte += 1
                bit_position = 0
            elif symbol in (ZERO, ONE):
                locations.append({
                    "physical_index": physical_index,
                    "symbol": symbol,
                    "frame_byte_index": frame_byte,
                    "data_bit_position": bit_position,
                })
                bit_position += 1
        return locations

    if mode != "hamming":
        raise ValueError(f"unknown encoding mode: {mode}")

    data_positions_zero_based = tuple(position - 1 for position in HAMMING_DATA_POSITIONS)
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
                    data_positions_zero_based.index(codeword_position)
                    if codeword_position in data_positions_zero_based
                    else None
                ),
            })
            codeword_position += 1
    return locations


def _delete_symbols(
    encoded: str,
    mode: str,
    percentage: float,
    deletion_seed: int,
) -> tuple[str, dict[str, Any]]:
    eligible = _eligible_deletion_locations(encoded, mode)
    target_count = _round_half_up(len(eligible) * percentage)
    rng = random.Random(deletion_seed)
    selected_indices = sorted(rng.sample(range(len(eligible)), target_count))
    removed = [eligible[index] for index in selected_indices]
    removed_indices = {item["physical_index"] for item in removed}
    damaged = "".join(
        symbol for index, symbol in enumerate(encoded) if index not in removed_indices
    )
    return damaged, {
        "deletion_seed": deletion_seed,
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


def _corrupt(
    encoded: str,
    mode: str,
    condition: str,
    repetition: int,
) -> tuple[str, dict[str, Any]]:
    seeds = SEED_PAIRS[repetition]
    schedule = _logical_schedule(repetition)
    if condition == "no_corruption":
        return encoded, {
            "bit_seed": seeds["bit_seed"],
            "deletion_seed": seeds["deletion_seed"],
            "affected_symbol_count": 0,
        }
    if condition == "single_bit_corruption":
        damaged, locations = _flip_logical_bits(
            encoded,
            mode,
            LOGICAL_FRAME_BYTE_INDEX,
            (SINGLE_BIT_POSITION,),
        )
        return damaged, {
            "bit_seed": seeds["bit_seed"],
            "deletion_seed": seeds["deletion_seed"],
            "logical_target": schedule,
            "affected_symbol_count": 1,
            "mapped_locations": locations,
        }
    if condition == "double_bit_corruption":
        damaged, locations = _flip_logical_bits(
            encoded,
            mode,
            LOGICAL_FRAME_BYTE_INDEX,
            DOUBLE_BIT_POSITIONS,
        )
        return damaged, {
            "bit_seed": seeds["bit_seed"],
            "deletion_seed": seeds["deletion_seed"],
            "logical_target": schedule,
            "affected_symbol_count": 2,
            "mapped_locations": locations,
        }
    if condition in DELETION_PERCENTAGES:
        damaged, metadata = _delete_symbols(
            encoded,
            mode,
            DELETION_PERCENTAGES[condition],
            seeds["deletion_seed"],
        )
        metadata["bit_seed"] = seeds["bit_seed"]
        return damaged, metadata
    raise ValueError(f"unknown corruption condition: {condition}")


def _measure(
    *,
    corpus: dict[str, Any],
    mode: str,
    condition: str,
    repetition: int,
    original_encoded: str,
    damaged_encoded: str,
    corruption: dict[str, Any],
    baseline_encoded_length: int,
) -> dict[str, Any]:
    analysis = analyze_recovered_text(original_encoded, damaged_encoded, corpus["text"])
    recovered = analysis.get("recovered_secret")
    decoder_returned = bool(analysis.get("decoder_returned"))
    exact_match = decoder_returned and recovered == corpus["text"]
    detected_failure = not decoder_returned
    undetected_error = decoder_returned and not exact_match
    outcome = (
        "successful_recovery" if exact_match else
        "undetected_error" if undetected_error else
        "detected_failure"
    )
    counts = count_codec_characters(original_encoded)
    return {
        "trial_id": f"W12_{corpus['id']}_{mode}_{condition}_R{repetition}",
        "corpus_id": corpus["id"],
        "expected_secret": corpus["text"],
        "encoding_mode": mode,
        "corruption_condition": condition,
        "repetition": repetition,
        "sent_zero_width_character_counts": counts,
        "retrieved_zero_width_character_counts": analysis["retrieved_counts"],
        "retention_percentage": analysis["retention_percentage"],
        "encoded_length": len(original_encoded),
        "encoded_length_overhead_relative_to_baseline_percent": (
            (len(original_encoded) / baseline_encoded_length - 1) * 100
        ),
        "corruption": corruption,
        "decoder_result": analysis,
        "recovered_secret": recovered,
        "exact_match": exact_match,
        "outcome": outcome,
        "failure_detected": detected_failure,
        "incorrect_recovery_without_detection": undetected_error,
        "encoded_sha256": hashlib.sha256(original_encoded.encode("utf-8")).hexdigest(),
        "damaged_encoded_sha256": hashlib.sha256(damaged_encoded.encode("utf-8")).hexdigest(),
    }


def _build_trials(corpus: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    trials: list[dict[str, Any]] = []
    for corpus_id in CORPUS_IDS:
        entry = corpus[corpus_id]
        encoded = {
            "baseline": encode_secret(entry["text"]),
            "hamming": encode_secret(entry["text"], error_correction="hamming"),
        }
        baseline_length = len(encoded["baseline"])
        for mode in MODES:
            for repetition in REPETITIONS:
                for condition in CONDITIONS:
                    damaged, corruption = _corrupt(
                        encoded[mode], mode, condition, repetition
                    )
                    trials.append(_measure(
                        corpus=entry,
                        mode=mode,
                        condition=condition,
                        repetition=repetition,
                        original_encoded=encoded[mode],
                        damaged_encoded=damaged,
                        corruption=corruption,
                        baseline_encoded_length=baseline_length,
                    ))
    return trials


def _expected_trial_keys() -> set[tuple[str, str, str, int]]:
    return {
        (corpus_id, mode, condition, repetition)
        for corpus_id in CORPUS_IDS
        for mode in MODES
        for condition in CONDITIONS
        for repetition in REPETITIONS
    }


def _validate_trial_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    invalid: list[dict[str, Any]] = []
    expected = _expected_trial_keys()
    actual = [
        (record.get("corpus_id"), record.get("encoding_mode"),
         record.get("corruption_condition"), record.get("repetition"))
        for record in records
    ]
    counts = Counter(actual)
    for key in sorted(expected | set(actual)):
        if counts[key] != 1:
            invalid.append({"combination": list(key), "record_count": counts[key]})
    for record in records:
        trial_id = record.get("trial_id")
        corpus_id = record.get("corpus_id")
        mode = record.get("encoding_mode")
        condition = record.get("corruption_condition")
        repetition = record.get("repetition")
        corruption = record.get("corruption", {})
        if record.get("outcome") not in OUTCOME_CATEGORIES:
            invalid.append({"trial_id": trial_id, "issue": "invalid outcome"})
        if "affected_symbol_count" not in corruption:
            invalid.append({"trial_id": trial_id, "issue": "missing affected_symbol_count"})
        expected_seeds = SEED_PAIRS.get(repetition)
        if expected_seeds is None:
            invalid.append({"trial_id": trial_id, "issue": "invalid repetition"})
        else:
            for seed_name in ("bit_seed", "deletion_seed"):
                if corruption.get(seed_name) != expected_seeds[seed_name]:
                    invalid.append({
                        "trial_id": trial_id,
                        "issue": f"invalid or missing {seed_name}",
                    })
        expected_affected = {
            "no_corruption": 0,
            "single_bit_corruption": 1,
            "double_bit_corruption": 2,
        }.get(condition)
        if expected_affected is not None and corruption.get("affected_symbol_count") != expected_affected:
            invalid.append({"trial_id": trial_id, "issue": "incorrect affected_symbol_count"})
        if condition in DELETION_PERCENTAGES:
            removed = corruption.get("removed_symbols", [])
            physical_positions = [item.get("physical_index") for item in removed]
            affected = corruption.get("affected_symbol_count")
            eligible_before = corruption.get("eligible_symbol_count_before")
            eligible_after = corruption.get("eligible_symbol_count_after")
            actual_percentage = corruption.get("actual_deletion_percentage")
            if not isinstance(affected, int) or not isinstance(eligible_before, int):
                invalid.append({"trial_id": trial_id, "issue": "invalid deletion count types"})
                continue
            if len(removed) != affected or len(set(physical_positions)) != len(physical_positions):
                invalid.append({"trial_id": trial_id, "issue": "deletion position/count mismatch"})
            if eligible_before is None or eligible_after != eligible_before - affected:
                invalid.append({"trial_id": trial_id, "issue": "eligible deletion count mismatch"})
            if corruption.get("target_deletion_percentage") != DELETION_PERCENTAGES[condition] * 100:
                invalid.append({"trial_id": trial_id, "issue": "incorrect deletion percentage target"})
            if eligible_before:
                expected_percentage = affected / eligible_before * 100
                if actual_percentage != expected_percentage:
                    invalid.append({"trial_id": trial_id, "issue": "incorrect actual deletion percentage"})
            expected_target = _round_half_up(eligible_before * DELETION_PERCENTAGES[condition])
            if corruption.get("target_symbol_removal_count") != expected_target:
                invalid.append({"trial_id": trial_id, "issue": "incorrect deletion target count"})
        if condition in {"single_bit_corruption", "double_bit_corruption"}:
            target = corruption.get("logical_target", {})
            if target.get("frame_byte_index") != LOGICAL_FRAME_BYTE_INDEX:
                invalid.append({"trial_id": trial_id, "issue": "incorrect logical frame-byte target"})
            expected_bits = (
                [SINGLE_BIT_POSITION]
                if condition == "single_bit_corruption"
                else list(DOUBLE_BIT_POSITIONS)
            )
            if target.get("single_bit_position") != SINGLE_BIT_POSITION or target.get("double_bit_positions") != list(DOUBLE_BIT_POSITIONS):
                invalid.append({"trial_id": trial_id, "issue": "incorrect logical bit schedule"})
            mapped = corruption.get("mapped_locations", [])
            if [item.get("data_bit_position") for item in mapped] != expected_bits:
                invalid.append({"trial_id": trial_id, "issue": "incorrect mapped bit positions"})

    for corpus_id in CORPUS_IDS:
        for condition in CONDITIONS:
            for repetition in REPETITIONS:
                paired = [
                    record for record in records
                    if record.get("corpus_id") == corpus_id
                    and record.get("corruption_condition") == condition
                    and record.get("repetition") == repetition
                ]
                if len(paired) == 2:
                    baseline, hamming = sorted(paired, key=lambda item: item.get("encoding_mode", ""))
                    if baseline.get("corruption") != hamming.get("corruption"):
                        baseline_seeds = {
                            key: baseline.get("corruption", {}).get(key)
                            for key in ("bit_seed", "deletion_seed")
                        }
                        hamming_seeds = {
                            key: hamming.get("corruption", {}).get(key)
                            for key in ("bit_seed", "deletion_seed")
                        }
                        if baseline_seeds != hamming_seeds:
                            invalid.append({
                                "corpus_id": corpus_id,
                                "condition": condition,
                                "repetition": repetition,
                                "issue": "Baseline/Hamming seed mismatch",
                            })
                    if condition in {"single_bit_corruption", "double_bit_corruption"}:
                        if baseline.get("corruption", {}).get("logical_target") != hamming.get("corruption", {}).get("logical_target"):
                            invalid.append({
                                "corpus_id": corpus_id,
                                "condition": condition,
                                "repetition": repetition,
                                "issue": "Baseline/Hamming logical target mismatch",
                            })
    return invalid


def _aggregate(records: list[dict[str, Any]], invalid_records: list[dict[str, Any]]) -> dict[str, Any]:
    def count_by(field: str) -> dict[str, int]:
        return dict(sorted(Counter(str(record[field]) for record in records).items()))

    outcome_counts = dict.fromkeys(OUTCOME_CATEGORIES, 0)
    for record in records:
        outcome_counts[record["outcome"]] += 1

    success_rates: dict[str, dict[str, float | None]] = {}
    for mode in MODES:
        success_rates[mode] = {}
        for condition in CONDITIONS:
            matching = [
                record for record in records
                if record["encoding_mode"] == mode and record["corruption_condition"] == condition
            ]
            success_rates[mode][condition] = (
                sum(record["outcome"] == "successful_recovery" for record in matching) / len(matching) * 100
                if matching else None
            )

    by_corpus_mode: dict[str, Any] = {}
    for corpus_id in CORPUS_IDS:
        by_corpus_mode[corpus_id] = {}
        for mode in MODES:
            matching = [
                record for record in records
                if record["corpus_id"] == corpus_id and record["encoding_mode"] == mode
            ]
            by_corpus_mode[corpus_id][mode] = {
                "trial_count": len(matching),
                "outcome_counts": {
                    category: sum(record["outcome"] == category for record in matching)
                    for category in OUTCOME_CATEGORIES
                },
                "average_encoded_length": mean(record["encoded_length"] for record in matching),
                "average_retention_percentage": mean(record["retention_percentage"] for record in matching),
            }

    deletion_statistics: dict[str, Any] = {}
    for mode in MODES:
        deletion_statistics[mode] = {}
        for condition in DELETION_PERCENTAGES:
            matching = [
                record for record in records
                if record["encoding_mode"] == mode and record["corruption_condition"] == condition
            ]
            deletion_statistics[mode][condition] = {
                "affected_symbol_counts": [record["corruption"]["affected_symbol_count"] for record in matching],
                "actual_deletion_percentages": [record["corruption"]["actual_deletion_percentage"] for record in matching],
                "eligible_symbol_counts_before": [record["corruption"]["eligible_symbol_count_before"] for record in matching],
            }

    retention_by_mode_and_condition: dict[str, dict[str, float | None]] = {}
    for mode in MODES:
        retention_by_mode_and_condition[mode] = {}
        for condition in CONDITIONS:
            matching = [
                record["retention_percentage"] for record in records
                if record["encoding_mode"] == mode and record["corruption_condition"] == condition
            ]
            retention_by_mode_and_condition[mode][condition] = mean(matching) if matching else None

    overheads: dict[str, dict[str, float]] = {}
    for corpus_id in CORPUS_IDS:
        baseline = next(
            record["encoded_length"] for record in records
            if record["corpus_id"] == corpus_id and record["encoding_mode"] == "baseline"
        )
        overheads[corpus_id] = {
            mode: next(
                record["encoded_length_overhead_relative_to_baseline_percent"]
                for record in records
                if record["corpus_id"] == corpus_id and record["encoding_mode"] == mode
            )
            for mode in MODES
        }
        overheads[corpus_id]["baseline_encoded_length"] = baseline

    return {
        "total_trials": len(records),
        "expected_total_trials": 120,
        "corpus_messages": list(CORPUS_IDS),
        "modes": list(MODES),
        "conditions": list(CONDITIONS),
        "repetitions": list(REPETITIONS),
        "repetitions_per_combination": 3,
        "trial_counts_by_corpus": count_by("corpus_id"),
        "trial_counts_by_mode": count_by("encoding_mode"),
        "trial_counts_by_condition": count_by("corruption_condition"),
        "outcome_counts": outcome_counts,
        "recovery_success_rates_by_mode_and_condition_percent": success_rates,
        "results_by_corpus_and_mode": by_corpus_mode,
        "average_encoded_length_and_overhead": overheads,
        "deletion_statistics": deletion_statistics,
        "retention_percentages": {
            "average": mean(record["retention_percentage"] for record in records),
            "by_mode_and_condition": retention_by_mode_and_condition,
        },
        "invalid_records": invalid_records,
        "unexpected_execution_errors": [],
    }


def _write_report(output: Path, summary: dict[str, Any]) -> None:
    lines = [
        "# Week 12 Baseline vs. Hamming Comparative Experiment",
        "",
        "This report was generated from the individual trial JSON records.",
        "The experiment uses four corpus messages, two modes, five conditions,",
        "and three deterministic repetitions per combination (120 trials total).",
        "",
        "## Seed pairs",
        "",
        "| Repetition | Bit seed | Deletion seed |",
        "|---:|---:|---:|",
    ]
    for repetition in REPETITIONS:
        seeds = SEED_PAIRS[repetition]
        lines.append(f"| R{repetition} | {seeds['bit_seed']} | {seeds['deletion_seed']} |")
    lines.extend([
        "",
        "Bit targets are frame byte 9, bit 1 for single-bit corruption, and",
        "frame byte 9, bits 1 and 5 for double-bit corruption. Targets are",
        "mapped to representation-specific physical positions.",
        "",
        "Deletion eligibility includes ZERO and ONE symbols, including Hamming",
        "parity symbols, and excludes separators and the two-symbol Hamming prefix.",
        "Requested deletion counts use nearest-integer half-up rounding.",
        "",
        "## Outcome totals",
        "",
        f"- Total trials: {summary['total_trials']}",
    ])
    for category, count in summary["outcome_counts"].items():
        lines.append(f"- {category}: {count}")
    lines.extend([
        "",
        "Unexpected execution errors are kept separate from decoder outcomes.",
        "To reproduce the experiment, run the command documented in the methodology file.",
    ])
    (output / "experiment_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_experiment(output: Path = DEFAULT_OUTPUT) -> dict[str, Any]:
    if output.exists() and any(output.iterdir()):
        raise FileExistsError(f"refusing to overwrite non-empty output directory: {output}")

    corpus = load_and_validate_corpus(CORPUS_PATH)
    selected_corpus = {corpus_id: corpus[corpus_id] for corpus_id in CORPUS_IDS}
    trials = _build_trials(selected_corpus)
    invalid_records = _validate_trial_records(trials)
    if invalid_records or len(trials) != 120:
        raise RuntimeError(f"trial matrix validation failed: {invalid_records}")

    output.mkdir(parents=True, exist_ok=True)
    for record in trials:
        filename = (
            f"{record['corpus_id']}_{record['encoding_mode']}_"
            f"{record['corruption_condition']}_R{record['repetition']}.json"
        )
        (output / filename).write_text(
            json.dumps(record, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    written_records = [
        json.loads(path.read_text(encoding="utf-8"))
        for path in sorted(output.glob("*.json"))
        if path.name != "summary.json"
    ]
    written_invalid = _validate_trial_records(written_records)
    summary = _aggregate(written_records, written_invalid)
    if written_invalid or summary["total_trials"] != 120:
        raise RuntimeError(f"written-record validation failed: {written_invalid}")
    (output / "summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    _write_report(output, summary)
    return summary


if __name__ == "__main__":
    result = run_experiment()
    print(json.dumps({
        "output": str(DEFAULT_OUTPUT),
        "total_trials": result["total_trials"],
        "outcome_counts": result["outcome_counts"],
    }, indent=2))
