# Week 12 Comparative Experiment Methodology

The full experiment compares Baseline `encode_secret(secret)` with Hamming
`encode_secret(secret, error_correction="hamming")` for SA01, SU01, LA01, and
LU01. Each message/mode/condition combination has three deterministic
repetitions, producing 120 individual trial records. The experiment is
automated locally and does not represent a statistically large sample.

## Conditions and logical corruption targets

Each repetition includes no corruption, one-bit corruption, two-bit
corruption, approximately 1% deletion, and approximately 5% deletion.

- Single-bit target: frame byte 9, data bit 1, zero-based.
- Double-bit targets: frame byte 9, data bits 1 and 5, zero-based.
- Baseline and Hamming map those logical targets to their own physical symbol
  positions.

## Seed pairs

| Repetition | Bit seed | Deletion seed |
|---:|---:|---:|
| R1 | 481201 | 481202 |
| R2 | 481211 | 481212 |
| R3 | 481221 | 481222 |

The approved logical bit targets are fixed across all repetitions. Both the bit
seed and deletion seed are recorded in every trial's corruption metadata.
Because the logical bit targets are fixed, the bit seed identifies the
repetition but does not select a new bit position. Repetition-specific deletion
seeds produce distinct deterministic deletion schedules where the eligible
population permits; sampling is performed independently against each mode's
eligible-symbol list, while corresponding modes use the same seed and rate.

## Deletion methodology

Only ZERO and ONE symbols are eligible. U+200D separators and the two-symbol
Hamming prefix are excluded from the denominator. Hamming parity symbols remain
eligible. The requested removal count is calculated as
`floor(eligible_count * requested_percentage + 0.5)`. Each trial records the
eligible count before and after deletion, target count, actual affected count,
actual percentage, seed, and physical deletion locations.

## Outcomes and verification

Each trial is classified as exactly one of:

- `successful_recovery`: decoder returned the exact expected secret.
- `detected_failure`: decoder did not return a message.
- `undetected_error`: decoder returned a nonexact message.

Unexpected programming or analysis exceptions are not converted into decoder
outcomes. They propagate and must be investigated separately. The runner first
validates the in-memory 120-trial matrix, including seed pairs, affected-symbol
counts, deletion metadata, and Baseline/Hamming logical target agreement. It
then writes individual records, reloads those records, and derives
`summary.json` from the reloaded records.

Run from the repository root with:

```powershell
python tests/week12_testing/comparative_experiment.py
```

Outputs are written to
`tests/week12_testing/comparative_experiment_output/`. The runner refuses to
overwrite a non-empty output directory. The directory contains 120 individual
JSON records, `summary.json`, and `experiment_report.md`.
