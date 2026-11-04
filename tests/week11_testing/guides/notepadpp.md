# Week 11 Notepad++ — Paste and Copy Back

This is the manual guide for the approved Week 11 Notepad++ paste-and-copy-back operation. It is for the official records under `tests/week11_testing/production_testing/Notepad++/`; do not use the Week 10 preliminary files.

## Before the transfer

1. Select one existing trial folder under `tests/week11_testing/production_testing/Notepad++/`. Use the folder and JSON record with the same trial ID, for example `W11_Notepad++-SA01_R1`.
2. Open the JSON record and verify its `trial_id`, `corpus_id`, `repetition`, `platform`, `operation`, and paths. The approved Notepad++ operation is `paste_and_copy_back`; the corpus IDs are `SA01`, `SA02`, `SU01`, `SU02`, `LA01`, `LA02`, and `LU01`, `LU02`, each with `R1`, `R2`, and `R3`.
3. Confirm `local_validation.passed` and `local_validation.exact_round_trip` are both `true`. This validates the codec/input setup only; it is not a platform result.
4. Confirm the matching `_sent.txt` and `_retrieved.txt` files exist in that trial folder. Use the trial's own files and never reuse another repetition's retrieved file.
5. Record the Notepad++ version, operating-system version, and the UTC start time. The required timestamp format is ISO 8601 UTC, such as `2026-10-29T20:14:01Z`.

## Manual Notepad++ operation

1. Open the selected trial's `_sent.txt` file in Notepad++ and verify the trial ID/path before copying.
2. Copy the complete encoded message exactly as saved. Do not retype, trim, normalize, format, repair, or otherwise alter cover text, line endings, or zero-width characters.
3. Open a new, clean Notepad++ document and paste the complete copied message into it without editing.
4. Capture the required screenshot of the clean Notepad++ document showing the transferred content. Save it in that trial's `evidence/` directory. Use a unique file name such as `W11_Notepad++-SA01_R1.png`.
5. Copy the complete message back out of the same Notepad++ document. Do not include other document content or application chrome.
6. Paste the copied content unchanged into the matching `_retrieved.txt` file. Save it using the existing protocol's UTF-8 and newline-preservation requirements. Preserve an empty or corrupted result exactly as obtained; do not repair zero-width characters.

## Record metadata and analyze

After the transfer and retrieved file have been saved:

1. Update only the selected JSON record. Set `status` to `completed` for a completed paste/copy-back operation, or `failed` for an actual platform-operation failure. Set `tester` to `Tristan Koch`, using the repository's established format. Set `timestamp_utc` to the current UTC timestamp in `YYYY-MM-DDTHH:mm:ssZ` format.
2. Add the Notepad++ document screenshot filepath to `evidence_paths` using the existing production-root-relative convention, for example `Notepad++/W11_Notepad++-SA01_R1/evidence/W11_Notepad++-SA01_R1.png`. Keep the record's evidence references inside `tests/week11_testing/production_testing` and point each reference to an existing, non-empty file.
3. From the repository root, run the analyzer for that exact record. Example:

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Notepad++/W11_Notepad++-SA01_R1/W11_Notepad++-SA01_R1.json
```

4. Review the analyzer output. It records separate `U+200B`, `U+200C`, and `U+200D` counts, total retention, `retention_percentage`, whether retention exceeded 100%, decoder success or error, exact recovered-secret match, and the failure category when applicable. Note relevant observations in the JSON `notes` array, including application/OS details, encoding or newline prompts, and any observed loss or corruption.
5. Capture a screenshot of the analyzer terminal output and save it under the same trial's `evidence/` directory, using a name such as `W11_Notepad++-SA01_R1_terminal.png`.
6. Add that terminal screenshot filepath to `evidence_paths`, save the JSON record, and run the same analyzer command again. The second run verifies the record after its final evidence update; retain the final analyzer fields and output.

## Completed versus failed trials

A trial is `completed` when the approved paste/copy-back operation was actually performed, the raw retrieved content was saved for that trial, and the required metadata and evidence are present. A completed trial can still have failed decoding or failed exact recovery; those are measured platform results, not reasons to replace the raw result or automatically change the trial status.

A trial is `failed` when the platform operation itself failed or was blocked after the failure was observed and documented, while preserving the raw result that was actually obtained and the required evidence. Do not substitute expected plaintext for a failed recovery. A `ready_for_manual_transfer` record, missing retrieved file, or empty retrieved file before a platform result is supplied is incomplete; do not analyze it as a finished trial.

Do not run the analyzer against an unfinished trial. Do not modify codec configuration, corpus files, protocol definitions, production logic, or any other trial record. Do not perform a second transfer using the same repetition's retrieved file.
