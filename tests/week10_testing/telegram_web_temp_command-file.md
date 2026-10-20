# Week 10 Preliminary Feasibility Check — Telegram Web Send and Retrieve

This is a preliminary feasibility check for **Telegram Web — send and retrieve message**, not an official production trial. Use only `SA01`; do not count it toward production workload or change the protocol. If Telegram Web or the workflow is unavailable, record the blocker and report it to Ifeanyi before proposing a change.

## 1. Preflight and local baseline

From the repository root, confirm the repository and branch; the branch must be `tristan-week10`.

```powershell
git rev-parse --show-toplevel
git branch --show-current
python tests/week9_testing/verify_henry_codec.py
python -m unittest discover -s tests -v
```

Load `SA01` from `tests/fixtures/week9_corpus.json`. It must be `short_ascii`, `Hello`, with SHA-256 `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`.

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

Stop on any failure. Display the exact payload with `Get-Content -Raw .\week10_sa01_encoded.txt` or a plain-text editor; do not alter it.

## 2. Manual Telegram Web operation

1. Confirm manually the approved Telegram account and exact chat/recipient. This guide does not choose a destination.
2. Open Telegram Web manually and record the Telegram Web/browser version, URL or client variant, and operating system.
3. Paste the complete encoded payload into a fresh message without editing it. Record any formatting or preview behavior.
4. Send the message manually only after confirming the destination.
5. Open the delivered message manually and copy only its body exactly. Exclude sender labels, timestamps, replies, and unrelated text.

## 3. Retrieval and analysis

Paste the copied body unchanged into UTF-8 `week10_sa01_retrieved.txt`; do not repair, normalize, or trim it. Run:

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

Record separate `U+200B`, `U+200C`, `U+200D` counts, totals, retention, exact-text equality, decode status/error, and exact recovered-secret equality. Collect relevant screenshots, Telegram Web/browser/OS versions, exact steps, and limitations without exposing private account details.

## 4. Blank result record

```text
Preliminary check ID: ____________________
Platform-operation: Telegram Web — send and retrieve message
Expected behavior: local SA01 recovery is exactly Hello; platform result is measured without repair.
Observed result: ______________________________________________
Corpus ID / expected SHA-256: SA01 / 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
Codec configuration: src/zero_width_codec.py; cover "Team 1 compatibility test."; recovery_mode=False
Telegram Web/browser version: ____________________
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

Do not imply that Telegram Web was tested merely because this guide exists. Keep preliminary results separate from production results.
