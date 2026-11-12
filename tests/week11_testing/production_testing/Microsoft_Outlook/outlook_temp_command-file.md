# Week 13 Microsoft Outlook Production-Testing Command Guide

This temporary guide is for the 24 official Week 11 Microsoft Outlook production trials. Use the prepared trial files under `tests/week11_testing/production_testing/Microsoft_Outlook/`. Each repetition is an independent manual `send_and_retrieve` operation using the matching original encoded input.

## 1. UTC timestamp

Run this in PowerShell when the trial is performed:

```powershell
(Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
```

## 2. Trial procedure

1. Select the matching trial JSON record and its `_sent.txt` file for the corpus ID and repetition. Confirm the record uses platform `Microsoft Outlook`, platform directory `Microsoft_Outlook`, and operation `send_and_retrieve`.
2. Open Outlook manually and confirm the approved account and exact recipient/destination. Record any Outlook/OS version or format behavior that is observed; do not guess unrecorded settings.
3. Copy the complete original encoded `_sent.txt` contents, including visible cover text, line endings, and invisible characters. Paste and send it without retyping, trimming, normalizing, shortening, splitting, or repairing the payload.
4. Open the delivered message through the approved retrieval path. Copy only the complete message body; exclude headers, quoted replies, signatures, and unrelated content.
5. Save the retrieved content unchanged to the matching `_retrieved.txt` file. Preserve the raw result and do not substitute the expected plaintext.
6. Capture the required Outlook evidence screenshot in that trial's `evidence/` directory. Update only the selected JSON record with the tester, UTC timestamp, and evidence file path.
7. Run the matching analyzer command below from the repository root and confirm that the resulting JSON contains the analyzer measurements and completed analysis fields.

## 3. Analyzer commands

The analyzer reads each trial's sent and retrieved paths from its JSON record. Run a command only after the corresponding retrieved file contains the raw Outlook result.

### SA01

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Outlook/W11_Outlook-SA01_R1/W11_Outlook-SA01_R1.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Outlook/W11_Outlook-SA01_R2/W11_Outlook-SA01_R2.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Outlook/W11_Outlook-SA01_R3/W11_Outlook-SA01_R3.json
```

### SA02

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Outlook/W11_Outlook-SA02_R1/W11_Outlook-SA02_R1.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Outlook/W11_Outlook-SA02_R2/W11_Outlook-SA02_R2.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Outlook/W11_Outlook-SA02_R3/W11_Outlook-SA02_R3.json
```

### SU01

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Outlook/W11_Outlook-SU01_R1/W11_Outlook-SU01_R1.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Outlook/W11_Outlook-SU01_R2/W11_Outlook-SU01_R2.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Outlook/W11_Outlook-SU01_R3/W11_Outlook-SU01_R3.json
```

### SU02

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Outlook/W11_Outlook-SU02_R1/W11_Outlook-SU02_R1.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Outlook/W11_Outlook-SU02_R2/W11_Outlook-SU02_R2.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Outlook/W11_Outlook-SU02_R3/W11_Outlook-SU02_R3.json
```

### LA01

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Outlook/W11_Outlook-LA01_R1/W11_Outlook-LA01_R1.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Outlook/W11_Outlook-LA01_R2/W11_Outlook-LA01_R2.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Outlook/W11_Outlook-LA01_R3/W11_Outlook-LA01_R3.json
```

### LA02

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Outlook/W11_Outlook-LA02_R1/W11_Outlook-LA02_R1.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Outlook/W11_Outlook-LA02_R2/W11_Outlook-LA02_R2.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Outlook/W11_Outlook-LA02_R3/W11_Outlook-LA02_R3.json
```

### LU01

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Outlook/W11_Outlook-LU01_R1/W11_Outlook-LU01_R1.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Outlook/W11_Outlook-LU01_R2/W11_Outlook-LU01_R2.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Outlook/W11_Outlook-LU01_R3/W11_Outlook-LU01_R3.json
```

### LU02

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Outlook/W11_Outlook-LU02_R1/W11_Outlook-LU02_R1.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Outlook/W11_Outlook-LU02_R2/W11_Outlook-LU02_R2.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Microsoft_Outlook/W11_Outlook-LU02_R3/W11_Outlook-LU02_R3.json
```

Review the analyzer output and the matching JSON after each run. Do not modify the original sent file or repair the retrieved text to improve the result.
