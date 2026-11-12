# Notepad++ Reproducibility Procedure

**Prepared by:** Tristan Koch  
**Date:** November 11, 2026  
**Platform:** Notepad++  
**Operation:** Paste encoded text into a clean Notepad++ document, then copy it back.

## Purpose

This document records the reproducible Week 11 Notepad++ production-testing procedure and the results stored in the completed trial JSON records. It is separate from the Week 11 manual guide and does not alter any trial artifact.

## Confirmed inputs and environment

- Use the prepared trial folders under `tests/week11_testing/production_testing/Notepad++/`.
- The official corpus IDs were `SA01`, `SA02`, `SU01`, `SU02`, `LA01`, `LA02`, `LU01`, and `LU02`, with repetitions `R1`, `R2`, and `R3`.
- The approved operation was `paste_and_copy_back` with the `reuse_encoded_input` policy. Each repetition had its own sent file, retrieved file, JSON record, and evidence.
- The application used was Notepad++. The records and screenshots inspected do not record the Notepad++ version or the operating-system version; those values remain unverified.
- The procedure required the retrieved file to be saved as UTF-8 while preserving the captured line endings. A more specific Notepad++ encoding or newline setting is not recorded in the completed JSON records.
- The trial records identify the prepared codec/protocol context as protocol version `1.0-week11-baseline` and preserve the input hash for each repetition.

## Reproduction procedure

1. Select one trial folder and open its JSON record. Confirm the trial ID, corpus ID, repetition, platform, operation, and sent/retrieved paths. Confirm `local_validation.passed` and `local_validation.exact_round_trip` are true before beginning the platform operation.
2. Open that trial's `_sent.txt` file in a plain-text editor. Copy the entire encoded message exactly, including cover text, line endings, separators, and zero-width characters. Do not regenerate, retype, trim, normalize, format, or repair the input.
3. Open a new clean Notepad++ document and paste the copied message without editing it.
4. Capture the Notepad++ evidence screenshot in the trial's `evidence/` directory. The completed records use names such as `W11_NPP-SA01_R1.png`.
5. Copy the complete message back out of the same Notepad++ document. Select only the transferred message; do not include application chrome or unrelated content.
6. Paste the clipboard content unchanged into the matching `_retrieved.txt` file. Preserve the raw result, including an empty or corrupted result if one occurs. Save using UTF-8 and preserve the captured line endings.
7. Update only the selected JSON record with the tester, current UTC `timestamp_utc`, completed status, and the actual screenshot path. Keep evidence paths relative to `tests/week11_testing/production_testing` and point them to files, not directories.
8. From the repository root, run:

   ```powershell
   python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Notepad++/W11_Notepad++-SA01_R1/W11_Notepad++-SA01_R1.json
   ```

   Replace the trial ID in the record path for another repetition. The analyzer reads the matching sent and retrieved paths from that JSON record.

9. Review the analyzer output and JSON fields for sent/retrieved counts of U+200B, U+200C, and U+200D, retention percentage, decoder return, exact match, decoder error, and failure category. Capture the analyzer terminal screenshot, add its path to the selected record, save, and run the same analyzer command again.

## Observed results

All 24 completed Notepad++ records were checked:

- 24 of 24 trials had `retention_percentage` equal to `100.0`.
- Every trial retained the complete sent zero-width payload, with matching retrieved counts for U+200B, U+200C, and U+200D.
- `decoder_returned` was `true` for all 24 trials.
- `exact_match` was `true` for all 24 trials.
- No Notepad++ trial was classified with a failure category.

The records therefore support exact recovery for all completed Notepad++ production trials. This is a Week 11 observed result documented during Week 13; it is not a new experiment.

## Reproducibility limits

The repository evidence confirms the application, operation, file paths, UTF-8 save requirement, line-ending preservation requirement, timestamps, screenshots, and analyzer procedure. It does not verify the Notepad++ version, Windows version, or a more specific encoding/newline dialog selection. A reproducer should record those values at the time of a new run rather than infer them from this document.
