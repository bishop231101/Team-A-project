# Week 10 Preliminary Feasibility Check — Google Chrome Browser Console Paste and Copy Back

This is a preliminary feasibility check for **Google Chrome Browser Console — paste and copy back**, not an official production trial. Use only `SA01`; do not count it toward the planned workload or change the approved protocol. If Google Chrome or the workflow is unavailable, record the blocker and report it to Ifeanyi before proposing a change. This guide requires Google Chrome specifically, not Opera GX or another Chromium-based browser.

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
Path("tests/week10_testing/preliminary_testing/Google_Chrome_Browser_Console/week10_Chrome-01_sa01_encoded.txt").write_text(encoded, encoding="utf-8")
print({"corpus_id": item["id"], "counts": count_codec_characters(encoded), "local_round_trip": True})
'@ | python -
```

Stop on any validation or local-round-trip failure. Display the exact payload with `Get-Content -Raw 'tests/week10_testing/preliminary_testing/Google_Chrome_Browser_Console/week10_Chrome-01_sa01_encoded.txt'`; do not retype, normalize, trim, or repair it.

## 2. Manual Google Chrome Browser Console operation

1. Confirm manually that the browser is **Google Chrome**, not Opera GX or another Chromium-based browser. If Chrome access cannot be confirmed, record that blocker and stop for team-lead review; do not claim Chrome is installed or available.
2. Open Chrome's About page at `chrome://settings/help` and record the exact version shown there, the operating system, and the date of the check. Do not substitute a browser version from memory.
3. Start from a fresh Chrome tab with DevTools opened through the normal Chrome UI. Select the **Console** panel and leave an empty Console prompt ready. Do not navigate to a page containing private data, install an extension, disable browser security, change security settings, or use browser automation.
4. Before using the platform workflow, confirm that the local `SA01` encode/decode command in this guide completed successfully and that `tests/week10_testing/preliminary_testing/Google_Chrome_Browser_Console/week10_Chrome-01_sa01_encoded.txt` is the exact locally generated payload. If it failed, stop and investigate; do not open the Console for the platform check.
5. Manually open `tests/week10_testing/preliminary_testing/Google_Chrome_Browser_Console/week10_Chrome-01_sa01_encoded.txt` in a plain-text editor and copy its entire contents exactly, including the visible cover text and invisible characters. In the empty Chrome Console prompt, paste that exact text only as text to be copied back. Do **not** press Enter, execute it, wrap it in JavaScript, type a function, or paste any unreviewed script. The Console test is a paste-and-copy-back check, not code execution.
6. If Chrome displays a self-XSS or paste-protection warning, do not type an allow phrase, bypass the warning, or weaken a security setting. Record the warning and stop the check for team-lead review because the required manual operation was not safely available.
7. If Chrome accepts the paste without requiring a bypass, manually select the complete unexecuted text in the Console prompt and copy it back. Paste that clipboard content unchanged into UTF-8 `tests/week10_testing/preliminary_testing/Google_Chrome_Browser_Console/week10_Chrome-01_sa01_retrieved.txt`. Do not include the prompt marker, any Console output, a warning, or unrelated text. If the prompt cannot be copied back exactly without executing or transforming the payload, stop and record the workflow as blocked rather than inventing a workaround.
8. Record the precise starting state, exact source file, paste location, whether the paste warning appeared, whether Enter was avoided, the copy-back method, and any observed alteration. Keep all browser interactions manual.

## 3. Retrieval and analysis

Do not manually repair, normalize, or trim `tests/week10_testing/preliminary_testing/Google_Chrome_Browser_Console/week10_Chrome-01_sa01_retrieved.txt`. Run:

```powershell
@'
from pathlib import Path
from src.zero_width_codec import count_codec_characters, extract_secret
sent = open("tests/week10_testing/preliminary_testing/Google_Chrome_Browser_Console/week10_Chrome-01_sa01_encoded.txt", encoding="utf-8", newline="").read(); retrieved = open("tests/week10_testing/preliminary_testing/Google_Chrome_Browser_Console/week10_Chrome-01_sa01_retrieved.txt", encoding="utf-8", newline="").read()
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

Record separate `U+200B`, `U+200C`, and `U+200D` counts, totals, retention (undefined when encoded total is zero), exact-text match, decode result/error, and exact recovered-secret equality. Collect relevant screenshots of the Chrome About page, the empty/used Console prompt without unrelated content, and the local analysis; record the exact Chrome version, OS version, precise manual steps, and limitations. Exclude unrelated browsing data, private messages, account details, and credentials. If the Console cannot support a safe, reliable, unexecuted paste-and-copy-back operation, leave the result pending or blocked and request team-lead review.

## 4. Blank result record

```text
Preliminary check ID: ____________________
Platform-operation: Google Chrome Browser Console — paste and copy back
Expected behavior: local SA01 recovery is exactly Hello; Console copy-back is measured without repair.
Observed result: ______________________________________________
Corpus ID / expected SHA-256: SA01 / 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
Codec configuration: src/zero_width_codec.py; cover "Team 1 compatibility test."; recovery_mode=False
Browser (must be Google Chrome): ____________________
Precise Chrome version: ____________________
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

Do not fabricate Chrome availability or a browser result. Keep this preliminary check separate from official production results.
