"""Run Henry's Week 10 codec-verification and failure-analysis checks."""

from pathlib import Path
import sys


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from src.failure_analysis import analyze_recovered_text
from src.zero_width_codec import ONE, ZERO, embed_secret


def main() -> None:
    cover = "Team 1 compatibility test."
    secret = "WeChat test message"
    sent = embed_secret(cover, secret, recovery_mode=False)
    exact = analyze_recovered_text(sent, sent, secret)
    removed = analyze_recovered_text(sent, cover, secret)

    first_symbol = next(
        index for index, character in enumerate(sent) if character in {ZERO, ONE}
    )
    replacement = ONE if sent[first_symbol] == ZERO else ZERO
    altered_text = sent[:first_symbol] + replacement + sent[first_symbol + 1 :]
    altered = analyze_recovered_text(sent, altered_text, secret)

    checks = (
        ("Baseline count reproduces 278", exact["sent_counts"]["total"] == 278),
        (
            "Per-character counts reproduce 137/111/30",
            exact["sent_counts"]
            == {"U+200B": 137, "U+200C": 111, "U+200D": 30, "total": 278},
        ),
        ("Local exact recovery", exact["exact_match"]),
        ("Complete removal classified", removed["failure_category"] == "complete_payload_removal"),
        ("Altered marker classified", altered["failure_category"] == "frame_marker_corruption"),
    )

    print("HENRY SMITH - WEEK 10 CODEC VERIFICATION")
    print(f"Secret: {secret!r}")
    print(f"Codec counts: {exact['sent_counts']}")
    for description, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'}  {description}")
    print(f"All Week 10 verification checks passed: {all(value for _, value in checks)}")
    print("Production raw-data review: pending Tristan's sent/retrieved files")
    if not all(value for _, value in checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
