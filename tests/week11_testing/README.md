# Week 11 Official Baseline Production Testing

This directory is for the approved Week 11 baseline dataset only. It is separate from `tests/week10_testing/preliminary_testing/`; no Week 10 file or result is an official production trial.

The approved scope is 7 platform-operation combinations × 8 frozen corpus messages × 3 repetitions = 168 planned trials. The fixed baseline is `recovery_mode=False`, cover text `Team 1 compatibility test.`, and codec commit `4134cec1d23be3ae7069440a3718e09069922bdc`.

## Week 11 repetition-policy clarification confirmed by the team lead

Ifeanyi, the team lead, confirmed the Week 11 repetition policy:

- Encode each approved corpus message once with the approved configuration.
- Reuse that identical encoded input for all three repetitions across every applicable platform-operation combination.
- Treat each transmission as a separate trial with its own retrieved text, JSON record, evidence, and analysis.
- Use the recorded SHA-256 input hash to verify that the encoded inputs are identical across repetitions and platforms.

The manifest records this policy as `reuse_encoded_input`. Reusing the encoded input does not merge repetitions: every transmission still requires an independent manual transfer and independent result.

## Commands

From the repository root in PowerShell:

Prepare the existing platform folders, without using `tests/week10_testing`:

```powershell
python tests/week11_testing/production_workflow.py prepare `
  --root tests/week11_testing/production_testing
```

The command encodes each corpus ID once, stores canonical inputs under `production_testing/canonical_inputs/`, and copies the identical bytes to all applicable trial `_sent.txt` files. It creates empty UTF-8 `_retrieved.txt` files, individual JSON records, and each trial's `evidence/` folder. It performs no platform operation and creates no platform result. Preparation stops before writing if an expected trial folder or canonical input already exists.

The existing platform folders are `Gmail`, `Discord`, `Microsoft_Word`, `Microsoft_Outlook`, `Telegram_Web`, `Notepad++`, and `Google_Chrome_Browser_Console`. Each contains 24 folders such as `Gmail/W11_Gmail-SA01_R1/`.

For each trial, use the matching platform guide and a fresh manual transfer. Save the platform result exactly as retrieved to that trial's `_retrieved.txt`. Preserve UTF-8 and line endings; do not trim, normalize, repair, or retype invisible characters. Record the application/browser and OS versions, manual steps, UTC timestamp, tester, and evidence paths in that trial's record. Mark the record `completed` for a completed transfer or `failed` for an actual platform failure. A missing or empty retrieved file, or a `ready_for_manual_transfer` record, is incomplete.

Analyze one completed trial after its record has been updated:

```powershell
python tests/week11_testing/production_workflow.py analyze-trial `
  --root tests/week11_testing/production_testing `
  --record tests/week11_testing/production_testing/Gmail/W11_Gmail-SA01_R1/W11_Gmail-SA01_R1.json
```

Analyze all records in a manifest:

```powershell
python tests/week11_testing/production_workflow.py analyze-batch `
  --root tests/week11_testing/production_testing `
  --manifest tests/week11_testing/production_manifest.json
```

Batch analysis writes `production_testing/analysis/batch_analysis.json`. Empty retrieved files are reported as `incomplete`, not decoded and not counted as completed results. The analysis reports individual U+200B/U+200C/U+200D counts, totals, count-based retention, decoder return/error, exact recovery, and retention above 100% as an investigation flag. It never caps retention or turns missing/invalid files into successes.

## Evidence rules and failure handling

- Every official trial has a unique `W11_..._R1`, `R2`, or `R3` record and its own raw sent/retrieved paths.
- Screenshots and other evidence belong under that trial's `evidence/` directory and must be referenced by the record.
- A local round trip verifies only the codec/input setup; it is not a platform result.
- Gmail and Word failures observed in Week 10 are preliminary context only. Record any Week 11 failure as a new official trial with its own evidence.
- Stop a trial if the platform forces editing or if the exact retrieved content cannot be captured. Record the blocker; do not repair the text.
- Do not put Week 10 artifacts, WeChat artifacts, simulated retrievals, or screenshots created without an actual transfer in the official directory.
- To resume, do not rerun `prepare` over an existing root. Add only missing manual results and run analysis; if preparation stopped on a collision, inspect the existing folder and use a separately reviewed recovery plan rather than deleting or overwriting it.

The existing codec and corpus remain unchanged. The helper performs no browser or platform automation.
