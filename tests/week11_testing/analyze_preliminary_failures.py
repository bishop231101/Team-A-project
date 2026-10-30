"""Reproduce Henry's Week 11 review of Gmail and Word preliminary failures."""

from pathlib import Path
import sys


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from src.failure_analysis import analyze_recovered_text


TEST_ROOT = REPOSITORY_ROOT / "tests" / "week10_testing" / "preliminary_testing"
CASES = (
    (
        "Gmail",
        "Gmail/week10_Gmail-01_sa01_encoded.txt",
        "Gmail/week10_Gmail-01_sa01_retrieved.txt",
        {"U+200B": 0, "U+200C": 52, "U+200D": 16, "total": 68},
        "structural_corruption",
    ),
    (
        "Microsoft Word",
        "Microsoft_Word/week10_Word-01_sa01_encoded.txt",
        "Microsoft_Word/week10_Word-01_sa01_retrieved.txt",
        {"U+200B": 0, "U+200C": 0, "U+200D": 0, "total": 0},
        "complete_payload_removal",
    ),
)


def main() -> None:
    print("HENRY SMITH - WEEK 11 PRELIMINARY FAILURE ANALYSIS")
    all_passed = True
    for platform, sent_path, retrieved_path, expected_counts, expected_category in CASES:
        sent = (TEST_ROOT / sent_path).read_text(encoding="utf-8")
        retrieved = (TEST_ROOT / retrieved_path).read_text(encoding="utf-8")
        result = analyze_recovered_text(sent, retrieved, "Hello")
        passed = (
            result["sent_counts"]["total"] == 152
            and result["retrieved_counts"] == expected_counts
            and result["failure_category"] == expected_category
            and not result["decoder_returned"]
        )
        all_passed &= passed
        retention = result["retention_percentage"]
        print(f"\n{platform}")
        print(f"  Sent counts:      {result['sent_counts']}")
        print(f"  Retrieved counts: {result['retrieved_counts']}")
        print(f"  Retention:        {retention:.2f}%")
        print(f"  Decoder returned: {result['decoder_returned']}")
        print(f"  Failure category: {result['failure_category']}")
        print(f"  Evidence check:   {'PASS' if passed else 'FAIL'}")

    print(f"\nAll preliminary failure checks passed: {all_passed}")
    print("Data status: preliminary; not counted as official production trials")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
