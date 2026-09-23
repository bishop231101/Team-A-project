"""Run Henry Smith's controlled Week 6 recovery scenarios.

Run from the repository root:
    python tests/week6_testing/run_henry_recovery_demo.py
"""

from pathlib import Path
import sys


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from src.zero_width_codec import ONE, SEPARATOR, ZERO, encode_secret, extract_secret


REPETITION_FACTOR = 5
SECRET = "Week 6 percentage recovery test"


def damage_groups(encoded: str, percentage: int, corruption_type: str) -> str:
    """Damage data symbols while preserving the structural separators."""
    groups = [list(group) for group in encoded[REPETITION_FACTOR:].split(SEPARATOR)]
    target = round(sum(len(group) for group in groups) * percentage / 100)
    damaged = 0
    pass_number = 0

    while damaged < target:
        for group_index, group in enumerate(groups):
            if damaged >= target:
                break
            if pass_number >= REPETITION_FACTOR // 2:
                raise ValueError("requested corruption exceeds the correction limit")

            remove_symbol = corruption_type == "removal" or (
                corruption_type == "mixed" and (group_index + pass_number) % 2 == 0
            )
            if remove_symbol:
                group.pop(0)
            else:
                position = len(group) - 1 - pass_number
                group[position] = ONE if group[position] == ZERO else ZERO
            damaged += 1
        pass_number += 1

    return (SEPARATOR * REPETITION_FACTOR) + SEPARATOR.join(
        "".join(group) for group in groups
    )


def main() -> None:
    scenarios = [
        ("removal", 10),
        ("removal", 20),
        ("removal", 30),
        ("alteration", 10),
        ("alteration", 20),
        ("alteration", 30),
        ("mixed", 30),
    ]
    encoded = encode_secret(SECRET, recovery_mode=True, repetition_factor=REPETITION_FACTOR)

    print("Henry Smith - Week 6 five-copy recovery evaluation")
    print(f"Original secret: {SECRET}")
    print("Scenario     Percent  Decode result")
    print("------------ -------  -------------")
    all_passed = True
    for corruption_type, percentage in scenarios:
        damaged = damage_groups(encoded, percentage, corruption_type)
        recovered = extract_secret(damaged)
        passed = recovered == SECRET
        all_passed = all_passed and passed
        print(f"{corruption_type:<12} {percentage:>3}%     {'PASS' if passed else 'FAIL'}")

    print(f"All Week 6 recovery scenarios passed: {all_passed}")


if __name__ == "__main__":
    main()
