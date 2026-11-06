# Gmail Reproducibility Procedure

**Prepared by:** Tristan Koch  
**Date:** November 4, 2026  
**Platform:** Gmail (Google Chrome)  
**Operation:** Send email to self, then copy the message body back into the corresponding retrieved file.

## Purpose

This procedure documents how to reproduce the Week 11 Gmail paste/send-and-retrieve production-testing workflow. It is intended to allow another team member to independently repeat a trial and compare the resulting zero-width character retention and decoding outcomes.

## Prerequisites

- Access to the project repository and the prepared Week 11 Gmail production trial files.
- Access to Gmail through Google Chrome.
- The original trial's `_sent.txt` file and corresponding JSON record.
- The approved Week 11 codec and protocol configuration.
- A location to save the trial's screenshot evidence.

Use the existing prepared trial files. Do not generate a replacement encoded message or modify the original sent file.

## Reproduction

### Step 1 — Open the original sent file

Navigate to the selected Gmail trial folder and open its corresponding `_sent.txt` file.

For example:

`W11_Gmail-LA01_R1_sent.txt`

Copy the complete contents of the file to the clipboard without modifying the text.

### Step 2 — Send the message through Gmail

1. Open Gmail in Google Chrome.
2. Click **Compose**.
3. Enter your own email address as the recipient.
4. Set the subject line to the trial ID.

   Example: `W11_Gmail-LA01_R1`

5. Paste the copied contents of the `_sent.txt` file into the email body.
6. Send the email.

### Step 3 — Retrieve the sent message

1. Open the email from your Sent folder or the received copy in your Inbox.
2. Locate the message body.
3. Capture a screenshot showing the sent email and save it in the corresponding trial's `evidence` folder.
4. Select the complete message body and press `Ctrl + C` to copy it.

Do not manually modify, repair, or normalize the retrieved content.

### Step 4 — Save the retrieved content

1. Return to the corresponding Gmail trial folder in VS Code.
2. Open the matching `_retrieved.txt` file.

   Example: `W11_Gmail-LA01_R1_retrieved.txt`

3. Paste the copied message body into the file.
4. Save the file using UTF-8 encoding, preserving the retrieved content and line endings.

### Step 5 — Update the trial JSON record

Open the corresponding trial JSON record and update the following fields:

- `status`: Set to `completed` after the transfer and retrieval have been performed.
- `tester`: Enter the name of the person performing the reproduction.
- `timestamp_utc`: Generate and enter the current UTC timestamp.
- `evidence_paths`: Add the relative path to the screenshot captured during the trial.

To generate the timestamp in PowerShell:

```powershell
(Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
```

For example, an evidence path should reference the actual screenshot file inside the trial's evidence folder, rather than the folder itself.

Save the JSON record after updating these fields.

### Step 6 — Run the trial analyzer

After saving the retrieved file and updating the JSON record, run the analyzer for the selected trial.

Example:

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Gmail/W11_Gmail-LA01_R1/W11_Gmail-LA01_R1.json
```

The analyzer measures and reports:

- Sent and retrieved zero-width character counts.
- Lost zero-width characters.
- Zero-width character retention percentage.
- Decoder success or failure.
- Recovered secret.
- Exact-match result.
- Decoder errors and applicable failure category.
- Trial validation status.

Review the output and confirm that the analyzer completed successfully and that the results were saved to the trial record.

## Reproducibility Notes

- Each repetition must be performed as an independent send-and-retrieve operation.
- Use the matching original `_sent.txt` and `_retrieved.txt` files for each trial.
- Do not reuse retrieved content from another repetition.
- Do not manually repair or alter retrieved text to improve recovery results.
- Preserve the original trial evidence and analyzer results.
- Record the browser and operating-system versions used during reproduction.

The purpose of this procedure is to determine whether another tester can reproduce the Gmail results under the same approved conditions and observe similar zero-width character retention and decoding behavior.