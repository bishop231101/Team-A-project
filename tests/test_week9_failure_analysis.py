"""Tests for Week 9 recovered-sequence diagnostics."""

import unittest

from src.failure_analysis import analyze_recovered_text
from src.zero_width_codec import ONE, ZERO, embed_secret


class Week9FailureAnalysisTests(unittest.TestCase):
    def test_exact_recovery_is_reported_separately_from_retention(self) -> None:
        sent = embed_secret("Cover", "CS481")
        result = analyze_recovered_text(sent, sent, "CS481")
        self.assertEqual(result["retention_percentage"], 100.0)
        self.assertTrue(result["decoder_returned"])
        self.assertTrue(result["exact_match"])
        self.assertIsNone(result["failure_category"])

    def test_complete_payload_removal_is_classified(self) -> None:
        sent = embed_secret("Cover", "CS481")
        result = analyze_recovered_text(sent, "Cover", "CS481")
        self.assertEqual(result["retention_percentage"], 0.0)
        self.assertFalse(result["decoder_returned"])
        self.assertEqual(result["failure_category"], "complete_payload_removal")

    def test_malformed_sequence_is_classified_as_structural_corruption(self) -> None:
        sent = embed_secret("Cover", "CS481")
        result = analyze_recovered_text(sent, sent[:-1], "CS481")
        self.assertFalse(result["decoder_returned"])
        self.assertEqual(result["failure_category"], "structural_corruption")

    def test_frame_marker_corruption_is_classified(self) -> None:
        sent = embed_secret("Cover", "CS481")
        first_symbol = next(
            index for index, character in enumerate(sent) if character in {ZERO, ONE}
        )
        replacement = ONE if sent[first_symbol] == ZERO else ZERO
        damaged = sent[:first_symbol] + replacement + sent[first_symbol + 1 :]
        result = analyze_recovered_text(sent, damaged, "CS481")
        self.assertEqual(result["retention_percentage"], 100.0)
        self.assertEqual(result["failure_category"], "frame_marker_corruption")

    def test_retention_above_one_hundred_is_flagged(self) -> None:
        sent = embed_secret("Cover", "CS481")
        result = analyze_recovered_text(sent, sent + ZERO, "CS481")
        self.assertGreater(result["retention_percentage"], 100.0)
        self.assertTrue(result["retention_above_100_percent"])


if __name__ == "__main__":
    unittest.main()
