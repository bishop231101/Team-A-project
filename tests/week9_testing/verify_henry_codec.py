"""Verify Henry's Week 9 corpus and baseline codec configuration."""

from hashlib import sha256
import json
from pathlib import Path
import sys


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from src.zero_width_codec import (
    ONE,
    SEPARATOR,
    ZERO,
    count_codec_characters,
    embed_secret,
    extract_secret,
)


CORPUS_PATH = REPOSITORY_ROOT / "tests" / "fixtures" / "week9_corpus.json"
COVER_TEXT = "Team 1 compatibility test."
CODEC_COMMIT = "4134cec1d23be3ae7069440a3718e09069922bdc"
EXPECTED_IDS = ("SA01", "SA02", "SU01", "SU02", "LA01", "LA02", "LU01", "LU02")


def visible_text(stego_text: str) -> str:
    return "".join(
        character
        for character in stego_text
        if character not in {ZERO, ONE, SEPARATOR}
    )


def main() -> None:
    corpus = json.loads(CORPUS_PATH.read_text(encoding="utf-8"))
    ids = tuple(item["id"] for item in corpus)
    if ids != EXPECTED_IDS or len(set(ids)) != len(ids):
        raise SystemExit("FAIL: corpus IDs are missing, duplicated, or out of order")

    print("HENRY SMITH - WEEK 9 CODEC AND CORPUS VERIFICATION")
    print(f"Codec commit: {CODEC_COMMIT}")
    print(f"Fixed cover: {COVER_TEXT}")
    print("ID    Category        UTF-8 bytes  Codec chars  Exact result")
    print("----  --------------  -----------  -----------  ------------")

    passed = 0
    for item in corpus:
        secret = item["text"]
        digest_matches = sha256(secret.encode("utf-8")).hexdigest() == item["sha256"]
        stego = embed_secret(COVER_TEXT, secret, recovery_mode=False)
        exact_match = extract_secret(stego) == secret
        cover_unchanged = visible_text(stego) == COVER_TEXT
        deterministic = stego == embed_secret(COVER_TEXT, secret, recovery_mode=False)
        item_passed = digest_matches and exact_match and cover_unchanged and deterministic
        passed += int(item_passed)
        codec_count = count_codec_characters(stego)["total"]
        print(
            f"{item['id']:<4}  {item['category']:<14}  "
            f"{len(secret.encode('utf-8')):>11}  {codec_count:>11}  "
            f"{'PASS' if item_passed else 'FAIL'}"
        )

    print(f"Corpus SHA-256 checks passed: {passed == len(corpus)}")
    print(f"Exact baseline round trips passed: {passed}/{len(corpus)}")
    print(f"Henry codec confirmation complete: {passed == len(corpus)}")
    if passed != len(corpus):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
