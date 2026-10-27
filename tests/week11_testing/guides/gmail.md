# Week 11 Gmail — Send and Retrieve Message

This is the manual guide for the approved Gmail send-and-retrieve combination. It is not browser automation and must not be used with the Week 10 preliminary files.

## Before the transfer

1. Confirm the record uses the approved `reuse_encoded_input` policy. The same corpus input is sent three times, but each repetition is a separate manual transfer.
2. Confirm the trial record is a Week 11 ID such as `W11_Gmail-SA01_R1` and that its local round trip passed.
3. Open that trial's `_sent.txt` in a plain-text editor. Copy the complete file contents exactly, including visible cover text and invisible characters. Do not retype, trim, normalize, or repair it.
4. Record the Gmail/browser and operating-system versions and the UTC start time.

## Manual Gmail operation

1. In Gmail, create a fresh message to the approved test account or recipient specified by the team. Do not reuse an earlier message or paste Week 10 evidence.
2. Paste the complete `_sent.txt` contents into the message body without editing or formatting it.
3. Capture the required send evidence without exposing credentials or unrelated private mail, then send manually.
4. Open the delivered message through the approved retrieval path. Copy only the complete delivered body. Do not include Gmail chrome, quoted unrelated text, signatures, or a prompt marker.
5. Paste that clipboard content unchanged into the trial's UTF-8 `_retrieved.txt`. Preserve line endings as captured. Do not inspect-and-repair invisible characters. Never use another repetition's retrieved file.
6. Save the screenshot or other evidence in the trial directory and add its relative path to the trial record.

## Analyze and record

From the repository root, run:

```powershell
python tests/week11_testing/production_workflow.py analyze-trial `
  --root tests/week11_testing/production_testing `
  --record tests/week11_testing/production_testing/Gmail/W11_Gmail-SA01_R1/W11_Gmail-SA01_R1.json
```

The command persists measurements and decoder errors in that trial's JSON record. A zero-width retention result and exact recovery result are separate measurements; Gmail failure is still a valid official result if the transfer and evidence are real.

If Gmail changes the content, blocks copying, or does not permit an exact retrieval, save the unmodified content that was actually obtained, record the limitation, and mark the trial `failed` or `blocked` according to the team's record convention. Do not create a replacement retrieved file to make decoding succeed.
