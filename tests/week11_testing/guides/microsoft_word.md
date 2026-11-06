# Week 11 Microsoft Word — Save, Reopen, and Retrieve

This is the manual guide for the approved Week 11 Microsoft Word `save_reopen_and_retrieve` operation. It applies only to official records under `tests/week11_testing/production_testing/Microsoft_Word/`; do not use the Week 10 preliminary files.

The production trials measure what Microsoft Word actually preserves. Do not assume that Word preserves zero-width characters, and do not claim a retention or decoding result before the corresponding trial has been performed and analyzed.

## Before the transfer

1. Select one existing trial folder under `tests/week11_testing/production_testing/Microsoft_Word/`. Use the folder and JSON record with the same trial ID, such as `W11_Word-SA01_R1`.
2. Verify the record fields: `trial_id`, `corpus_id`, `repetition`, `platform` (`Microsoft Word`), `platform_directory` (`Microsoft_Word`), `operation` (`save_reopen_and_retrieve`), and the recorded sent/retrieved paths.
3. Confirm `local_validation.passed` and `local_validation.exact_round_trip` are both `true`. This checks the codec and prepared input only; it is not a Word result.
4. Confirm the trial's own `_sent.txt`, `_retrieved.txt`, and `evidence/` paths exist. The Week 11 policy is `reuse_encoded_input`: the same encoded corpus input is reused across repetitions, but every repetition has an independent manual transfer, retrieved file, JSON record, and evidence.
5. Record the actual Microsoft Word version, Word document format used for the saved document, operating-system version, and UTC start time. Use the required timestamp format `YYYY-MM-DDTHH:mm:ssZ`.

## Prepare and open the encoded message

1. From the repository root, locate the selected trial's `_sent.txt` using the path already stored in its JSON record. Open it in a plain-text editor or use the exact file path from the record.
2. Copy the complete file contents exactly, including visible cover text, line endings, separators, and invisible zero-width characters. Do not retype, trim, normalize, repair, or format the content.
3. Do not regenerate the input for an individual repetition. Use the prepared Week 11 `_sent.txt` belonging to the selected trial so its recorded `input_sha256` remains the source-of-truth check.

## Manual Microsoft Word operation

1. Open Microsoft Word manually and create a new blank document.
2. Paste the complete encoded message into the blank document without editing, reformatting, or replacing any characters. Do not use macros, scripts, automation, or a conversion step that changes the content.
3. Capture the required Word screenshot showing the document and transferred content without exposing unrelated private information. Save it under the selected trial's `evidence/` directory, using a name such as `W11_Word-SA01_R1.png`.
4. Save the Word document in the selected document format and record the format and save location. Do not reuse another repetition's document.
5. Close Word fully, then reopen the saved document manually. Record whether Word displays a conversion, compatibility, encoding, repair, or format prompt. Do not accept an option that intentionally changes the test content without recording the deviation.
6. Select only the message content. Do not include headers, footers, paragraph marks, comments, unrelated text, or Word interface content. Copy the complete retrieved text after reopening.
7. Paste the copied content unchanged into the selected trial's `_retrieved.txt`. Save it as UTF-8 while preserving the captured line endings. Preserve empty, truncated, or corrupted output exactly as retrieved. Do not manually repair or normalize zero-width characters.

If Word forces formatting or editing that prevents an exact retrieval, preserve the raw result that was actually obtained, record the limitation, and do not substitute the expected plaintext.

## Update the record and analyze

After the manual save, close, reopen, retrieval, and `_retrieved.txt` save:

1. Update only the selected JSON record. Set `status` to `completed` when the approved Word operation and retrieval file have been completed. Set it to `failed` only when the Word operation itself failed or was blocked after the failure was documented. Set `tester` to `Tristan Koch` and set `timestamp_utc` to the current UTC timestamp.
2. Add the Word document screenshot path to `evidence_paths` using the production-root-relative convention, for example `Microsoft_Word/W11_Word-SA01_R1/evidence/W11_Word-SA01_R1.png`.
3. From the repository root, run the analyzer for the exact selected record:

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Word/W11_Word-SA01_R1/W11_Word-SA01_R1.json
```

4. Review the analyzer output and the updated JSON. It records separate `U+200B`, `U+200C`, and `U+200D` counts, totals, count-based retention, retention above 100% flags, decoder return/error, exact recovery, and any failure category. Record Word's version, document format, save/reopen behavior, prompts, and relevant observations in the `notes` array.
5. Capture a screenshot of the analyzer terminal output and save it in the same trial's `evidence/` directory, using a name such as `W11_Word-SA01_R1_terminal.png`.
6. Add the terminal screenshot path to `evidence_paths`, save the JSON record, and run the same analyzer command again. This final run verifies the record after the evidence update.

## Completed, failed, and incomplete trials

A trial is `completed` when the approved Word save/close/reopen/retrieve operation was performed, the raw retrieved text was saved for that trial, and the required metadata and evidence are present. A completed trial may still show zero retention, a decoder failure, or failed exact recovery. Those are valid measured platform outcomes.

A trial is `failed` when the Word operation itself failed or was blocked and the failure, raw result if any, and evidence were preserved. A `ready_for_manual_transfer` record, missing retrieved file, or empty retrieved file before a platform result is supplied is incomplete and must not be analyzed as a finished trial.

Do not replace a failed or corrupted retrieval with the expected plaintext. Do not reuse retrieved files between repetitions. Do not run the analyzer until the selected trial has a real raw result and terminal metadata.

## Common limitations and troubleshooting

- Word may remove, transform, or fail to preserve zero-width characters during paste, save, close, reopen, or copy. Measure the result; do not assume success or failure in advance.
- A Word format or compatibility prompt may change the document. Record the prompt and selected option in the trial notes.
- If the retrieved text differs from the sent text, save the exact retrieved content and let the analyzer report retention and decoding outcomes.
- If the document cannot be reopened or the text cannot be copied without forced editing, stop the trial, preserve the available raw result and evidence, and record the blocker.
- Keep Word screenshots and analyzer screenshots inside that trial's `evidence/` directory and reference individual files, not only the directory, in `evidence_paths`.
- Keep all Week 11 artifacts separate from `tests/week10_testing/preliminary_testing/Microsoft_Word/`. Do not modify codec configuration, corpus fixtures, production logic, or protocol files.
