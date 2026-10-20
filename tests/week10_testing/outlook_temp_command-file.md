# Week 10 Preliminary Feasibility Check — Microsoft Outlook Send and Retrieve

This is a preliminary feasibility check for **Microsoft Outlook — send and retrieve message**, not an official production trial. Use only `SA01`; do not count it toward production workload or alter the protocol. If Outlook or the workflow is unavailable, record the blocker and report it to Ifeanyi before proposing a change.

## 1. Preflight and local baseline

From the repository root, confirm the repository and branch. The branch must be `tristan-week10`; stop otherwise. Preserve pre-existing changes.

```powershell
git rev-parse --show-toplevel
git branch --show-current
python tests/week9_testing/verify_henry_codec.py
python -m unittest discover -s tests -v
```

Validate `SA01` from `tests/fixtures/week9_corpus.json`: category `short_ascii`, text `Hello`, expected SHA-256 `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`.

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
Path("week10_sa01_encoded.txt").write_text(encoded, encoding="utf-8")
print({"corpus_id": item["id"], "counts": count_codec_characters(encoded), "local_round_trip": True})
'@ | python -
```

Stop on any validation or local-round-trip failure. Display the exact payload with `Get-Content -Raw .\week10_sa01_encoded.txt`; never retype, trim, normalize, or repair it.

## 2. Manual Outlook operation

1. Confirm the approved Outlook account and exact recipient/destination manually; this guide does not invent either one.
2. Open Outlook manually and record the Outlook desktop/web version and operating system.
3. Start a fresh message and paste the complete encoded payload into the body without editing it. Record any format choice or conversion behavior.
4. Send manually only after confirming the destination.
5. Open the delivered message manually in the intended recipient account and copy only the message body exactly as retrieved. Exclude quoted replies, signatures, headers, and unrelated text.

## 3. Retrieval and analysis

Paste the copied body unchanged into UTF-8 `week10_sa01_retrieved.txt`. Do not repair or normalize it. Run:

```powershell
@'
from pathlib import Path
from src.zero_width_codec import count_codec_characters, extract_secret
sent = Path("week10_sa01_encoded.txt").read_text(encoding="utf-8"); retrieved = Path("week10_sa01_retrieved.txt").read_text(encoding="utf-8")
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

Record individual `U+200B`, `U+200C`, `U+200D` counts, totals, retention, exact-text match, decode result/error, and exact recovered-secret equality. Collect relevant screenshots, Outlook/OS version, manual steps, and limitations only; exclude private or unrelated account information.

## 4. Blank result record

```text
Preliminary check ID: ____________________
Platform-operation: Microsoft Outlook — send and retrieve message
Expected behavior: local SA01 recovery is exactly Hello; platform result is measured without repair.
Observed result: ______________________________________________
Corpus ID / expected SHA-256: SA01 / 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
Codec configuration: src/zero_width_codec.py; cover "Team 1 compatibility test."; recovery_mode=False
Outlook version / account mode: ____________________
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

Documented commands are not performed tests. Keep the preliminary result separate from official production results.
