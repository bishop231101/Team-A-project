"""Local Week 3 tests for the zero-width Unicode codec."""

import json
from pathlib import Path
import tempfile
import unittest

from code.zero_width_codec import (
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
