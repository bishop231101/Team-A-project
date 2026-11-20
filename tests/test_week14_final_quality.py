"""Final-release compatibility and Hamming diagnostic checks."""

from __future__ import annotations

import hashlib
import unittest

from src.zero_width_codec import (
    ONE,
    SEPARATOR,
    ZERO,
    diagnose_stego_text,
    encode_secret,
    extract_secret,
)


SECRET = "Week 14 compatibility 🔐"
EXPECTED_HASHES = {
    "baseline": "ba2e64dbbc45c59cbb6655d1cf32f25ef940444a4da72851d56b12b9d2dc3ad4",
    "repetition": "1b853e2edce1ad950668b9e5969afd5b15cdbf03b0d8c0e0ccfd5449857d278e",
    "hamming": "bec357e22e8763c8adbc4334d34cdd3e3ee70525aa9b4e193c02ae129c818249",
}


def _flip(symbol: str) -> str:
    return ONE if symbol == ZERO else ZERO


def _damage_codeword(
    encoded: str,
    codeword_index: int,
    positions: tuple[int, ...],
) -> str:
    codewords = [list(codeword) for codeword in encoded[2:].split(SEPARATOR)]
    for position in positions:
        codewords[codeword_index][position] = _flip(codewords[codeword_index][position])
    return (SEPARATOR * 2) + SEPARATOR.join("".join(codeword) for codeword in codewords)


class Week14FinalQualityTests(unittest.TestCase):
    def test_released_encodings_remain_byte_for_byte_stable(self) -> None:
        encodings = {
            "baseline": encode_secret(SECRET),
            "repetition": encode_secret(SECRET, recovery_mode=True),
            "hamming": encode_secret(SECRET, error_correction="hamming"),
        }
        for mode, encoded in encodings.items():
            with self.subTest(mode=mode):
                digest = hashlib.sha256(encoded.encode("utf-8")).hexdigest()
                self.assertEqual(digest, EXPECTED_HASHES[mode])
                self.assertEqual(extract_secret(encoded), SECRET)

    def test_hamming_corrects_single_errors_in_separate_codewords(self) -> None:
        encoded = encode_secret(SECRET, error_correction="hamming")
        damaged = _damage_codeword(encoded, 0, (0,))
        damaged = _damage_codeword(damaged, 8, (12,))
        self.assertEqual(extract_secret(damaged), SECRET)

    def test_hamming_double_bit_diagnostic_is_stable(self) -> None:
        encoded = encode_secret(SECRET, error_correction="hamming")
        damaged = _damage_codeword(encoded, 8, (0, 1))
        diagnostic = diagnose_stego_text(damaged)
        self.assertFalse(diagnostic["success"])
        self.assertEqual(diagnostic["encoding_mode"], "hamming")
        self.assertEqual(diagnostic["error_category"], "hamming_double_bit_error")

    def test_hamming_deletion_diagnostic_is_stable(self) -> None:
        encoded = encode_secret(SECRET, error_correction="hamming")
        first_data_symbol = next(
            index for index, character in enumerate(encoded) if character in {ZERO, ONE}
        )
        damaged = encoded[:first_data_symbol] + encoded[first_data_symbol + 1 :]
        diagnostic = diagnose_stego_text(damaged)
        self.assertFalse(diagnostic["success"])
        self.assertEqual(diagnostic["encoding_mode"], "hamming")
        self.assertEqual(diagnostic["error_category"], "malformed_hamming_codeword")


if __name__ == "__main__":
    unittest.main()
