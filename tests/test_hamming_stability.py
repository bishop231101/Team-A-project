"""Week 12 stabilization tests for the optional Hamming SECDED mode."""

from __future__ import annotations

import itertools
import json
import unittest
from pathlib import Path

from src.zero_width_codec import (
    DecodeError,
    ONE,
    SEPARATOR,
    ZERO,
    count_codec_characters,
    encode_secret,
    extract_secret,
)


CORPUS_PATH = Path(__file__).parent / "fixtures" / "week9_corpus.json"


def _flip(symbol: str) -> str:
    return ONE if symbol == ZERO else ZERO


def _damage_hamming_codeword(
    encoded: str,
    codeword_index: int,
    positions: tuple[int, ...],
) -> str:
    codewords = [list(codeword) for codeword in encoded[2:].split(SEPARATOR)]
    for position in positions:
        codewords[codeword_index][position] = _flip(codewords[codeword_index][position])
    return (SEPARATOR * 2) + SEPARATOR.join("".join(codeword) for codeword in codewords)


class HammingStabilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.corpus = json.loads(CORPUS_PATH.read_text(encoding="utf-8"))

    def test_complete_corpus_round_trips_in_both_modes(self) -> None:
        for entry in self.corpus:
            secret = entry["text"]
            with self.subTest(message_id=entry["id"], mode="standard"):
                self.assertEqual(extract_secret(encode_secret(secret)), secret)
            with self.subTest(message_id=entry["id"], mode="hamming"):
                protected = encode_secret(secret, error_correction="hamming")
                self.assertEqual(extract_secret(protected), secret)
                self.assertEqual(
                    protected,
                    encode_secret(secret, error_correction="hamming"),
                )

    def test_single_error_in_each_codeword_is_corrected_for_complete_corpus(self) -> None:
        for entry in self.corpus:
            secret = entry["text"]
            encoded = encode_secret(secret, error_correction="hamming")
            codeword_count = len(encoded[2:].split(SEPARATOR))
            damaged = encoded
            for codeword_index in range(codeword_count):
                damaged = _damage_hamming_codeword(
                    damaged,
                    codeword_index,
                    (codeword_index % 13,),
                )
            with self.subTest(message_id=entry["id"]):
                self.assertEqual(extract_secret(damaged), secret)

    def test_all_double_bit_pairs_are_rejected(self) -> None:
        secret = "Week 12 double-bit rejection"
        encoded = encode_secret(secret, error_correction="hamming")
        payload_codeword = 8
        for positions in itertools.combinations(range(13), 2):
            with self.subTest(positions=positions):
                damaged = _damage_hamming_codeword(encoded, payload_codeword, positions)
                with self.assertRaisesRegex(DecodeError, "double-bit"):
                    extract_secret(damaged)

    def test_all_triple_bit_patterns_do_not_return_false_success(self) -> None:
        secret = "Week 12 false-success prevention"
        encoded = encode_secret(secret, error_correction="hamming")
        payload_codeword = 8
        for positions in itertools.combinations(range(13), 3):
            with self.subTest(positions=positions):
                damaged = _damage_hamming_codeword(encoded, payload_codeword, positions)
                with self.assertRaises(DecodeError):
                    extract_secret(damaged)

    def test_damaged_prefix_and_codeword_separator_are_rejected(self) -> None:
        encoded = encode_secret("separator integrity", error_correction="hamming")
        missing_prefix_symbol = encoded[1:]
        first_separator = encoded.find(SEPARATOR, 2)
        missing_codeword_separator = (
            encoded[:first_separator] + encoded[first_separator + 1 :]
        )
        for name, damaged in (
            ("missing prefix symbol", missing_prefix_symbol),
            ("missing codeword separator", missing_codeword_separator),
        ):
            with self.subTest(name=name):
                with self.assertRaises(DecodeError):
                    extract_secret(damaged)

    def test_encoded_length_matches_documented_format(self) -> None:
        for entry in self.corpus:
            secret = entry["text"]
            frame_bytes = 12 + len(secret.encode("utf-8"))
            standard = encode_secret(secret)
            protected = encode_secret(secret, error_correction="hamming")
            standard_count = count_codec_characters(standard)["total"]
            protected_count = count_codec_characters(protected)["total"]
            with self.subTest(message_id=entry["id"]):
                self.assertEqual(standard_count, (9 * frame_bytes) - 1)
                self.assertEqual(protected_count, (14 * frame_bytes) + 1)
                self.assertGreater(protected_count, standard_count)
                self.assertLess(protected_count, standard_count * 2)

    def test_large_unicode_boundary_round_trip(self) -> None:
        secret = "Café 世界 🔐\n" * 512
        encoded = encode_secret(secret, error_correction="hamming")
        self.assertEqual(extract_secret(encoded), secret)


if __name__ == "__main__":
    unittest.main()
