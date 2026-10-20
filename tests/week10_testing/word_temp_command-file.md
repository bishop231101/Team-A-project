# Week 10 Preliminary Feasibility Check — Microsoft Word Save, Reopen, and Retrieve

This is a preliminary feasibility check for **Microsoft Word — save, close or reopen, and retrieve text**. It is not an official production trial and must not count toward the planned workload. Use only corpus entry `SA01`; do not change the approved protocol. If Word or the workflow is unavailable, record the blocker and report it to Ifeanyi before proposing a change.

## 1. Preflight and local baseline

From the repository root, verify the repository and branch. The branch must be `tristan-week10`; stop if it is not.

```powershell
git rev-parse --show-toplevel
git branch --show-current
python tests/week9_testing/verify_henry_codec.py
python -m unittest discover -s tests -v
```

Use `tests/fixtures/week9_corpus.json` and validate `SA01`: category `short_ascii`, text `Hello`, SHA-256 `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`.

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

Do not continue if validation or local recovery fails. Display the exact UTF-8 payload with `Get-Content -Raw .\week10_sa01_encoded.txt` or a plain-text editor. Do not retype, normalize, trim, or repair it.

## 2. Manual Word operation

1. Confirm that Microsoft Word is the approved application and record its exact version, document format, and operating system.
2. Create a new blank document manually. Paste the entire encoded payload into the document without editing it. Do not use an automated macro or script.
3. Save the document to a manually chosen location and record the filename and format. Close Word fully.
4. Reopen the saved document manually. Select only the message text and copy it exactly. Do not include paragraph marks, headers, footers, or unrelated content. Record whether the text was retrieved before or after reopening and any Word conversion prompt.

## 3. Retrieval and analysis

Paste the copied text unchanged into a UTF-8 file named `week10_sa01_retrieved.txt`. Do not manually repair, normalize, or trim it. Run:

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

Record separate `U+200B`, `U+200C`, and `U+200D` encoded/retrieved counts, totals, retention (undefined when encoded total is zero), exact-text match, decode result/error, and exact `Hello` match. Collect relevant screenshots, Word/OS version, exact save/reopen/retrieve steps, and limitations without exposing unrelated document content or personal information.

## 4. Blank result record

```text
Preliminary check ID: ____________________
Platform-operation: Microsoft Word — save, reopen, and retrieve text
Expected behavior: local SA01 recovery is exactly Hello; saved/reopened text is measured unchanged.
Observed result: ______________________________________________
Corpus ID / expected SHA-256: SA01 / 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
Codec configuration: src/zero_width_codec.py; cover "Team 1 compatibility test."; recovery_mode=False
Microsoft Word version / document format: ____________________
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

Do not fabricate a Word result from these instructions. Keep this preliminary check separate from official production results.
