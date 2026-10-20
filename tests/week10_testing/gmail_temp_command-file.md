# Week 10 Preliminary Feasibility Check — Gmail Send and Retrieve

This is one preliminary feasibility check for the approved combination **Gmail — send and retrieve message**. It is not an official production trial and must not be counted toward the planned workload. Use only corpus entry `SA01` for this check. Do not change the approved protocol. If Gmail or the workflow is unavailable, record the blocker and report it to Ifeanyi before proposing a change.

## 1. Preflight and corpus validation

From the repository root, confirm the repository and branch:

```powershell
git rev-parse --show-toplevel
git branch --show-current
```

The branch must be `tristan-week10`. Record the output. If it is different, stop. Confirm that `tests/fixtures/week9_corpus.json` exists and that the repository is clean enough for you to identify your own pre-existing changes; do not overwrite or revert anyone’s work.

Run the approved repository verification commands before the check:

```powershell
python tests/week9_testing/verify_henry_codec.py
python -m unittest discover -s tests -v
```

The approved input is `SA01`, category `short_ascii`, expected secret `Hello`, and expected SHA-256 `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`. The following command loads the entry from the corpus, validates its category and hash, encodes it with the approved baseline, verifies local recovery, and saves the exact encoded text as UTF-8. Run it from the repository root; it creates a local artifact only when you perform this guide.

```powershell
@'
import hashlib, json
from pathlib import Path
from src.zero_width_codec import embed_secret, extract_secret, count_codec_characters

item = next(x for x in json.loads(Path("tests/fixtures/week9_corpus.json").read_text(encoding="utf-8")) if x["id"] == "SA01")
assert item["category"] == "short_ascii"
assert item["text"] == "Hello"
assert hashlib.sha256(item["text"].encode("utf-8")).hexdigest() == item["sha256"] == "185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969"
encoded = embed_secret("Team 1 compatibility test.", item["text"], recovery_mode=False)
assert extract_secret(encoded) == "Hello"
Path("week10_sa01_encoded.txt").write_text(encoded, encoding="utf-8")
print({"id": item["id"], "category": item["category"], "secret": item["text"], "counts": count_codec_characters(encoded), "local_round_trip": True})
'@ | python -
```

Do not proceed if corpus validation or the local round trip fails. Preserve the error, investigate the local issue, and report it. Do not assume a platform failure is responsible. For manual copying, display the exact file with `Get-Content -Raw .\week10_sa01_encoded.txt` or open it in a plain-text editor. Do not retype, normalize, trim, or repair it.

## 2. Manual Gmail operation

1. Confirm manually that you are using the intended Gmail account and the exact recipient/destination approved for this check. This guide does not choose a recipient.
2. Open Gmail manually and record the Gmail/browser version and operating system.
3. Start a fresh message. Paste the entire contents of `week10_sa01_encoded.txt` into the message body without editing it. Record the exact workflow and any formatting mode used.
4. Send the message manually only after confirming the destination. Do not send it to an unapproved account.
5. Open the delivered message manually in the intended recipient account, select the message body, and copy it exactly as displayed. Do not copy quoted replies, signatures, unrelated text, or headers.

## 3. Retrieval, comparison, and metrics

Paste the copied body into a new UTF-8 text file named `week10_sa01_retrieved.txt` without changing any character. Save it manually. Never trim, normalize, or repair retrieved text before comparison. Run this read-only analysis from the repository root:

```powershell
@'
from pathlib import Path
from src.zero_width_codec import count_codec_characters, extract_secret

sent = Path("week10_sa01_encoded.txt").read_text(encoding="utf-8")
retrieved = Path("week10_sa01_retrieved.txt").read_text(encoding="utf-8")
sc, rc = count_codec_characters(sent), count_codec_characters(retrieved)
print("encoded counts:", sc)
print("retrieved counts:", rc)
print("exact encoded-text match:", retrieved == sent)
if sc["total"] == 0:
    print("retention percentage: undefined (encoded total is zero)")
else:
    retention = rc["total"] / sc["total"] * 100
    print(f"retention percentage: {retention:.2f}%")
    if retention > 100:
        print("FLAG: retention exceeds 100%; investigate")
try:
    recovered = extract_secret(retrieved)
    print("decode succeeded:", True)
    print("recovered secret:", repr(recovered))
    print("exact recovered-secret match:", recovered == "Hello")
except Exception as error:
    print("decode succeeded:", False)
    print("decode error:", type(error).__name__, str(error))
'@ | python -
```

Report `U+200B`, `U+200C`, and `U+200D` separately and the totals exactly as returned. Exact-text equality and count retention are different measurements. Collect only relevant evidence: screenshots of the workflow and result, the Gmail/browser version, operating system, exact manual steps, and observed limitations. Exclude private messages, unrelated personal information, account details, and credentials.

## 4. Blank result record

Fill this in only after manually performing the check. It distinguishes expected behavior from observed results; do not pre-populate it.

```text
Preliminary check ID: ____________________
Platform-operation: Gmail — send and retrieve message
Expected behavior: SA01 is loaded from the approved corpus; local recovery is exactly Hello; platform result is measured without text repair.
Observed result: ______________________________________________
Corpus ID: SA01
Expected SHA-256: 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
Codec configuration: src/zero_width_codec.py; cover "Team 1 compatibility test."; recovery_mode=False; repetition_factor: not used
Gmail/browser version: ____________________
Operating system: ____________________
Encoded U+200B / U+200C / U+200D / total: ____ / ____ / ____ / ____
Retrieved U+200B / U+200C / U+200D / total: ____ / ____ / ____ / ____
Retention percentage: ____________________ (undefined if encoded total is zero)
Exact encoded-text match: Yes / No
Decode result: Success / Failure; error if any: ____________________
Recovered secret exactly equals Hello: Yes / No / Not decoded
Evidence references: _____________________________________________
Limitations and observations: ____________________________________
Next steps: _____________________________________________________
```

Do not claim that this check was performed merely because the commands are documented. Keep it separate from official production results.
