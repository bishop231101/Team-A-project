"""A small, deterministic zero-width Unicode steganography codec.

This Week 3 prototype appends an encoded frame to ordinary cover text.  The
invisible frame uses the character mapping selected by Team A and includes a
version marker, payload length, and CRC-32 checksum so damaged text is not
silently treated as a valid secret.
"""

from __future__ import annotations

import struct
import zlib
from collections import Counter


ZERO = "\u200b"  # ZERO WIDTH SPACE
ONE = "\u200c"  # ZERO WIDTH NON-JOINER
SEPARATOR = "\u200d"  # ZERO WIDTH JOINER

_MAGIC = b"ZWS1"
_HEADER_LENGTH = 8  # Four magic bytes followed by a four-byte payload length.
_CHECKSUM_LENGTH = 4
_CODEC_CHARACTERS = frozenset((ZERO, ONE, SEPARATOR))
_DEFAULT_REPETITION_FACTOR = 3
_MIN_REPETITION_FACTOR = 3
_MAX_REPETITION_FACTOR = 15


class DecodeError(ValueError):
    """Raised when an invisible frame is missing, malformed, or damaged."""


class EmbedError(ValueError):
    """Raised when a cover text cannot safely receive another payload."""


def encode_secret(
    secret: str,
    recovery_mode: bool = False,
    repetition_factor: int = _DEFAULT_REPETITION_FACTOR,
) -> str:
    """Encode ``secret`` into an invisible, self-validating frame.

    The frame is UTF-8 payload bytes prefixed with ``ZWS1`` and a big-endian
    payload length, then suffixed with a CRC-32 checksum. The default mode
    encodes each byte as eight zero-width bit characters. ``recovery_mode``
    repeats every bit ``repetition_factor`` times and uses majority voting.
    The factor must be an odd integer from 3 through 15. The default remains
    three for compatibility with Week 5; Week 6 testing uses five copies to
    recover as many as two removed or altered data symbols in each group.
    """
    if not isinstance(secret, str):
        raise TypeError("secret must be a string")
    if not isinstance(recovery_mode, bool):
        raise TypeError("recovery_mode must be a boolean")
    _validate_repetition_factor(repetition_factor)

    payload = secret.encode("utf-8")
    frame = _MAGIC + struct.pack(">I", len(payload)) + payload
    frame += struct.pack(">I", zlib.crc32(frame) & 0xFFFFFFFF)
    if recovery_mode:
        return _encode_with_repetition(frame, repetition_factor)
    return SEPARATOR.join(_encode_byte(value) for value in frame)


def embed_secret(
    cover_text: str,
    secret: str,
    recovery_mode: bool = False,
    repetition_factor: int = _DEFAULT_REPETITION_FACTOR,
) -> str:
    """Append an encoded secret to visible ``cover_text``.

    Removing the codec's three invisible characters from the returned string
    produces exactly the original cover text.
    """
    if not isinstance(cover_text, str):
        raise TypeError("cover_text must be a string")
    if contains_codec_characters(cover_text):
        raise EmbedError(
            "cover text already contains project zero-width characters; "
            "repeated embedding is not supported"
        )
    return cover_text + encode_secret(
        secret,
        recovery_mode=recovery_mode,
        repetition_factor=repetition_factor,
    )


def extract_secret(stego_text: str) -> str:
    """Recover and validate a secret embedded by :func:`embed_secret`.

    Only the project's three configured zero-width characters are interpreted;
    all visible cover text is ignored. A malformed frame raises ``DecodeError``
    instead of returning a potentially corrupted result.
    """
    if not isinstance(stego_text, str):
        raise TypeError("stego_text must be a string")

    encoded = "".join(char for char in stego_text if char in _CODEC_CHARACTERS)
    if not encoded:
        raise DecodeError("no zero-width payload was found")

    repetition_factor = _repetition_factor_from_prefix(encoded)
    if repetition_factor is not None:
        frame = _decode_with_repetition(encoded[repetition_factor:], repetition_factor)
    else:
        frame = _decode_standard(encoded)

    return _decode_frame(frame)


def _decode_standard(encoded: str) -> bytes:
    blocks = encoded.split(SEPARATOR)
    if any(len(block) != 8 for block in blocks):
        raise DecodeError("payload contains an incomplete or malformed byte block")

    try:
        return bytes(_decode_byte(block) for block in blocks)
    except ValueError as error:
        raise DecodeError("payload contains an invalid bit value") from error


def _decode_frame(frame: bytes) -> str:

    minimum_frame_length = _HEADER_LENGTH + _CHECKSUM_LENGTH
    if len(frame) < minimum_frame_length:
        raise DecodeError("payload frame is too short")
    if frame[:4] != _MAGIC:
        raise DecodeError("payload has an unrecognized format marker")

    payload_length = struct.unpack(">I", frame[4:8])[0]
    expected_length = _HEADER_LENGTH + payload_length + _CHECKSUM_LENGTH
    if len(frame) != expected_length:
        raise DecodeError("payload length does not match its frame")

    stored_checksum = struct.unpack(">I", frame[-_CHECKSUM_LENGTH:])[0]
    calculated_checksum = zlib.crc32(frame[:-_CHECKSUM_LENGTH]) & 0xFFFFFFFF
    if stored_checksum != calculated_checksum:
        raise DecodeError("payload checksum does not match")

    try:
        return frame[_HEADER_LENGTH:-_CHECKSUM_LENGTH].decode("utf-8")
    except UnicodeDecodeError as error:
        raise DecodeError("payload is not valid UTF-8") from error


def _validate_repetition_factor(repetition_factor: int) -> None:
    if isinstance(repetition_factor, bool) or not isinstance(repetition_factor, int):
        raise TypeError("repetition_factor must be an integer")
    if not _MIN_REPETITION_FACTOR <= repetition_factor <= _MAX_REPETITION_FACTOR:
        raise ValueError("repetition_factor must be between 3 and 15")
    if repetition_factor % 2 == 0:
        raise ValueError("repetition_factor must be odd")


def _repetition_factor_from_prefix(encoded: str) -> int | None:
    prefix_length = len(encoded) - len(encoded.lstrip(SEPARATOR))
    if prefix_length < _MIN_REPETITION_FACTOR:
        return None
    try:
        _validate_repetition_factor(prefix_length)
    except (TypeError, ValueError) as error:
        raise DecodeError("recovery payload has an invalid repetition prefix") from error
    return prefix_length


def _encode_with_repetition(frame: bytes, repetition_factor: int) -> str:
    repeated_bits = []
    for value in frame:
        for bit in f"{value:08b}":
            symbol = ONE if bit == "1" else ZERO
            repeated_bits.append(symbol * repetition_factor)
    return (SEPARATOR * repetition_factor) + SEPARATOR.join(repeated_bits)


def _decode_with_repetition(encoded: str, repetition_factor: int) -> bytes:
    groups = encoded.split(SEPARATOR)
    minimum_group_length = (repetition_factor // 2) + 1
    if not groups or any(
        not minimum_group_length <= len(group) <= repetition_factor for group in groups
    ):
        raise DecodeError("recovery payload contains a missing or malformed bit group")

    bits = []
    for group in groups:
        zero_count = group.count(ZERO)
        one_count = group.count(ONE)
        if zero_count == one_count:
            raise DecodeError("recovery payload has no majority bit value")
        bits.append("0" if zero_count > one_count else "1")

    if len(bits) % 8 != 0:
        raise DecodeError("recovery payload does not contain complete bytes")
    return bytes(int("".join(bits[index : index + 8]), 2) for index in range(0, len(bits), 8))


def contains_codec_characters(text: str) -> bool:
    """Return whether ``text`` contains one of this project's codec symbols."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return any(character in _CODEC_CHARACTERS for character in text)


def count_codec_characters(text: str) -> dict[str, int]:
    """Count codec symbols for repeatable platform-survival measurements.

    The returned mapping uses Unicode code-point labels so a test runner can
    record sent and recovered symbol totals without depending on invisible text
    rendering in a terminal or platform UI.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    counts = Counter(character for character in text if character in _CODEC_CHARACTERS)
    return {
        "U+200B": counts[ZERO],
        "U+200C": counts[ONE],
        "U+200D": counts[SEPARATOR],
        "total": sum(counts.values()),
    }


def _encode_byte(value: int) -> str:
    return "".join(ONE if bit == "1" else ZERO for bit in f"{value:08b}")


def _decode_byte(block: str) -> int:
    bits = "".join("0" if char == ZERO else "1" if char == ONE else "?" for char in block)
    if "?" in bits:
        raise ValueError("unknown bit character")
    return int(bits, 2)
