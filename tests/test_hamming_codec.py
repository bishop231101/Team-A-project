"""Week 11 tests for the optional Hamming SECDED codec mode."""

import unittest

from src.zero_width_codec import (
    DecodeError,
    ONE,
    SEPARATOR,
    ZERO,
    embed_secret,
    encode_secret,
    extract_secret,
)


def flip_symbol(symbol: str) -> str:
    return ONE if symbol == ZERO else ZERO


def damage_codeword(encoded: str, codeword_index: int, positions: tuple[int, ...]) -> str:
    prefix = SEPARATOR * 2
    codewords = [list(codeword) for codeword in encoded[2:].split(SEPARATOR)]
    for position in positions:
        codewords[codeword_index][position] = flip_symbol(codewords[codeword_index][position])
    return prefix + SEPARATOR.join("".join(codeword) for codeword in codewords)


class HammingCodecTests(unittest.TestCase):
    def test_hamming_round_trip_for_ascii_unicode_and_empty_payloads(self) -> None:
        for secret in ("", "Hello", "Café 世界 🔐"):
            with self.subTest(secret=secret):
                stego = embed_secret("Visible cover", secret, error_correction="hamming")
                self.assertEqual(extract_secret(stego), secret)

    def test_hamming_encoding_is_deterministic(self) -> None:
        first = encode_secret("deterministic", error_correction="hamming")
        second = encode_secret("deterministic", error_correction="hamming")
        self.assertEqual(first, second)

    def test_hamming_mode_preserves_visible_cover(self) -> None:
        cover = "This visible message remains unchanged."
        stego = embed_secret(cover, "hidden", error_correction="hamming")
        visible = "".join(
            character for character in stego if character not in {ZERO, ONE, SEPARATOR}
        )
        self.assertEqual(visible, cover)

    def test_every_single_bit_position_is_corrected(self) -> None:
        encoded = encode_secret("single-bit correction", error_correction="hamming")
        for position in range(13):
            with self.subTest(position=position):
                damaged = damage_codeword(encoded, 0, (position,))
                self.assertEqual(extract_secret(damaged), "single-bit correction")

    def test_one_altered_bit_in_every_codeword_is_corrected(self) -> None:
        secret = "correct every protected byte"
        encoded = encode_secret(secret, error_correction="hamming")
        codeword_count = len(encoded[2:].split(SEPARATOR))
        damaged = encoded
        for codeword_index in range(codeword_count):
            damaged = damage_codeword(damaged, codeword_index, (codeword_index % 13,))
        self.assertEqual(extract_secret(damaged), secret)

    def test_two_altered_bits_in_one_codeword_are_rejected(self) -> None:
        encoded = encode_secret("double-bit rejection", error_correction="hamming")
        damaged = damage_codeword(encoded, 0, (0, 1))
        with self.assertRaisesRegex(DecodeError, "double-bit"):
            extract_secret(damaged)

    def test_three_altered_bits_do_not_return_false_success(self) -> None:
        encoded = encode_secret("false-success prevention", error_correction="hamming")
        damaged = damage_codeword(encoded, 0, (0, 1, 2))
        with self.assertRaises(DecodeError):
            extract_secret(damaged)

    def test_deleted_symbol_is_rejected(self) -> None:
        encoded = encode_secret("deletion", error_correction="hamming")
        first_data_symbol = next(
            index for index, character in enumerate(encoded) if character in {ZERO, ONE}
        )
        damaged = encoded[:first_data_symbol] + encoded[first_data_symbol + 1 :]
        with self.assertRaisesRegex(DecodeError, "Hamming payload"):
            extract_secret(damaged)

    def test_gmail_style_zero_symbol_removal_is_rejected(self) -> None:
        encoded = encode_secret("Hello", error_correction="hamming")
        damaged = encoded.replace(ZERO, "")
        with self.assertRaises(DecodeError):
            extract_secret(damaged)

    def test_complete_payload_removal_is_rejected(self) -> None:
        stego = embed_secret("Visible cover", "Hello", error_correction="hamming")
        stripped = "".join(
            character for character in stego if character not in {ZERO, ONE, SEPARATOR}
        )
        with self.assertRaisesRegex(DecodeError, "no zero-width payload"):
            extract_secret(stripped)

    def test_mode_validation_and_mutual_exclusion(self) -> None:
        with self.assertRaisesRegex(ValueError, "error_correction"):
            encode_secret("secret", error_correction="reed-solomon")
        with self.assertRaisesRegex(TypeError, "error_correction"):
            encode_secret("secret", error_correction=True)  # type: ignore[arg-type]
        with self.assertRaisesRegex(ValueError, "cannot be combined"):
            encode_secret(
                "secret",
                recovery_mode=True,
                error_correction="hamming",
            )


if __name__ == "__main__":
    unittest.main()
