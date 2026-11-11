# Week 13 Chrome Browser Console Production-Testing Command Guide

This temporary guide is for the 24 official Week 11 Google Chrome Browser Console production trials. The trial records use platform `Browser Console`, platform directory `Google_Chrome_Browser_Console`, and operation `paste_and_copy_back`.

## 1. UTC timestamp

Run this in PowerShell when the trial is performed:

```powershell
(Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
```

## 2. Trial procedure

1. Select the matching trial JSON record and `_sent.txt` file for the corpus ID and repetition. Use the exact prepared encoded payload; do not regenerate, retype, trim, normalize, or repair it.
2. Confirm that the browser is Google Chrome, record the exact version from `chrome://settings/help` and the operating system, and start from a fresh tab with DevTools opened through the normal Chrome UI.
3. Select the **Console** panel and leave an empty Console prompt ready. Paste the complete encoded payload as text only. Do not press Enter, execute it, wrap it in JavaScript, paste a script, disable security, or bypass a self-XSS warning.
4. If Chrome cannot safely support the documented unexecuted paste-and-copy-back operation, stop and document the limitation rather than inventing a workaround.
5. If the paste is accepted, manually select and copy the complete unexecuted text. Exclude the prompt marker, Console output, warnings, and unrelated content.
6. Save the copied content unchanged to the matching `_retrieved.txt` file. Capture the required Console evidence in that trial's `evidence/` directory.
7. Update only the selected JSON record with the tester, UTC timestamp, and evidence file path. Run the matching analyzer command below from the repository root and inspect the resulting JSON record.

## 3. Analyzer commands

The analyzer reads each trial's sent and retrieved paths from its JSON record. Run a command only after the corresponding retrieved file contains the raw Console result.

### SA01

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Google_Chrome_Browser_Console/W11_Chrome_Browser_Console-SA01_R1/W11_Chrome_Browser_Console-SA01_R1.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Google_Chrome_Browser_Console/W11_Chrome_Browser_Console-SA01_R2/W11_Chrome_Browser_Console-SA01_R2.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Google_Chrome_Browser_Console/W11_Chrome_Browser_Console-SA01_R3/W11_Chrome_Browser_Console-SA01_R3.json
```

### SA02

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Google_Chrome_Browser_Console/W11_Chrome_Browser_Console-SA02_R1/W11_Chrome_Browser_Console-SA02_R1.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Google_Chrome_Browser_Console/W11_Chrome_Browser_Console-SA02_R2/W11_Chrome_Browser_Console-SA02_R2.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Google_Chrome_Browser_Console/W11_Chrome_Browser_Console-SA02_R3/W11_Chrome_Browser_Console-SA02_R3.json
```

### SU01

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Google_Chrome_Browser_Console/W11_Chrome_Browser_Console-SU01_R1/W11_Chrome_Browser_Console-SU01_R1.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Google_Chrome_Browser_Console/W11_Chrome_Browser_Console-SU01_R2/W11_Chrome_Browser_Console-SU01_R2.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Google_Chrome_Browser_Console/W11_Chrome_Browser_Console-SU01_R3/W11_Chrome_Browser_Console-SU01_R3.json
```

### SU02

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Google_Chrome_Browser_Console/W11_Chrome_Browser_Console-SU02_R1/W11_Chrome_Browser_Console-SU02_R1.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Google_Chrome_Browser_Console/W11_Chrome_Browser_Console-SU02_R2/W11_Chrome_Browser_Console-SU02_R2.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Google_Chrome_Browser_Console/W11_Chrome_Browser_Console-SU02_R3/W11_Chrome_Browser_Console-SU02_R3.json
```

### LA01

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Google_Chrome_Browser_Console/W11_Chrome_Browser_Console-LA01_R1/W11_Chrome_Browser_Console-LA01_R1.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Google_Chrome_Browser_Console/W11_Chrome_Browser_Console-LA01_R2/W11_Chrome_Browser_Console-LA01_R2.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Google_Chrome_Browser_Console/W11_Chrome_Browser_Console-LA01_R3/W11_Chrome_Browser_Console-LA01_R3.json
```

### LA02

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Google_Chrome_Browser_Console/W11_Chrome_Browser_Console-LA02_R1/W11_Chrome_Browser_Console-LA02_R1.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Google_Chrome_Browser_Console/W11_Chrome_Browser_Console-LA02_R2/W11_Chrome_Browser_Console-LA02_R2.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Google_Chrome_Browser_Console/W11_Chrome_Browser_Console-LA02_R3/W11_Chrome_Browser_Console-LA02_R3.json
```

### LU01

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Google_Chrome_Browser_Console/W11_Chrome_Browser_Console-LU01_R1/W11_Chrome_Browser_Console-LU01_R1.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Google_Chrome_Browser_Console/W11_Chrome_Browser_Console-LU01_R2/W11_Chrome_Browser_Console-LU01_R2.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Google_Chrome_Browser_Console/W11_Chrome_Browser_Console-LU01_R3/W11_Chrome_Browser_Console-LU01_R3.json
```

### LU02

```powershell
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Google_Chrome_Browser_Console/W11_Chrome_Browser_Console-LU02_R1/W11_Chrome_Browser_Console-LU02_R1.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Google_Chrome_Browser_Console/W11_Chrome_Browser_Console-LU02_R2/W11_Chrome_Browser_Console-LU02_R2.json
python tests/week11_testing/production_workflow.py analyze-trial --root tests/week11_testing/production_testing --record tests/week11_testing/production_testing/Google_Chrome_Browser_Console/W11_Chrome_Browser_Console-LU02_R3/W11_Chrome_Browser_Console-LU02_R3.json
```

Review the analyzer output and the matching JSON after each run. Do not modify the original sent file or repair the retrieved text.
