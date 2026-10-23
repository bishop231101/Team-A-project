# Week 10 Preliminary Feasibility Check — Discord Send and Retrieve

This is a preliminary feasibility check for **Discord — send and retrieve message**, not an official production trial. Use only `SA01`; do not count it toward the planned production workload or change the approved protocol. If Discord or the workflow is unavailable, record the blocker and report it to Ifeanyi before proposing a change.

## 1. Preflight and local baseline

From the repository root, verify the repository and branch:

```powershell
git rev-parse --show-toplevel
git branch --show-current
```

The branch must be `tristan-week10`; otherwise stop. Confirm `tests/fixtures/week9_corpus.json` exists and preserve all pre-existing changes. Run the existing checks:

```powershell
python tests/week9_testing/verify_henry_codec.py
python -m unittest discover -s tests -v
```

Load `SA01` from that corpus, not from a retyped replacement. It must have category `short_ascii`, text `Hello`, and SHA-256 `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`.

```powershell
@'
import hashlib, json
from pathlib import Path
from src.zero_width_codec import embed_secret, extract_secret, count_codec_characters
item = next(x for x in json.loads(Path("tests/fixtures/week9_corpus.json").read_text(encoding="utf-8")) if x["id"] == "SA01")
assert item["category"] == "short_ascii" and item["text"] == "Hello"
assert hashlib.sha256(item["text"].encode("utf-8")).hexdigest() == item["sha256"] == "185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969"
encoded = embed_secret("Team 1 compatibility test.", item["text"], recovery_mode=False)
assert extract_secret(encoded) == "Hello"
Path("tests/week10_testing/preliminary_testing/Discord/week10_Discord-01_sa01_encoded.txt").write_text(encoded, encoding="utf-8")
print({"corpus_id": item["id"], "counts": count_codec_characters(encoded), "local_round_trip": True})
'@ | python -
```

Stop if validation or local recovery fails. Display the exact payload with `Get-Content -Raw 'tests/week10_testing/preliminary_testing/Discord/week10_Discord-01_sa01_encoded.txt'` or a plain-text editor; do not retype, trim, normalize, or repair invisible characters.

## 2. Manual Discord operation

1. Confirm manually the approved Discord account, server/channel or direct-message destination, and recipient. This guide does not invent a destination.
2. Open Discord manually and record the Discord/client or browser version and operating system.
3. In a fresh message, paste the complete contents of `tests/week10_testing/preliminary_testing/Discord/week10_Discord-01_sa01_encoded.txt` without editing it. Record the channel/context and any visible formatting behavior.
4. Send the message manually only after confirming the destination.
5. Retrieve the delivered message body manually from Discord, selecting and copying exactly the sent text. Exclude usernames, timestamps, reactions, quoted text, and unrelated content.

## 3. Retrieval and analysis

Paste the copied body unchanged into `tests/week10_testing/preliminary_testing/Discord/week10_Discord-01_sa01_retrieved.txt` as UTF-8. Do not manually repair or normalize it. Run:

```powershell
@'
from pathlib import Path
from src.zero_width_codec import count_codec_characters, extract_secret
sent = open("tests/week10_testing/preliminary_testing/Discord/week10_Discord-01_sa01_encoded.txt", encoding="utf-8", newline="").read()
retrieved = open("tests/week10_testing/preliminary_testing/Discord/week10_Discord-01_sa01_retrieved.txt", encoding="utf-8", newline="").read()
sc, rc = count_codec_characters(sent), count_codec_characters(retrieved)
print("encoded:", sc); print("retrieved:", rc); print("exact encoded-text match:", retrieved == sent)
if sc["total"] == 0: print("retention percentage: undefined (encoded total is zero)")
else:
    p = rc["total"] / sc["total"] * 100; print(f"retention percentage: {p:.2f}%")
    print("FLAG: retention exceeds 100%; investigate" if p > 100 else "retention flag: none")
try:
    value = extract_secret(retrieved); print("decode succeeded:", True); print("recovered secret:", repr(value)); print("exact recovered-secret match:", value == "Hello")
except Exception as error: print("decode succeeded:", False); print("decode error:", type(error).__name__, str(error))
'@ | python -
```

Record each `U+200B`, `U+200C`, and `U+200D` count, each total, retention, exact-text equality, decode status/error, and exact equality with `Hello`. Collect relevant screenshots, version information, exact steps, and limitations only; exclude private or unrelated account information.

## 4. Blank result record

```text
Preliminary check ID: ____________________
Platform-operation: Discord — send and retrieve message
Expected behavior: local SA01 recovery is exactly Hello; platform preservation is measured without repair.
Observed result: ______________________________________________
Corpus ID / expected SHA-256: SA01 / 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
Codec configuration: src/zero_width_codec.py; cover "Team 1 compatibility test."; recovery_mode=False
Discord/client or browser version: ____________________
Operating system: ____________________
Encoded U+200B / U+200C / U+200D / total: ____ / ____ / ____ / ____
Retrieved U+200B / U+200C / U+200D / total: ____ / ____ / ____ / ____
Retention percentage: ____________________
Exact encoded-text match: Yes / No
Decode result and error: _________________________________________
Recovered secret exactly equals Hello: Yes / No / Not decoded
Evidence references: _____________________________________________
Limitations and observations: ____________________________________
Next steps: _____________________________________________________
```

Commands documented here are not evidence that the check occurred. Keep this preliminary result separate from official production trials.
