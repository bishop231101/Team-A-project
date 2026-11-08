"""Read-only unit coverage for the Week 12 comparative experiment helpers."""

from __future__ import annotations

import unittest
from copy import deepcopy
from pathlib import Path

from src.week11_production import load_and_validate_corpus
from src.zero_width_codec import encode_secret
from tests.week12_testing.comparative_experiment import (
    CONDITIONS,
    CORPUS_IDS,
    DELETION_PERCENTAGES,
    DOUBLE_BIT_POSITIONS,
    LOGICAL_FRAME_BYTE_INDEX,
    REPETITIONS,
    SEED_PAIRS,
    SINGLE_BIT_POSITION,
    _corrupt,
    _delete_symbols,
    _aggregate,
    _expected_trial_keys,
    _validate_trial_records,
)


CORPUS_PATH = Path(__file__).parent / "fixtures" / "week9_corpus.json"


def _synthetic_records() -> list[dict[str, object]]:
    records = []
    for corpus_id in CORPUS_IDS:
        for mode in ("baseline", "hamming"):
            for condition in CONDITIONS:
                for repetition in REPETITIONS:
                    seeds = SEED_PAIRS[repetition]
                    corruption: dict[str, object] = {
                        "bit_seed": seeds["bit_seed"],
                        "deletion_seed": seeds["deletion_seed"],
                        "affected_symbol_count": 0,
                    }
                    if condition == "single_bit_corruption":
                        corruption.update({
                            "affected_symbol_count": 1,
                            "logical_target": {
                                "bit_seed": seeds["bit_seed"],
                                "frame_byte_index": 9,
                                "single_bit_position": 1,
                                "double_bit_positions": [1, 5],
                            },
                            "mapped_locations": [{"data_bit_position": 1}],
                        })
                    elif condition == "double_bit_corruption":
                        corruption.update({
                            "affected_symbol_count": 2,
                            "logical_target": {
                                "bit_seed": seeds["bit_seed"],
                                "frame_byte_index": 9,
                                "single_bit_position": 1,
                                "double_bit_positions": [1, 5],
                            },
                            "mapped_locations": [
                                {"data_bit_position": 1},
                                {"data_bit_position": 5},
                            ],
                        })
                    elif condition in DELETION_PERCENTAGES:
                        target_percentage = DELETION_PERCENTAGES[condition] * 100
                        target_count = 1 if condition == "deletion_1_percent" else 5
                        removed = [{"physical_index": index} for index in range(target_count)]
                        corruption.update({
                            "eligible_symbol_count_before": 100,
                            "target_deletion_percentage": target_percentage,
                            "target_symbol_removal_count": target_count,
                            "affected_symbol_count": target_count,
                            "actual_deletion_percentage": target_count,
                            "removed_symbols": removed,
                            "eligible_symbol_count_after": 100 - target_count,
                        })
                    records.append({
                        "trial_id": f"synthetic_{corpus_id}_{mode}_{condition}_R{repetition}",
                        "corpus_id": corpus_id,
                        "encoding_mode": mode,
                        "corruption_condition": condition,
                        "repetition": repetition,
                        "outcome": "successful_recovery",
                        "corruption": corruption,
                        "encoded_length": 100 if mode == "baseline" else 150,
                        "encoded_length_overhead_relative_to_baseline_percent": 0 if mode == "baseline" else 50,
                        "retention_percentage": 100.0,
                    })
    return records


class ComparativeExperimentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        corpus = load_and_validate_corpus(CORPUS_PATH)
        cls.corpus = {corpus_id: corpus[corpus_id] for corpus_id in CORPUS_IDS}

    def test_approved_matrix_has_120_unique_combinations(self) -> None:
        expected = _expected_trial_keys()
        self.assertEqual(len(expected), 120)
        self.assertEqual(len(CORPUS_IDS) * 2 * len(CONDITIONS) * len(REPETITIONS), 120)
        self.assertEqual(len(_validate_trial_records([])), 120)

    def test_seed_pairs_are_distinct_and_recorded(self) -> None:
        self.assertEqual(
            [SEED_PAIRS[repetition]["bit_seed"] for repetition in REPETITIONS],
            [481201, 481211, 481221],
        )
        self.assertEqual(
            [SEED_PAIRS[repetition]["deletion_seed"] for repetition in REPETITIONS],
            [481202, 481212, 481222],
        )
        for repetition in REPETITIONS:
            _, corruption = _corrupt(
                encode_secret(self.corpus["SA01"]["text"]),
                "baseline",
                "single_bit_corruption",
                repetition,
            )
            self.assertEqual(corruption["bit_seed"], SEED_PAIRS[repetition]["bit_seed"])

    def test_logical_bit_targets_are_approved(self) -> None:
        self.assertEqual(LOGICAL_FRAME_BYTE_INDEX, 9)
        self.assertEqual(SINGLE_BIT_POSITION, 1)
        self.assertEqual(DOUBLE_BIT_POSITIONS, (1, 5))
        for mode in ("baseline", "hamming"):
            encoded = encode_secret(self.corpus["SA01"]["text"], error_correction="hamming" if mode == "hamming" else None)
            damaged, metadata = _corrupt(encoded, mode, "double_bit_corruption", 2)
            self.assertNotEqual(damaged, encoded)
            self.assertEqual(metadata["affected_symbol_count"], 2)
            self.assertEqual(
                [item["data_bit_position"] for item in metadata["mapped_locations"]],
                [1, 5],
            )

    def test_deletion_metadata_uses_actual_removals_and_preserves_parity_eligibility(self) -> None:
        for mode in ("baseline", "hamming"):
            encoded = encode_secret(self.corpus["SA01"]["text"], error_correction="hamming" if mode == "hamming" else None)
            damaged, metadata = _delete_symbols(encoded, mode, DELETION_PERCENTAGES["deletion_5_percent"], 481212)
            repeated_damaged, repeated_metadata = _delete_symbols(encoded, mode, DELETION_PERCENTAGES["deletion_5_percent"], 481212)
            self.assertEqual(damaged, repeated_damaged)
            self.assertEqual(metadata, repeated_metadata)
            self.assertEqual(len(encoded) - len(damaged), metadata["affected_symbol_count"])
            self.assertEqual(metadata["target_symbol_removal_count"], metadata["affected_symbol_count"])
            self.assertEqual(
                metadata["actual_deletion_percentage"],
                metadata["affected_symbol_count"] / metadata["eligible_symbol_count_before"] * 100,
            )
            self.assertEqual(
                metadata["eligible_symbol_count_before"] - metadata["affected_symbol_count"],
                metadata["eligible_symbol_count_after"],
            )

    def test_validation_checks_seed_and_deletion_metadata(self) -> None:
        records = _synthetic_records()
        self.assertEqual(_validate_trial_records(records), [])
        corrupted = deepcopy(records)
        corrupted[0]["corruption"]["bit_seed"] = 999999  # type: ignore[index]
        self.assertTrue(any("seed" in item["issue"] for item in _validate_trial_records(corrupted)))

    def test_summary_aggregation_uses_synthetic_trial_records(self) -> None:
        records = _synthetic_records()
        summary = _aggregate(records, [])
        self.assertEqual(summary["total_trials"], 120)
        self.assertEqual(summary["trial_counts_by_corpus"], {corpus_id: 30 for corpus_id in CORPUS_IDS})
        self.assertEqual(summary["trial_counts_by_mode"], {"baseline": 60, "hamming": 60})
        self.assertEqual(summary["outcome_counts"]["successful_recovery"], 120)
        self.assertEqual(summary["invalid_records"], [])


if __name__ == "__main__":
    unittest.main()
