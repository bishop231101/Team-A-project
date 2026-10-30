"""Demonstrate correctable and uncorrectable Week 11 Hamming cases."""

from pathlib import Path
import sys


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from src.zero_width_codec import (
    DecodeError,
    ONE,
    SEPARATOR,
    ZERO,
    count_codec_characters,
    encode_secret,
    extract_secret,
)


def flip(symbol: str) -> str:
    return ONE if symbol == ZERO else ZERO


def main() -> None:
    secret = "Week 11: Café 世界 🔐"
    standard = encode_secret(secret)
    protected = encode_secret(secret, error_correction="hamming")

    codewords = [list(codeword) for codeword in protected[2:].split(SEPARATOR)]
    codewords[0][0] = flip(codewords[0][0])
    single_error = (SEPARATOR * 2) + SEPARATOR.join(
        "".join(codeword) for codeword in codewords
    )

    codewords = [list(codeword) for codeword in protected[2:].split(SEPARATOR)]
    codewords[0][0] = flip(codewords[0][0])
    codewords[0][1] = flip(codewords[0][1])
    double_error = (SEPARATOR * 2) + SEPARATOR.join(
        "".join(codeword) for codeword in codewords
    )

    checks = []
    checks.append(("Unicode round trip", extract_secret(protected) == secret))
    checks.append(("Single-bit correction", extract_secret(single_error) == secret))
    try:
        extract_secret(double_error)
    except DecodeError as error:
        checks.append(("Double-bit safe rejection", "double-bit" in str(error)))
    else:
        checks.append(("Double-bit safe rejection", False))

    gmail_pattern = protected.replace(ZERO, "")
    try:
        extract_secret(gmail_pattern)
    except DecodeError:
        checks.append(("Gmail-style stripping safely rejected", True))
    else:
        checks.append(("Gmail-style stripping safely rejected", False))

    try:
        extract_secret("Visible cover")
    except DecodeError:
        checks.append(("Word-style complete stripping safely rejected", True))
    else:
        checks.append(("Word-style complete stripping safely rejected", False))

    print("HENRY SMITH - WEEK 11 HAMMING SECDED VERIFICATION")
    print("Secret type: multilingual Unicode text with emoji")
    print(f"Standard codec characters: {count_codec_characters(standard)['total']}")
    print(f"Hamming codec characters:  {count_codec_characters(protected)['total']}")
    for description, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'}  {description}")
    print(f"All Week 11 Hamming checks passed: {all(value for _, value in checks)}")
    print("Limitation: Hamming mode does not recover deleted or completely stripped payloads")
    if not all(value for _, value in checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
