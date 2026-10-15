"""Analyze one Week 9 sent/retrieved text pair from the command line."""

import argparse
import json
from pathlib import Path
import sys


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from src.failure_analysis import analyze_recovered_text


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Measure count-based retention and classify decoder behavior."
    )
    parser.add_argument("--sent", type=Path, required=True, help="UTF-8 sent-text file")
    parser.add_argument(
        "--retrieved", type=Path, required=True, help="UTF-8 retrieved-text file"
    )
    parser.add_argument("--secret", required=True, help="Expected synthetic secret")
    arguments = parser.parse_args()

    result = analyze_recovered_text(
        arguments.sent.read_text(encoding="utf-8"),
        arguments.retrieved.read_text(encoding="utf-8"),
        arguments.secret,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
