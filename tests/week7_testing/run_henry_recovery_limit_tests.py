"""Measure Henry Smith's Week 7 five-copy recovery boundary.

Run from the repository root:
    python tests/week7_testing/run_henry_recovery_limit_tests.py
"""

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


REPETITION_FACTOR = 5
SECRET = "Week 7 recovery limit test"


def damage_groups(
    encoded: str,
    percentage: int,
    corruption_type: str,
) -> tuple[str, int, int, int]:
    """Distribute data-symbol damage across five-copy groups."""
    groups = [list(group) for group in encoded[REPETITION_FACTOR:].split(SEPARATOR)]
    data_symbol_count = sum(len(group) for group in groups)
    target_changes = round(data_symbol_count * percentage / 100)
    removals = [0] * len(groups)
    alterations = [0] * len(groups)
    changes_made = 0
    pass_number = 0

    while changes_made < target_changes:
        for group_index, group in enumerate(groups):
            if changes_made >= target_changes:
                break
            if pass_number >= REPETITION_FACTOR:
                raise ValueError("requested corruption exceeds the available data symbols")

            remove_symbol = corruption_type == "removal" or (
                corruption_type == "mixed" and (group_index + pass_number) % 2 == 0
            )
            if remove_symbol:
                group.pop(0)
                removals[group_index] += 1
            else:
                position = len(group) - 1 - alterations[group_index]
                group[position] = ONE if group[position] == ZERO else ZERO
                alterations[group_index] += 1
            changes_made += 1
        pass_number += 1

    damaged = (SEPARATOR * REPETITION_FACTOR) + SEPARATOR.join(
        "".join(group) for group in groups
    )
    return damaged, sum(removals), sum(alterations), data_symbol_count


def evaluate(corruption_type: str, percentage: int) -> tuple[str, float]:
    encoded = encode_secret(
        SECRET,
        recovery_mode=True,
        repetition_factor=REPETITION_FACTOR,
    )
    damaged, _, _, _ = damage_groups(encoded, percentage, corruption_type)
    original_total = count_codec_characters(encoded)["total"]
    damaged_total = count_codec_characters(damaged)["total"]
    survival_rate = damaged_total / original_total * 100

    try:
        recovered = extract_secret(damaged)
        outcome = "RECOVERED" if recovered == SECRET else "INCORRECT"
    except DecodeError:
        outcome = "REJECTED"
    return outcome, survival_rate


def main() -> None:
    percentages = (35, 40, 45, 50)
    corruption_types = ("removal", "alteration", "mixed")
    all_expected = True

    print("Henry Smith - Week 7 five-copy recovery limit analysis")
    print("Scenario     Damage  Survival  Expected   Actual     Status")
    print("------------ ------  --------  ---------  ---------  ------")
    for corruption_type in corruption_types:
        for percentage in percentages:
            actual, survival_rate = evaluate(corruption_type, percentage)
            expected = "RECOVERED" if percentage <= 40 else "REJECTED"
            status = "PASS" if actual == expected else "FAIL"
            all_expected = all_expected and status == "PASS"
            print(
                f"{corruption_type:<12} {percentage:>3}%    "
                f"{survival_rate:>6.2f}%  {expected:<9}  {actual:<9}  {status}"
            )

    print(f"All Week 7 boundary expectations passed: {all_expected}")
    print("Observed recovery limit under distributed data-symbol damage: 40%")


if __name__ == "__main__":
    main()
