# Microsoft Word Reproducibility Procedure

**Prepared by:** Tristan Koch  
**Date:** November 11, 2026  
**Platform:** Microsoft Word  
**Operation:** Save the encoded message, close and reopen the document, then retrieve the text.

## Purpose

This document records the reproducible Week 11 Microsoft Word production-testing procedure and the completed analyzer results. It is separate from the Week 11 manual guide and does not alter any trial artifact.

## Confirmed inputs and environment

- Use the prepared trial folders under `tests/week11_testing/production_testing/Microsoft_Word/`.
- The official corpus IDs were `SA01`, `SA02`, `SU01`, `SU02`, `LA01`, `LA02`, `LU01`, and `LU02`, with repetitions `R1`, `R2`, and `R3`.
- The approved operation was `save_reopen_and_retrieve` with the `reuse_encoded_input` policy. Each repetition had its own sent file, retrieved file, JSON record, and evidence.
- The application used was Microsoft Word. The inspected records and screenshots do not record a Word version or operating-system version; those values remain unverified.
- The Word evidence shows a saved document with a `.docx` filename in the representative inspected trial, but the completed JSON records do not store the document-format field. The exact format and any conversion/compatibility prompt should be recorded in a future reproduction rather than inferred for every trial.
- The retrieved text was saved as UTF-8 while preserving the captured line endings. No additional Word encoding or environment setting is verified by the completed records.
- The trial records identify the prepared codec/protocol context as protocol version `1.0-week11-baseline` and preserve the input hash for each repetition.

## Reproduction procedure

1. Select one trial folder and open its JSON record. Confirm the trial ID, corpus ID, repetition, platform, operation, and sent/retrieved paths. Confirm `local_validation.passed` and `local_validation.exact_round_trip` are true before beginning the Word operation.
2. Open the selected `_sent.txt` file using the recorded path. Copy the complete encoded message exactly, including visible cover text, line endings, separators, and zero-width characters. Do not regenerate, retype, trim, normalize, format, or repair the input.
3. Open Microsoft Word manually and create a new blank document. Paste the complete encoded message without editing or reformatting it.
4. Capture the Word document screenshot in the trial's `evidence/` directory. The completed records use names such as `W11_Word-SA01_R1.png`.
5. Save the document, recording the actual format and save location. Close Word fully and reopen the saved document manually. Record any conversion, compatibility, encoding, repair, or format prompt and the option selected.
6. Select only the message content after reopening. Do not include headers, footers, paragraph marks, comments, or Word interface content. Copy the complete retrieved text.
7. Paste the copied content unchanged into the matching `_retrieved.txt` file. Save as UTF-8 while preserving the captured line endings. Preserve empty, truncated, or corrupted output exactly as retrieved; do not restore the expected zero-width payload.
8. Update only the selected JSON record with the tester, current UTC `timestamp_utc`, completed status, and the actual screenshot path. Keep evidence paths relative to `tests/week11_testing/production_testing` and point them to files, not directories.
9. From the repository root, run:

   ```powershell
   python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Word/W11_Word-SA01_R1/W11_Word-SA01_R1.json
   ```

   Replace the trial ID in the record path for another repetition. The analyzer reads the matching sent and retrieved paths from that JSON record.

10. Review the analyzer output and JSON fields for sent/retrieved counts of U+200B, U+200C, and U+200D, retention percentage, decoder return, exact match, decoder error, and failure category. Capture the analyzer terminal screenshot, add its path to the selected record, save, and run the same analyzer command again.

## Observed results

All 24 completed Microsoft Word records were checked:

- 24 of 24 trials experienced complete zero-width payload removal.
- Retrieved counts were zero for U+200B, U+200C, and U+200D in every trial.
- `retention_percentage` was `0.0` for all trials.
- `decoder_returned` was `false` for all trials.
- `exact_match` was `false` for all trials.
- Every trial had failure category `complete_payload_removal`.
- The analyzer error was that no zero-width payload was found.

These results describe the completed Week 11 save/reopen/retrieve trials. They do not claim that every Word version or document workflow behaves identically outside the recorded test conditions.

## Reproducibility limits

The repository evidence confirms the application, operation, prepared-file workflow, save/close/reopen sequence, raw retrieval requirement, screenshots, timestamps, and analyzer procedure. It does not verify the Microsoft Word version, Windows version, exact document-format choice for every repetition, or any conversion/compatibility prompt. A reproducer must record those values during the run.
