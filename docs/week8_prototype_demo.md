# Week 8 Prototype Demonstration Plan

## Purpose

Provide a short, repeatable demonstration of the current codec architecture,
integrity checks, five-copy recovery behavior, and documented recovery limit.
The demo is local and does not depend on a network connection or platform
login.

## Roles

- **Henry Smith:** technical operator and codec explanation.
- **Ifeanyi Emeka:** narrator and timekeeper.
- **Tristan Koch:** verifies displayed results and explains platform findings.

## Run command

From the repository root:

```powershell
python tests/week8_testing/run_henry_midterm_demo.py
```

## Demonstration flow

1. Identify the visible cover and synthetic secret.
2. Explain the `ZWS1 | length | payload | CRC-32` frame.
3. Show the standard encode/decode result.
4. Show that filtering the three codec characters restores the exact cover.
5. Explain five-copy majority voting and its two-symbol-per-group capacity.
6. Show successful recovery after 40% distributed alteration.
7. Show safe rejection after 45%, when the correction limit is exceeded.
8. State that repetition cannot recover a completely stripped payload.

## Expected success indicators

- All five numbered checks print `PASS`.
- `All demonstration checks passed: True` is displayed.
- The 45% example produces an explicit decoder error instead of incorrect text.

## Technical rehearsal record

- **Date:** October 8, 2026
- **Operator:** Henry Smith
- **Environment:** Local Python 3 session from the repository root
- **Result:** All five demonstration checks passed
- **Script execution time:** 0.004 seconds
- **Fallback verified:** `tests/week8_testing/henry_midterm_demo_output.txt`

This records the technical dry run. The team should still conduct its scheduled
timed rehearsal with narration and role handoffs before submitting the Midterm
Report.

## Fallback procedure

If the live terminal demonstration cannot run, open
`tests/week8_testing/henry_midterm_demo_output.txt`. It contains the saved
output from a verified run. The architecture and results can still be explained
without network access.

## Reset and troubleshooting

- Confirm the terminal is in the repository root.
- Confirm Python 3 is available with `python --version`.
- Rerun the command; it creates no persistent data and requires no reset.
- If the terminal font does not display invisible characters, use the printed
  codec-character counts rather than trying to display the payload directly.
- If a platform example fails, continue with the local demo and saved fallback.

## Evidence to capture

Capture one screenshot containing the five `PASS` results, the safe rejection
message, and `All demonstration checks passed: True`. Link and explain it in
the Midterm Report.
