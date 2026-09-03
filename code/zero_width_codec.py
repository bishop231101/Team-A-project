"""A small, deterministic zero-width Unicode steganography codec.

This Week 3 prototype appends an encoded frame to ordinary cover text.  The
invisible frame uses the character mapping selected by Team A and includes a
version marker, payload length, and CRC-32 checksum so damaged text is not
silently treated as a valid secret.
"""

from __future__ import annotations

import struct
import zlib


ZERO = "\u200b"  # ZERO WIDTH SPACE
ONE = "\u200c"  # ZERO WIDTH NON-JOINER
SEPARATOR = "\u200d"  # ZERO WIDTH JOINER

_MAGIC = b"ZWS1"
_HEADER_LENGTH = 8  # Four magic bytes followed by a four-byte payload length.
_CHECKSUM_LENGTH = 4
_CODEC_CHARACTERS = frozenset((ZERO, ONE, SEPARATOR))


class DecodeError(ValueError):
    """Raised when an invisible frame is missing, malformed, or damaged."""


def encode_secret(secret: str) -> str:
    """Encode ``secret`` into an invisible, self-validating frame.

    The frame is UTF-8 payload bytes prefixed with ``ZWS1`` and a big-endian
    payload length, then suffixed with a CRC-32 checksum. Each source byte is
    represented by eight zero-width bit characters; byte blocks are separated
    by ``SEPARATOR``.
    """
    if not isinstance(secret, str):
        raise TypeError("secret must be a string")

    payload = secret.encode("utf-8")
    frame = _MAGIC + struct.pack(">I", len(payload)) + payload
    frame += struct.pack(">I", zlib.crc32(frame) & 0xFFFFFFFF)
    return SEPARATOR.join(_encode_byte(value) for value in frame)


def embed_secret(cover_text: str, secret: str) -> str:
    """Append an encoded secret to visible ``cover_text``.

    Removing the codec's three invisible characters from the returned string
    produces exactly the original cover text.
    """
    if not isinstance(cover_text, str):
        raise TypeError("cover_text must be a string")
    return cover_text + encode_secret(secret)


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

    blocks = encoded.split(SEPARATOR)
    if any(len(block) != 8 for block in blocks):
        raise DecodeError("payload contains an incomplete or malformed byte block")

    try:
        frame = bytes(_decode_byte(block) for block in blocks)
    except ValueError as error:
        raise DecodeError("payload contains an invalid bit value") from error

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


def _encode_byte(value: int) -> str:
    return "".join(ONE if bit == "1" else ZERO for bit in f"{value:08b}")


def _decode_byte(block: str) -> int:
    bits = "".join("0" if char == ZERO else "1" if char == ONE else "?" for char in block)
    if "?" in bits:
        raise ValueError("unknown bit character")
    return int(bits, 2)
