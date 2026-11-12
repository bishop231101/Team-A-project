# Telegram Web Reproducibility Procedure

**Prepared by:** Tristan Koch  
**Date:** November 12, 2026  
**Platform:** Telegram Web  
**Operation:** Send the encoded message through Telegram Web, then retrieve the message body.

## Purpose and scope

This procedure documents the completed Week 11 Telegram Web production-testing workflow. It is intended to allow another team member to reproduce the 24 official trials and compare the zero-width characters retrieved from Telegram Web with the original encoded payload.

The test set contains eight official corpus IDs and three independent repetitions per corpus: 24 trials total. The approved repetition policy is `reuse_encoded_input`: the prepared encoded input for each corpus ID is reused unchanged for R1, R2, and R3, while every repetition has its own sent file, retrieved file, JSON record, and evidence.

## Environment and confirmed conditions

- Use the prepared trial folders under `tests/week11_testing/production_testing/Telegram_Web/`.
- The records identify the platform as `Telegram Web`, the platform directory as `Telegram_Web`, and the operation as `send_and_retrieve`.
- The documented access method was manual Telegram Web use: open Telegram Web, confirm the approved account and exact chat or recipient, send the prepared message, then retrieve and copy the message body.
- The trial records do not document a Telegram Web/browser version, operating-system version, exact URL or client variant, account mode, or session settings. A reproducer must record those details if needed for a new run; they must not be inferred from this guide.
- The recorded protocol version is `1.0-week11-baseline`, with `recovery_mode` set to `false` and cover text `Team 1 compatibility test.`.
- The repository evidence references an operation screenshot and an analyzer-terminal screenshot for each completed trial. Preserve those references and do not expose private account information, credentials, unrelated messages, or personal data.

## Official inputs

The eight corpus definitions are maintained in `tests/fixtures/week9_corpus.json`. Use the prepared encoded `_sent.txt` file for the selected trial rather than regenerating or rewriting its payload.

| Corpus ID | Corpus category |
|---|---|
| `SA01` | `short_ascii` |
| `SA02` | `short_ascii` |
| `SU01` | `short_unicode` |
| `SU02` | `short_unicode` |
| `LA01` | `long_ascii` |
| `LA02` | `long_ascii` |
| `LU01` | `long_unicode` |
| `LU02` | `long_unicode` |

Each ID has repetitions `R1`, `R2`, and `R3`. The original encoded message includes the recorded cover text and the zero-width payload. Copy it exactly from the matching `_sent.txt` file.

## Trial file layout

For corpus ID `{CORPUS}` and repetition `{R}`, the prepared trial uses:

```text
tests/week11_testing/production_testing/Telegram_Web/
└── W11_Telegram_Web-{CORPUS}_R{R}/
    ├── W11_Telegram_Web-{CORPUS}_R{R}_sent.txt
    ├── W11_Telegram_Web-{CORPUS}_R{R}_retrieved.txt
    ├── W11_Telegram_Web-{CORPUS}_R{R}.json
    └── evidence/
        ├── W11_Telegram_Web-{CORPUS}_R{R}.png
        └── W11_Telegram_Web-{CORPUS}_R{R}_terminal.png
```

The JSON record stores paths relative to `tests/week11_testing/production_testing`, for example:

```text
Telegram_Web/W11_Telegram_Web-SA01_R1/W11_Telegram_Web-SA01_R1_sent.txt
Telegram_Web/W11_Telegram_Web-SA01_R1/W11_Telegram_Web-SA01_R1_retrieved.txt
Telegram_Web/W11_Telegram_Web-SA01_R1/W11_Telegram_Web-SA01_R1.json
Telegram_Web/W11_Telegram_Web-SA01_R1/evidence/W11_Telegram_Web-SA01_R1.png
Telegram_Web/W11_Telegram_Web-SA01_R1/evidence/W11_Telegram_Web-SA01_R1_terminal.png
```

## Reproduction procedure

1. Select one corpus ID and repetition. Open the matching JSON record and confirm its `trial_id`, `corpus_id`, `repetition`, platform, operation, sent path, and retrieved path. Confirm `local_validation.passed` and `local_validation.exact_round_trip` are true.
2. Open the selected `_sent.txt` file in a plain-text editor. Copy the complete original encoded contents, including visible cover text, line endings, separators, and invisible zero-width characters. Do not retype, trim, normalize, reformat, shorten, split, repair, or regenerate the payload.
3. Open Telegram Web manually. Confirm the approved Telegram account and exact chat or recipient. Record the actual Telegram Web/browser version, client variant or URL, operating system, and date if conducting a new reproduction.
4. Paste the complete copied payload into the Telegram Web message interface and send it manually. Do not add formatting or other text.
5. Open the sent or delivered message through the approved retrieval path. Copy only the complete message body. Exclude interface text, headers, quoted replies, signatures, unrelated messages, and prompt markers.
6. Save the copied body unchanged to the matching `_retrieved.txt` file. Preserve the raw Telegram Web result, including any zero-width-character loss or corruption. Do not replace it with the original sent text or expected plaintext.
7. Capture the Telegram Web operation screenshot and save it in the selected trial's `evidence/` directory. Do not expose credentials or unrelated private information.
8. Generate the current UTC timestamp and enter it in the selected JSON record's `timestamp_utc` field:

   ```powershell
   (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
   ```

9. Update only the selected JSON record with the tester, completed status, UTC timestamp, and actual evidence file paths. Preserve the record's trial identity, input hash, sent path, and retrieved path.
10. From the repository root, run the matching analyzer command in the next section. Capture the analyzer terminal output as evidence, add its file path to `evidence_paths`, save the JSON record, and run the same command again to verify the final record.
11. Inspect the resulting JSON for `analysis_status`, `analysis_errors`, sent and retrieved counts for U+200B/U+200C/U+200D, `retention_percentage`, `decoder_returned`, `exact_match`, `decoder_error`, and `failure_category`.

Do not introduce an extra formatting or editing step between copying from Telegram Web and saving the retrieved file. The measured result must reflect what Telegram Web returned.

## Analyzer commands

The official analyzer interface is:

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record <matching-record-path>
```

The following commands are prewritten for all 24 Telegram Web trials. Run them only after the matching retrieved file contains the raw result.

### SA01

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Telegram_Web/W11_Telegram_Web-SA01_R1/W11_Telegram_Web-SA01_R1.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Telegram_Web/W11_Telegram_Web-SA01_R2/W11_Telegram_Web-SA01_R2.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Telegram_Web/W11_Telegram_Web-SA01_R3/W11_Telegram_Web-SA01_R3.json
```

### SA02

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Telegram_Web/W11_Telegram_Web-SA02_R1/W11_Telegram_Web-SA02_R1.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Telegram_Web/W11_Telegram_Web-SA02_R2/W11_Telegram_Web-SA02_R2.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Telegram_Web/W11_Telegram_Web-SA02_R3/W11_Telegram_Web-SA02_R3.json
```

### SU01

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Telegram_Web/W11_Telegram_Web-SU01_R1/W11_Telegram_Web-SU01_R1.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Telegram_Web/W11_Telegram_Web-SU01_R2/W11_Telegram_Web-SU01_R2.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Telegram_Web/W11_Telegram_Web-SU01_R3/W11_Telegram_Web-SU01_R3.json
```

### SU02

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Telegram_Web/W11_Telegram_Web-SU02_R1/W11_Telegram_Web-SU02_R1.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Telegram_Web/W11_Telegram_Web-SU02_R2/W11_Telegram_Web-SU02_R2.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Telegram_Web/W11_Telegram_Web-SU02_R3/W11_Telegram_Web-SU02_R3.json
```

### LA01

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Telegram_Web/W11_Telegram_Web-LA01_R1/W11_Telegram_Web-LA01_R1.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Telegram_Web/W11_Telegram_Web-LA01_R2/W11_Telegram_Web-LA01_R2.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Telegram_Web/W11_Telegram_Web-LA01_R3/W11_Telegram_Web-LA01_R3.json
```

### LA02

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Telegram_Web/W11_Telegram_Web-LA02_R1/W11_Telegram_Web-LA02_R1.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Telegram_Web/W11_Telegram_Web-LA02_R2/W11_Telegram_Web-LA02_R2.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Telegram_Web/W11_Telegram_Web-LA02_R3/W11_Telegram_Web-LA02_R3.json
```

### LU01

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Telegram_Web/W11_Telegram_Web-LU01_R1/W11_Telegram_Web-LU01_R1.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Telegram_Web/W11_Telegram_Web-LU01_R2/W11_Telegram_Web-LU01_R2.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Telegram_Web/W11_Telegram_Web-LU01_R3/W11_Telegram_Web-LU01_R3.json
```

### LU02

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Telegram_Web/W11_Telegram_Web-LU02_R1/W11_Telegram_Web-LU02_R1.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Telegram_Web/W11_Telegram_Web-LU02_R2/W11_Telegram_Web-LU02_R2.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Telegram_Web/W11_Telegram_Web-LU02_R3/W11_Telegram_Web-LU02_R3.json
```

## Evidence and metadata

Retain the following for each repetition:

- Original `_sent.txt` file, unchanged.
- Raw `_retrieved.txt` file copied from Telegram Web.
- JSON record with trial ID, corpus ID, repetition, tester, UTC timestamp, and evidence paths.
- Telegram Web operation screenshot, normally named `W11_Telegram_Web-{CORPUS}_R{R}.png`.
- Analyzer-terminal screenshot, normally named `W11_Telegram_Web-{CORPUS}_R{R}_terminal.png`.
- Final analyzer fields and any observed Telegram Web limitation.

Evidence paths in the completed records use the production-root-relative form shown in the Trial file layout section. Do not expose credentials or unrelated private account content in screenshots.

## Observed results

The completed Telegram Web records report:

| Corpus | Completed | Exact recoveries | Character retention |
|---|---:|---:|---:|
| `SA01` | 3/3 | 3/3 | 100% |
| `SA02` | 3/3 | 3/3 | 100% |
| `SU01` | 3/3 | 3/3 | 100% |
| `SU02` | 3/3 | 3/3 | 100% |
| `LA01` | 3/3 | 3/3 | 100% |
| `LA02` | 3/3 | 3/3 | 100% |
| `LU01` | 3/3 | 3/3 | 100% |
| `LU02` | 3/3 | 3/3 | 100% |
| **Total** | **24/24** | **24/24** | **100%** |

All 24 records have `status: completed`, `analysis_status: completed`, `analysis_errors: []`, `local_validation.passed: true`, 100.0% retention, `decoder_returned: true`, `exact_match: true`, `decoder_error: null`, and `failure_category: null`. Sent and retrieved U+200B, U+200C, and U+200D counts matched in every trial.

These are observed results for the documented Telegram Web testing environment and procedure. They are not a guarantee of universal behavior across other Telegram Web versions, browsers, operating systems, accounts, sessions, or workflows.

## Troubleshooting and limitations

- If Telegram Web removes or changes zero-width characters, save exactly what was retrieved and let the analyzer measure the result. Do not repair or replace the retrieved text.
- If the message cannot be sent or retrieved, capture the relevant Telegram Web evidence, document the observed limitation and environment details, preserve the original sent file, and do not fabricate a retrieved result.
- Do not shorten, split, reformat, or regenerate the encoded payload to work around a platform limitation. A pre-transmission blocker is not a decoder failure.
- Do not run the normal analyzer against an empty retrieved file. Preserve the trial as incomplete or blocked according to the approved record convention and document why no measurement was collected.
- Keep each repetition independent and use only the matching corpus/repetition files.
