"""Run Tristan Koch's detailed Week 6 five-copy recovery tests.

Run from the repository root:
    python tests/week6_testing/run_tristan_recovery_tests.py
"""

import sys
from pathlib import Path


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


def damage_groups(encoded, percentage, corruption_type):
    """Damage data symbols while preserving five-copy group separators.

    This follows the controlled approach used in Henry's Week 6 demo: each
    data group receives at most two changes, leaving a majority of its five
    symbols available for the codec's recovery decoder.
    """
    groups = [list(group) for group in encoded[REPETITION_FACTOR:].split(SEPARATOR)]
    data_symbol_count = sum(len(group) for group in groups)
    target_changes = round(data_symbol_count * percentage / 100)
    removed_count = 0
    altered_count = 0
    changes_made = 0
    pass_number = 0

    while changes_made < target_changes:
        for group_index, group in enumerate(groups):
            if changes_made >= target_changes:
                break
            if pass_number >= REPETITION_FACTOR // 2:
                raise ValueError("Requested corruption exceeds the correction limit.")

            remove_symbol = corruption_type == "removal" or (
                corruption_type == "mixed" and (group_index + pass_number) % 2 == 0
            )
            if remove_symbol:
                group.pop(0)
                removed_count += 1
            else:
                position = len(group) - 1 - pass_number
                group[position] = ONE if group[position] == ZERO else ZERO
                altered_count += 1
            changes_made += 1
        pass_number += 1

    damaged = (SEPARATOR * REPETITION_FACTOR) + SEPARATOR.join(
        "".join(group) for group in groups
    )
    return damaged, removed_count, altered_count, data_symbol_count


def run_test(test_number, corruption_type, percentage, secret_message):
    """Encode, corrupt, recover, and print evidence for one test scenario."""
    encoded = encode_secret(
        secret_message,
        recovery_mode=True,
        repetition_factor=REPETITION_FACTOR,
    )
    original_count = count_codec_characters(encoded)["total"]
    damaged, removed_count, altered_count, data_symbol_count = damage_groups(
        encoded, percentage, corruption_type
    )
    remaining_count = count_codec_characters(damaged)["total"]
    survival_rate = remaining_count / original_count * 100
    actual_data_corruption = (removed_count + altered_count) / data_symbol_count * 100

    recovered = None
    decoding_error = None
    try:
        recovered = extract_secret(damaged)
        decode_result = "Decoded without an exception"
    except DecodeError as error:
        decode_result = "Decoding failed"
        decoding_error = str(error)

    if corruption_type == "mixed":
        method = "Mixed removal and alteration"
    else:
        method = corruption_type.title()

    print("=" * 78)
    print(f"WEEK 6 RECOVERY TEST {test_number} OF 6")
    print("=" * 78)
    print(f"Original hidden message: {secret_message}")
    print(f"Corruption method: {method}")
    print(
        "Target corruption percentage: "
        f"Approximately {percentage}% of recoverable data symbols"
    )
    print(f"Actual data-symbol corruption percentage: {actual_data_corruption:.2f}%")
    print(f"Original zero-width character count: {original_count}")
    print(f"Remaining zero-width character count: {remaining_count}")
    print(f"Number of zero-width characters removed: {removed_count}")
    print(f"Number of zero-width characters altered: {altered_count}")
    print(f"Survival rate: {survival_rate:.2f}%")
    print(f"Decode result: {decode_result}")
    print(f"Recovered message: {recovered if recovered is not None else 'Not available'}")
    print(f"Recovered message matches original: {recovered == secret_message}")
    print(f"Decoding error: {decoding_error if decoding_error else 'None'}")
    print("-" * 78)


def main():
    scenarios = [
        ("removal", 10, "Hello"),
        ("removal", 20, "Zero Width Test"),
        ("removal", 30, "CS481 Test 123!"),
        ("alteration", 10, "This is a longer test message for Week 3."),
        ("alteration", 20, "Team A"),
        ("mixed", 30, "CS481"),
    ]

    print("TRISTAN KOCH WEEK 6 FIVE-COPY RECOVERY TESTS")
    print("=" * 78)
    for test_number, (corruption_type, percentage, secret_message) in enumerate(
        scenarios, start=1
    ):
        run_test(test_number, corruption_type, percentage, secret_message)


if __name__ == "__main__":
    main()
