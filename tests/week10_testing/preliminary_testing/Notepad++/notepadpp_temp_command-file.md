# Week 10 Preliminary Feasibility Check — Notepad++ Paste and Copy Back

This is a preliminary feasibility check for **Notepad++ — paste and copy back**, not an official production trial. Use only `SA01`; do not count it toward the planned workload or change the approved protocol. If Notepad++ or the workflow is unavailable, record the blocker and report it to Ifeanyi before proposing a change.

## 1. Preflight and local baseline

From the repository root, confirm the repository and branch. The branch must be `tristan-week10`; stop if not.

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
Path("tests/week10_testing/preliminary_testing/Notepad++/week10_NPP-01_sa01_encoded.txt").write_text(encoded, encoding="utf-8")
print({"corpus_id": item["id"], "counts": count_codec_characters(encoded), "local_round_trip": True})
'@ | python -
```

Stop on validation or local-round-trip failure. Display the exact payload with `Get-Content -Raw 'tests/week10_testing/preliminary_testing/Notepad++/week10_NPP-01_sa01_encoded.txt'`; do not retype, normalize, trim, or repair it.

**Overwrite protection:** This command writes to the existing preliminary-test artifact `tests/week10_testing/preliminary_testing/Notepad++/week10_NPP-01_sa01_encoded.txt`. Rerunning it may overwrite that file. Preserve the existing evidence and compare or back it up before rerunning any command that writes to the same path.

## 2. Manual Notepad++ operation

1. Open Notepad++ manually and record its exact version, encoding setting, and operating system.
2. Open a new document. Paste the complete encoded payload into it without editing, replacing, or formatting it.
3. Copy the entire payload back manually from Notepad++ into `tests/week10_testing/preliminary_testing/Notepad++/week10_NPP-01_sa01_retrieved.txt` as UTF-8. Do not include other document content. Save it without changing line endings or encoding if the application presents a choice.
4. Record whether the copy-back was from the same open document and any encoding or line-ending prompt.

## 3. Retrieval and analysis

The saved retrieved file must be the exact copy-back, with no manual repair or normalization. Run:

```powershell
@'
from pathlib import Path
from src.zero_width_codec import count_codec_characters, extract_secret
sent = open("tests/week10_testing/preliminary_testing/Notepad++/week10_NPP-01_sa01_encoded.txt", encoding="utf-8", newline="").read(); retrieved = open("tests/week10_testing/preliminary_testing/Notepad++/week10_NPP-01_sa01_retrieved.txt", encoding="utf-8", newline="").read()
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

Record `U+200B`, `U+200C`, `U+200D` separately and in total for both files, retention (undefined if encoded total is zero), exact-text match, decode result/error, and exact `Hello` match. Collect relevant screenshots, Notepad++/OS version, exact steps, and limitations without exposing unrelated content.

## 4. Blank result record

```text
Preliminary check ID: ____________________
Platform-operation: Notepad++ — paste and copy back
Expected behavior: local SA01 recovery is exactly Hello; copy-back is measured without repair.
Observed result: ______________________________________________
Corpus ID / expected SHA-256: SA01 / 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
Codec configuration: src/zero_width_codec.py; cover "Team 1 compatibility test."; recovery_mode=False
Notepad++ version / encoding / line endings: ____________________
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

This documentation is not a performed test. Keep the preliminary result separate from official production data.
