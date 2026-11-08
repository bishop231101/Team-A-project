# Week 12 Baseline vs. Hamming Comparative Experiment

This report was generated from the individual trial JSON records.
The experiment uses four corpus messages, two modes, five conditions,
and three deterministic repetitions per combination (120 trials total).

## Seed pairs

| Repetition | Bit seed | Deletion seed |
|---:|---:|---:|
| R1 | 481201 | 481202 |
| R2 | 481211 | 481212 |
| R3 | 481221 | 481222 |

Bit targets are frame byte 9, bit 1 for single-bit corruption, and
frame byte 9, bits 1 and 5 for double-bit corruption. Targets are
mapped to representation-specific physical positions. These logical targets
remain fixed across repetitions R1, R2, and R3.

Deletion eligibility includes ZERO and ONE symbols, including Hamming
parity symbols, and excludes separators and the two-symbol Hamming prefix.
Baseline and Hamming use the same requested deletion percentages
(approximately 1% and 5%) and the same repetition-specific deletion seed for
each paired trial. Their actual deleted-symbol counts and physical positions
may differ because the modes have different encoded layouts and eligible
deletion populations. The deletion patterns vary by seed across repetitions.
Requested deletion counts use nearest-integer half-up rounding.

## Outcome totals

- Total trials: 120
- successful_recovery: 36
- detected_failure: 84
- undetected_error: 0

Unexpected execution errors are kept separate from decoder outcomes.
To reproduce the experiment, run the command documented in the methodology file.
