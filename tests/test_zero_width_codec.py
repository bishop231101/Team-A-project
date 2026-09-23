"""Local Week 3 tests for the zero-width Unicode codec."""

import json
from pathlib import Path
import tempfile
import unittest

from src.zero_width_codec import (
    DecodeError,
    EmbedError,
    ONE,
    SEPARATOR,
    ZERO,
    contains_codec_characters,
    count_codec_characters,
    embed_secret,
    encode_secret,
    extract_secret,
)


class ZeroWidthCodecTests(unittest.TestCase):
    def test_round_trip_for_reusable_test_vectors(self) -> None:
        fixture = Path(__file__).parent / "fixtures" / "codec_test_vectors.json"
        test_vectors = json.loads(fixture.read_text(encoding="utf-8"))
        for vector in test_vectors:
            with self.subTest(name=vector["name"]):
                stego = embed_secret(vector["cover_text"], vector["secret"])
                self.assertEqual(extract_secret(stego), vector["secret"])

    def test_cover_text_remains_visibly_unchanged(self) -> None:
        cover = "A visible message with punctuation!"
        stego = embed_secret(cover, "hidden")
        visible_text = "".join(char for char in stego if char not in {ZERO, ONE, SEPARATOR})
        self.assertEqual(visible_text, cover)

    def test_encoding_is_deterministic(self) -> None:
        self.assertEqual(encode_secret("same secret"), encode_secret("same secret"))

    def test_missing_payload_is_rejected(self) -> None:
        with self.assertRaisesRegex(DecodeError, "no zero-width payload"):
            extract_secret("An ordinary message")

    def test_truncated_payload_is_rejected(self) -> None:
        encoded = encode_secret("damage check")
        with self.assertRaises(DecodeError):
            extract_secret(encoded[:-1])

    def test_invalid_argument_types_are_rejected(self) -> None:
        with self.assertRaises(TypeError):
            encode_secret(123)  # type: ignore[arg-type]
        with self.assertRaises(TypeError):
            embed_secret(None, "secret")  # type: ignore[arg-type]
        with self.assertRaises(TypeError):
            extract_secret(None)  # type: ignore[arg-type]

    def test_empty_cover_and_payload_round_trip(self) -> None:
        self.assertEqual(extract_secret(embed_secret("", "")), "")

    def test_round_trip_preserves_punctuation_and_line_breaks(self) -> None:
        cover = "Line one.\nLine two?\n"
        secret = "Punctuation: !@#$%^&*()\nsecond line"
        self.assertEqual(extract_secret(embed_secret(cover, secret)), secret)

    def test_repeated_embedding_is_rejected_clearly(self) -> None:
        first_embedding = embed_secret("Cover", "first secret")
        with self.assertRaisesRegex(EmbedError, "repeated embedding"):
            embed_secret(first_embedding, "second secret")

    def test_malformed_byte_block_is_rejected(self) -> None:
        malformed = ZERO * 7
        with self.assertRaisesRegex(DecodeError, "incomplete or malformed"):
            extract_secret(malformed)

    def test_unrelated_zero_width_character_is_not_treated_as_payload(self) -> None:
        word_joiner = "\u2060"
        with self.assertRaisesRegex(DecodeError, "no zero-width payload"):
            extract_secret(f"Visible{word_joiner} cover")

    def test_utf8_file_round_trip(self) -> None:
        stego = embed_secret("File cover", "Café 世界 🔐")
        with tempfile.TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "stego.txt"
            path.write_text(stego, encoding="utf-8")
            recovered_text = path.read_text(encoding="utf-8")
        self.assertEqual(extract_secret(recovered_text), "Café 世界 🔐")

    def test_one_hundred_generated_round_trips(self) -> None:
        for number in range(100):
            secret = f"Generated message {number}: Café 世界 🔐"
            with self.subTest(number=number):
                self.assertEqual(extract_secret(embed_secret("Cover", secret)), secret)

    def test_codec_character_counts_support_platform_measurements(self) -> None:
        encoded = encode_secret("measure me")
        counts = count_codec_characters(encoded)
        self.assertEqual(counts["total"], len(encoded))
        self.assertGreater(counts["U+200B"], 0)
        self.assertGreater(counts["U+200C"], 0)
        self.assertGreater(counts["U+200D"], 0)
        self.assertTrue(contains_codec_characters(encoded))
        self.assertFalse(contains_codec_characters("Ordinary cover text"))

    def test_recovery_mode_round_trip(self) -> None:
        stego = embed_secret("Cover", "recoverable secret", recovery_mode=True)
        self.assertEqual(extract_secret(stego), "recoverable secret")

    def test_recovery_mode_recovers_one_removed_data_symbol(self) -> None:
        encoded = encode_secret("recover one deletion", recovery_mode=True)
        first_data_symbol = next(index for index, character in enumerate(encoded) if character in {ZERO, ONE})
        damaged = encoded[:first_data_symbol] + encoded[first_data_symbol + 1 :]
        self.assertEqual(extract_secret(damaged), "recover one deletion")

    def test_recovery_mode_recovers_one_altered_data_symbol(self) -> None:
        encoded = encode_secret("recover one alteration", recovery_mode=True)
        first_data_symbol = next(index for index, character in enumerate(encoded) if character in {ZERO, ONE})
        replacement = ONE if encoded[first_data_symbol] == ZERO else ZERO
        damaged = encoded[:first_data_symbol] + replacement + encoded[first_data_symbol + 1 :]
        self.assertEqual(extract_secret(damaged), "recover one alteration")

    def test_recovery_mode_detects_removed_separator(self) -> None:
        encoded = encode_secret("separator damage", recovery_mode=True)
        separator_index = encoded.find(SEPARATOR, 3)
        damaged = encoded[:separator_index] + encoded[separator_index + 1 :]
        with self.assertRaisesRegex(DecodeError, "recovery payload"):
            extract_secret(damaged)

    def test_recovery_mode_requires_boolean_flag(self) -> None:
        with self.assertRaises(TypeError):
            encode_secret("secret", recovery_mode=3)  # type: ignore[arg-type]

    def test_five_copy_recovery_mode_round_trip(self) -> None:
        stego = embed_secret(
            "Cover",
            "Week 6 stronger recovery",
            recovery_mode=True,
            repetition_factor=5,
        )
        self.assertEqual(extract_secret(stego), "Week 6 stronger recovery")

    def test_five_copy_mode_recovers_two_removed_symbols_per_group(self) -> None:
        encoded = encode_secret("two deletions", recovery_mode=True, repetition_factor=5)
        groups = encoded[5:].split(SEPARATOR)
        groups[0] = groups[0][2:]
        damaged = (SEPARATOR * 5) + SEPARATOR.join(groups)
        self.assertEqual(extract_secret(damaged), "two deletions")

    def test_five_copy_mode_recovers_two_altered_symbols_per_group(self) -> None:
        encoded = encode_secret("two alterations", recovery_mode=True, repetition_factor=5)
        groups = encoded[5:].split(SEPARATOR)
        replacement = ONE if groups[0][0] == ZERO else ZERO
        groups[0] = replacement * 2 + groups[0][2:]
        damaged = (SEPARATOR * 5) + SEPARATOR.join(groups)
        self.assertEqual(extract_secret(damaged), "two alterations")

    def test_five_copy_mode_recovers_planned_corruption_percentages(self) -> None:
        secret = "Week 6 percentage recovery test"
        for corruption_type in ("removal", "alteration"):
            for percentage in (10, 20, 30):
                with self.subTest(corruption_type=corruption_type, percentage=percentage):
                    encoded = encode_secret(secret, recovery_mode=True, repetition_factor=5)
                    damaged = self._damage_recovery_groups(encoded, percentage, corruption_type)
                    self.assertEqual(extract_secret(damaged), secret)

    def test_five_copy_mode_recovers_mixed_thirty_percent_corruption(self) -> None:
        secret = "Week 6 mixed corruption"
        encoded = encode_secret(secret, recovery_mode=True, repetition_factor=5)
        damaged = self._damage_recovery_groups(encoded, 30, "mixed")
        self.assertEqual(extract_secret(damaged), secret)

    def test_repetition_factor_validation(self) -> None:
        for invalid_factor in (1, 2, 4, 16):
            with self.subTest(invalid_factor=invalid_factor):
                with self.assertRaises(ValueError):
                    encode_secret("secret", recovery_mode=True, repetition_factor=invalid_factor)
        with self.assertRaises(TypeError):
            encode_secret("secret", recovery_mode=True, repetition_factor=3.0)  # type: ignore[arg-type]

    @staticmethod
    def _damage_recovery_groups(encoded: str, percentage: int, corruption_type: str) -> str:
        repetition_factor = 5
        groups = [list(group) for group in encoded[repetition_factor:].split(SEPARATOR)]
        target = round(sum(len(group) for group in groups) * percentage / 100)
        damaged = 0
        pass_number = 0
        while damaged < target:
            for group_index, group in enumerate(groups):
                if damaged >= target:
                    break
                if pass_number >= 2:
                    raise AssertionError("test corruption exceeds the five-copy correction limit")
                if corruption_type == "removal" or (
                corruption_type == "mixed" and (group_index + pass_number) % 2 == 0
            ):
                    group.pop(0)
                else:
                    position = len(group) - 1 - pass_number
                    group[position] = ONE if group[position] == ZERO else ZERO
                damaged += 1
            pass_number += 1
        return (SEPARATOR * repetition_factor) + SEPARATOR.join("".join(group) for group in groups)
