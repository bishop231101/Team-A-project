"""Produce reproducible Week 12 Hamming stability and overhead results."""

from __future__ import annotations

import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.zero_width_codec import (
    DecodeError,
    ONE,
    SEPARATOR,
    ZERO,
    count_codec_characters,
    encode_secret,
    extract_secret,
)


CORPUS_PATH = ROOT / "tests" / "fixtures" / "week9_corpus.json"


def _flip(symbol: str) -> str:
    return ONE if symbol == ZERO else ZERO


def _damage_hamming(encoded: str, codeword_index: int, positions: tuple[int, ...]) -> str:
    codewords = [list(codeword) for codeword in encoded[2:].split(SEPARATOR)]
    for position in positions:
        codewords[codeword_index][position] = _flip(codewords[codeword_index][position])
    return (SEPARATOR * 2) + SEPARATOR.join("".join(codeword) for codeword in codewords)


def _rejected(encoded: str) -> bool:
    try:
        extract_secret(encoded)
    except DecodeError:
        return True
    return False


def main() -> None:
    corpus = json.loads(CORPUS_PATH.read_text(encoding="utf-8"))
    print("HENRY SMITH - WEEK 12 HAMMING STABILITY AND OVERHEAD")
    print("ID    Standard  Hamming  Overhead  Round trip  Single bit")
    print("----  --------  -------  --------  ----------  ----------")

    all_passed = True
    for entry in corpus:
        secret = entry["text"]
        standard = encode_secret(secret)
        protected = encode_secret(secret, error_correction="hamming")
        standard_count = count_codec_characters(standard)["total"]
        protected_count = count_codec_characters(protected)["total"]
        overhead = ((protected_count / standard_count) - 1) * 100
        round_trip = extract_secret(protected) == secret
        corrected = extract_secret(_damage_hamming(protected, 8, (0,))) == secret
        all_passed &= round_trip and corrected
        print(
            f"{entry['id']:<4}  {standard_count:>8}  {protected_count:>7}  "
            f"{overhead:>7.2f}%  {'PASS' if round_trip else 'FAIL':>10}  "
            f"{'PASS' if corrected else 'FAIL':>10}"
        )

    representative = encode_secret(
        "Week 12 controlled corruption",
        error_correction="hamming",
    )
    double_bit_rejected = _rejected(_damage_hamming(representative, 8, (0, 1)))
    deleted_symbol = representative[:16] + representative[17:]
    deletion_rejected = _rejected(deleted_symbol)
    all_passed &= double_bit_rejected and deletion_rejected

    print()
    print(f"Double-bit corruption safely rejected: {double_bit_rejected}")
    print(f"Deleted-symbol corruption safely rejected: {deletion_rejected}")
    print(f"All Week 12 Henry stability checks passed: {all_passed}")
    print("Limitation: Hamming corrects substitutions, not deleted or stripped symbols.")

    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
