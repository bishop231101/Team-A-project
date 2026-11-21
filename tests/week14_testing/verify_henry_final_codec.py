"""Run Henry's final Week 14 codec verification."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.zero_width_codec import (
    ONE,
    SEPARATOR,
    ZERO,
    diagnose_stego_text,
    encode_secret,
    extract_secret,
)


def _flip(symbol: str) -> str:
    return ONE if symbol == ZERO else ZERO


def _damage_codeword(encoded: str, positions: tuple[int, ...]) -> str:
    codewords = [list(codeword) for codeword in encoded[2:].split(SEPARATOR)]
    for position in positions:
        codewords[8][position] = _flip(codewords[8][position])
    return (SEPARATOR * 2) + SEPARATOR.join("".join(codeword) for codeword in codewords)


def main() -> None:
    secret = "Week 14 final verification: Café 世界 🔐"
    baseline = encode_secret(secret)
    repetition = encode_secret(secret, recovery_mode=True)
    hamming = encode_secret(secret, error_correction="hamming")

    checks = [
        ("Baseline backward-compatible round trip", extract_secret(baseline) == secret),
        ("Repetition backward-compatible round trip", extract_secret(repetition) == secret),
        ("Hamming Unicode round trip", extract_secret(hamming) == secret),
        (
            "Hamming single-bit correction",
            extract_secret(_damage_codeword(hamming, (0,))) == secret,
        ),
        (
            "Hamming double-bit detection",
            diagnose_stego_text(_damage_codeword(hamming, (0, 1)))["error_category"]
            == "hamming_double_bit_error",
        ),
    ]

    print("HENRY SMITH - WEEK 14 FINAL CODEC VERIFICATION")
    for description, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'}  {description}")
    print(f"All final codec checks passed: {all(passed for _, passed in checks)}")
    print("Limitation: Hamming corrects substitutions, not deleted or stripped symbols.")

    if not all(passed for _, passed in checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
