"""Run Henry Smith's local Week 8 midterm prototype demonstration."""

from pathlib import Path
import sys
from time import perf_counter


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from src.zero_width_codec import (
    DecodeError,
    ONE,
    SEPARATOR,
    ZERO,
    count_codec_characters,
    embed_secret,
    encode_secret,
    extract_secret,
)


COVER = "Team A midterm prototype demonstration."
SECRET = "CS481-MIDTERM"
REPETITION_FACTOR = 5


def alter_distributed_data_symbols(encoded: str, percentage: int) -> str:
    """Alter a percentage of data symbols, spreading changes among groups."""
    groups = [list(group) for group in encoded[REPETITION_FACTOR:].split(SEPARATOR)]
    target = round(sum(len(group) for group in groups) * percentage / 100)
    changed = 0
    pass_number = 0

    while changed < target:
        for group in groups:
            if changed >= target:
                break
            position = len(group) - 1 - pass_number
            group[position] = ONE if group[position] == ZERO else ZERO
            changed += 1
        pass_number += 1

    return (SEPARATOR * REPETITION_FACTOR) + SEPARATOR.join(
        "".join(group) for group in groups
    )


def visible_text(stego_text: str) -> str:
    return "".join(
        character
        for character in stego_text
        if character not in {ZERO, ONE, SEPARATOR}
    )


def main() -> None:
    started = perf_counter()
    standard = embed_secret(COVER, SECRET)
    protected = encode_secret(
        SECRET,
        recovery_mode=True,
        repetition_factor=REPETITION_FACTOR,
    )
    damaged_40 = alter_distributed_data_symbols(protected, 40)
    damaged_45 = alter_distributed_data_symbols(protected, 45)

    standard_round_trip = extract_secret(standard) == SECRET
    cover_unchanged = visible_text(standard) == COVER
    protected_round_trip = extract_secret(protected) == SECRET
    recovered_40 = extract_secret(damaged_40) == SECRET

    rejected_45 = False
    rejection_message = ""
    try:
        extract_secret(damaged_45)
    except DecodeError as error:
        rejected_45 = True
        rejection_message = str(error)

    checks = (
        standard_round_trip,
        cover_unchanged,
        protected_round_trip,
        recovered_40,
        rejected_45,
    )
    elapsed = perf_counter() - started

    print("TEAM A - WEEK 8 MIDTERM PROTOTYPE DEMONSTRATION")
    print("=" * 62)
    print(f"Visible cover: {COVER}")
    print(f"Synthetic secret: {SECRET}")
    print(f"Standard codec characters: {count_codec_characters(standard)['total']}")
    print(f"Five-copy codec characters: {count_codec_characters(protected)['total']}")
    print(f"1. Standard encode/decode: {'PASS' if standard_round_trip else 'FAIL'}")
    print(f"2. Visible cover unchanged: {'PASS' if cover_unchanged else 'FAIL'}")
    print(f"3. Five-copy encode/decode: {'PASS' if protected_round_trip else 'FAIL'}")
    print(f"4. Recovery after 40% alteration: {'PASS' if recovered_40 else 'FAIL'}")
    print(f"5. Safe rejection after 45% alteration: {'PASS' if rejected_45 else 'FAIL'}")
    print(f"   Decoder response: {rejection_message or 'No rejection'}")
    print(f"All demonstration checks passed: {all(checks)}")
    print(f"Local execution time: {elapsed:.3f} seconds")


if __name__ == "__main__":
    main()
