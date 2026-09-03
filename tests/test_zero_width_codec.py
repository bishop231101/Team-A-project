"""Local Week 3 tests for the zero-width Unicode codec."""

import json
from pathlib import Path
import unittest

from code.zero_width_codec import (
    DecodeError,
    ONE,
    SEPARATOR,
    ZERO,
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
