"""Tests for Henry's Week 10 production-trial validation support."""

import unittest

from src.production_trial_validation import (
    analyze_trial_record,
    duplicate_errors,
    validate_trial_metadata,
)
from src.zero_width_codec import count_codec_characters, embed_secret


def valid_record() -> dict:
    sent = embed_secret("Team 1 compatibility test.", "Hello")
    counts = count_codec_characters(sent)
    return {
        "trial_id": "GMAIL-SA01-R1",
        "platform": "Gmail",
        "operation": "send_and_retrieve",
        "corpus_id": "SA01",
        "repetition": 1,
        "tester": "Tristan Koch",
        "timestamp_utc": "2026-10-22T08:00:00Z",
        "codec_commit": "4134cec1d23be3ae7069440a3718e09069922bdc",
        "recovery_mode": False,
        "sent_path": "raw/GMAIL-SA01-R1-sent.txt",
        "retrieved_path": "raw/GMAIL-SA01-R1-retrieved.txt",
        "evidence_paths": ["screenshots/GMAIL-SA01-R1.png"],
        "claimed_metrics": {
            "sent_counts": counts,
            "retrieved_counts": counts,
            "retention_percentage": 100.0,
            "decoder_returned": True,
            "exact_match": True,
            "failure_category": None,
        },
    }


class Week10ProductionTrialValidationTests(unittest.TestCase):
    def test_valid_exact_recovery_record_passes(self) -> None:
        record = valid_record()
        sent = embed_secret("Team 1 compatibility test.", "Hello")
        result = analyze_trial_record(record, sent, sent, "Hello")
        self.assertTrue(result["valid"])
        self.assertEqual(result["validation_errors"], [])

    def test_incorrect_claimed_count_is_rejected(self) -> None:
        record = valid_record()
        record["claimed_metrics"]["retrieved_counts"] = {
            "U+200B": 0,
            "U+200C": 0,
            "U+200D": 0,
            "total": 0,
        }
        sent = embed_secret("Team 1 compatibility test.", "Hello")
        result = analyze_trial_record(record, sent, sent, "Hello")
        self.assertFalse(result["valid"])
        self.assertTrue(
            any("retrieved_counts" in error for error in result["validation_errors"])
        )

    def test_unapproved_operation_is_rejected(self) -> None:
        record = valid_record()
        record["operation"] = "paste_and_copy_back"
        errors = validate_trial_metadata(record)
        self.assertTrue(any("approved workflow" in error for error in errors))

    def test_missing_evidence_is_rejected(self) -> None:
        record = valid_record()
        record["evidence_paths"] = []
        self.assertIn(
            "evidence_paths must be a nonempty list",
            validate_trial_metadata(record),
        )

    def test_duplicates_are_reported_for_both_records(self) -> None:
        first = valid_record()
        second = valid_record()
        errors = duplicate_errors([first, second])
        self.assertIn(0, errors)
        self.assertIn(1, errors)
        self.assertEqual(len(errors[0]), 2)
        self.assertEqual(len(errors[1]), 2)


if __name__ == "__main__":
    unittest.main()
