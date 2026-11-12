# Discord Reproducibility Procedure

**Prepared by:** Tristan Koch  
**Date:** November 11, 2026  
**Platform:** Discord  
**Operation:** Send the encoded message in an approved Discord text channel, then retrieve the message body.

## Purpose and scope

This procedure documents the official Week 11 Discord production-testing workflow and the Week 13 record interpretation. It is intended to allow another team member to reproduce the 24 planned Discord trials, compare the recovered zero-width payload with the original, and distinguish a measured platform result from a trial blocked before transmission.

The official Discord set contains eight corpus messages and three independent repetitions per message: 24 planned trials in total. The approved repetition policy is `reuse_encoded_input`: the prepared encoded input for each corpus ID is reused unchanged for R1, R2, and R3, while each repetition keeps its own trial folder, files, JSON record, and evidence.

## Required setup

- Access to the project repository and the prepared files under `tests/week11_testing/production_testing/Discord/`.
- A Discord account with access to the approved server and text channel used by the team. The existing evidence shows the Capstone Project Server and the `week-11-trials` channel; confirm current access before reproducing a trial.
- A plain-text editor or repository editor for opening the prepared `_sent.txt` file and saving the retrieved text.
- PowerShell and Python available from the repository root for the timestamp command and the official analyzer.
- A way to capture the required Discord and analyzer screenshots without exposing unrelated private information.

The repository does not record a required Discord application version, operating-system version, or account setting. A reproducer should record those details if they are needed for a separate reproduction rather than infer them from this guide. Discord Nitro is not required for trials whose payloads fit within the account's message limit; the LA02 payload exceeded the standard limit in the documented campaign.

## Official corpus messages

These are the existing definitions in `tests/fixtures/week9_corpus.json`. They are the plaintext secrets used to prepare the encoded `_sent.txt` files. Do not rewrite them or generate replacement payloads for an official trial.

| Corpus ID | Category | Existing message |
|---|---|---|
| `SA01` | `short_ascii` | `Hello` |
| `SA02` | `short_ascii` | `Test 123!` |
| `SU01` | `short_unicode` | `Café` |
| `SU02` | `short_unicode` | `你好` |
| `LA01` | `long_ascii` | `The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. ` |
| `LA02` | `long_ascii` | `Team 1 checks message recovery, punctuation, and numbers 12345. Team 1 checks message recovery, punctuation, and numbers 12345. Team 1 checks message recovery, punctuation, and numbers 12345. Team 1 checks message recovery, punctuation, and numbers 12345. ` |
| `LU01` | `long_unicode` | `Café déjà vu — résumé. Café déjà vu — résumé. Café déjà vu — résumé. Café déjà vu — résumé. ` |
| `LU02` | `long_unicode` | `你好，世界！こんにちは。 你好，世界！こんにちは。 你好，世界！こんにちは。 你好，世界！こんにちは。 ` |

The prepared encoded files use the recorded cover text `Team 1 compatibility test.` together with the encoded corpus message. The encoded content, including zero-width characters, must be copied from the prepared file rather than recreated manually.

## Trial file layout and naming

Each trial uses this pattern, where `{CORPUS}` is one of the eight IDs and `{R}` is `1`, `2`, or `3`:

```text
tests/week11_testing/production_testing/Discord/
└── W11_Discord-{CORPUS}_R{R}/
    ├── W11_Discord-{CORPUS}_R{R}_sent.txt
    ├── W11_Discord-{CORPUS}_R{R}_retrieved.txt
    ├── W11_Discord-{CORPUS}_R{R}.json
    └── evidence/
        ├── W11_Discord-{CORPUS}_R{R}.png
        └── W11_Discord-{CORPUS}_R{R}_terminal.png
```

The JSON record stores production-root-relative paths such as:

```text
Discord/W11_Discord-SA01_R1/W11_Discord-SA01_R1_sent.txt
Discord/W11_Discord-SA01_R1/W11_Discord-SA01_R1_retrieved.txt
Discord/W11_Discord-SA01_R1/W11_Discord-SA01_R1.json
Discord/W11_Discord-SA01_R1/evidence/W11_Discord-SA01_R1.png
Discord/W11_Discord-SA01_R1/evidence/W11_Discord-SA01_R1_terminal.png
```

The actual screenshot names may follow the matching trial ID. Use the path already present in the selected JSON record when reproducing or reviewing a trial.

## Reproduction procedure

### Step 1 — Select the prepared trial

Choose one existing trial folder and open its JSON record. Confirm its `trial_id`, `corpus_id`, `repetition`, `platform` (`Discord`), `operation` (`send_and_retrieve`), and sent/retrieved paths. Confirm the matching `_sent.txt` file belongs to that exact repetition. Do not regenerate the encoded input.

### Step 2 — Copy the original encoded message

Open the selected `_sent.txt` file and copy its complete contents. Preserve the visible cover text, line endings, separators, and all invisible zero-width characters. Do not retype, trim, normalize, shorten, split, format, or repair the message.

### Step 3 — Send through Discord

1. Open the approved Discord server and text channel.
2. Paste the complete copied message into the message box.
3. Send the message manually.
4. Capture the required evidence screenshot showing the Discord operation and save it in that trial's `evidence/` directory.

Do not assume that Discord preserves zero-width characters. The test measures the content Discord actually returns.

### Step 4 — Retrieve and preserve the message

1. Locate the sent Discord message.
2. Copy only the complete message content, without Discord interface text or unrelated messages.
3. Paste the copied content unchanged into that trial's matching `_retrieved.txt` file.
4. Preserve any loss, corruption, or empty result exactly as retrieved. Do not substitute the original sent content or expected plaintext.

### Step 5 — Record metadata and evidence

For a successfully executed trial, update only the selected JSON record with the required tester, UTC `timestamp_utc`, completed status, and actual evidence file paths. Keep evidence references relative to `tests/week11_testing/production_testing` and reference individual files rather than only an evidence directory.

The repository's existing timestamp command is:

```powershell
(Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
```

Run it when the trial is performed. Do not reuse a timestamp from another trial.

### Step 6 — Run the official analyzer

From the repository root, run the analyzer for the selected completed trial:

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Discord/W11_Discord-SA01_R1/W11_Discord-SA01_R1.json
```

Replace the record path with the selected trial's JSON path. The analyzer reads the sent and retrieved paths from that JSON record and records zero-width counts, retention, decoder success, exact recovery, decoder errors, and any applicable failure category. Capture the analyzer terminal output as evidence, add its file path to the JSON record, save the record, and run the same command again to verify the final record.

Do not run this analyzer command for a blocked trial whose retrieved file is blank because no message was transmitted.

## Evidence and metadata to retain

For each completed Discord trial, retain:

- The original `_sent.txt` file unchanged.
- The raw `_retrieved.txt` content copied from Discord.
- The JSON record with its trial identity, corpus ID, repetition, operation, tester, UTC timestamp, and evidence paths.
- A Discord screenshot showing the manual send/retrieve operation.
- A terminal screenshot showing the analyzer output.
- The analyzer measurements stored in the JSON record.

The 21 completed Discord records follow this procedure. Their analyzer results report 100% character retention, decoder success, and exact recovery for every executed trial.

## Observed campaign results

The completed Discord campaign accounts for 24 planned trials:

- 21 trials were successfully executed and analyzed.
- All 21 completed trials retained 100% of the sent zero-width characters and achieved exact recovery.
- `W11_Discord-LA02_R1`, `W11_Discord-LA02_R2`, and `W11_Discord-LA02_R3` were blocked before transmission because the original encoded LA02 payload exceeded Discord's standard message-size limit. Sending it would require Discord Nitro.
- The three blocked records retain their separate trial IDs and reference the shared evidence file `Discord/W11_Discord-LA02_R1/evidence/W11_Discord-LA02_unable-to-send.png`.
- The blocked records have null measurements and no retrieved payload or decoder result. They are not analyzed as decoder failures and are excluded from recovery comparisons.

These results describe the documented account, payloads, and send/retrieve procedure. They should not be generalized to every Discord account, subscription level, client version, or workflow.

## Troubleshooting and platform limitations

If Discord prevents a message from being sent:

1. Do not modify, shorten, split, re-encode, or otherwise repair the original `_sent.txt` payload.
2. Capture a screenshot of the limitation, preserving the application message that explains why transmission was unavailable.
3. Keep the original sent file and its trial identity unchanged.
4. Do not create a fabricated retrieved file or decoder result. Leave `measured_results` null.
5. Document the limitation factually in the JSON `notes` field and set the record status to `blocked` when the platform operation did not occur.
6. Reference the actual screenshot file in `evidence_paths`. A single screenshot may be shared by multiple repetitions when it documents the same limitation, as with the three LA02 records.
7. Do not run the normal analyzer against a blank retrieved file. The current analyzer accepts completed or failed transfer records, not pre-transmission `blocked` records; treating a blocked trial as a decoding failure would create misleading measurements.

If the message is sent successfully, continue with retrieval, raw-file preservation, metadata, evidence, and analyzer steps above. If only part of a message is obtained, preserve exactly what was obtained and document the limitation rather than replacing it with expected content.
