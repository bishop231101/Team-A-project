# Week 11 Official Gmail Production Summary

## Scope and status

This summary covers the 24 official Week 11 Gmail production trials: eight approved corpus messages, three repetitions per message, and one Gmail send-and-retrieve operation per repetition. The approved repetition policy was `reuse_encoded_input`: each corpus message was encoded once, then the identical encoded input was used for R1–R3. Each repetition remained an independent trial.

All 24 trial records were present, completed, and passed analyzer validation. Their validation checks reported no errors, and their terminal metadata and evidence references were valid.

- `status`: `completed`
- `analysis_status`: `completed`
- `analysis_errors`: an empty list
- valid recorded terminal metadata and evidence references

These are record-validation results. They do not mean that the hidden secret was recovered. In the recorded measurements, all 24 trials had `decoder_returned: false`, `exact_match: false`, and `recovered_secret: null`.

## Recorded measurements by corpus message

The sent and retrieved character tuples below are ordered U+200B / U+200C / U+200D. The values were identical across R1, R2, and R3 for each corpus message.

| Category | Corpus | Repetitions | Sent tuple | Retrieved tuple | Sent total | Retrieved total | Retention | Decoder / exact match |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Short ASCII | SA01 | R1–R3 | 84 / 52 / 16 | 0 / 52 / 16 | 152 | 68 | 44.74% | 0/3 / 0/3 |
| Short ASCII | SA02 | R1–R3 | 104 / 64 / 20 | 0 / 64 / 20 | 188 | 84 | 44.68% | 0/3 / 0/3 |
| Short Unicode | SU01 | R1–R3 | 79 / 57 / 16 | 0 / 57 / 16 | 152 | 73 | 48.03% | 0/3 / 0/3 |
| Short Unicode | SU02 | R1–R3 | 85 / 59 / 17 | 0 / 59 / 17 | 161 | 76 | 47.20% | 0/3 / 0/3 |
| Long ASCII | LA01 | R1–R3 | 838 / 698 / 191 | 0 / 18 / 7 | 1,727 | 25 | 1.45% | 0/3 / 0/3 |
| Long ASCII | LA02 | R1–R3 | 1,166 / 978 / 267 | 0 / 17 / 8 | 2,411 | 25 | 1.04% | 0/3 / 0/3 |
| Long Unicode | LU01 | R1–R3 | 615 / 441 / 131 | 0 / 18 / 7 | 1,187 | 25 | 2.11% | 0/3 / 0/3 |
| Long Unicode | LU02 | R1–R3 | 656 / 624 / 159 | 0 / 18 / 7 | 1,439 | 25 | 1.74% | 0/3 / 0/3 |

`Decoder / exact match` reports any successful decoder outcomes and exact recovered-secret matches out of the three repetitions.

## Category totals

Retention in this table is the category's total retrieved zero-width count divided by its total sent zero-width count.

| Category | Trials | Sent total | Retrieved total | Retention | Decoder successes | Exact matches | Failure category |
|---|---:|---:|---:|---:|---:|---:|---|
| Short ASCII | 6 | 1,020 | 456 | 44.71% | 0/6 | 0/6 | `structural_corruption` |
| Short Unicode | 6 | 939 | 447 | 47.60% | 0/6 | 0/6 | `structural_corruption` |
| Long ASCII | 6 | 12,414 | 150 | 1.21% | 0/6 | 0/6 | `structural_corruption` |
| Long Unicode | 6 | 7,878 | 150 | 1.90% | 0/6 | 0/6 | `structural_corruption` |
| **Overall** | **24** | **22,251** | **1,203** | **5.41%** | **0/24** | **0/24** | **24 structural-corruption results** |

## Zero-width retention pattern

Across all 24 records, the aggregate sent/retrieved counts were:

| Character | Sent | Retrieved | Retention |
|---|---:|---:|---:|
| U+200B | 10,881 | 0 | 0.00% |
| U+200C | 8,919 | 909 | 10.19% |
| U+200D | 2,451 | 294 | 12.00% |

In these recorded Gmail retrievals, U+200B was absent from every retrieved file. U+200C and U+200D were fully retained in the short ASCII and short Unicode trials, matching their original sent counts. In the long ASCII and long Unicode trials, only small portions of these characters remained. This summary reports the observed pattern only; it does not infer why Gmail removed or altered particular characters.

## Decoder failures

All 24 trials recorded the same decoder result:

- Failure category: `structural_corruption`
- Decoder error: `payload contains an incomplete or malformed byte block`
- `decoder_returned`: `false`
- `exact_match`: `false`
- `recovered_secret`: `null`

The records therefore document valid, completed manual Gmail trials with measured platform results, but no successful secret recovery.

## Methodology

The Gmail sends, retrievals, and evidence collection were performed manually using the approved Gmail guide. The raw retrieved body for each repetition was preserved in that trial's `_retrieved.txt` file. The analyzer compared sent and retrieved U+200B/U+200C/U+200D counts, calculated total-count retention, attempted decoding, recorded decoder errors and failure categories, and recorded exact recovered-secret comparison results in each trial JSON record.

Week 10 preliminary feasibility testing remains separate and is not included in these 24 official results.

## Source records and evidence

Reviewers can inspect the original data under [`production_testing/Gmail/`](production_testing/Gmail/). Each trial has its own record, sent text, retrieved text, and evidence directory:

- Short ASCII: `production_testing/Gmail/W11_Gmail-SA01_R{1,2,3}/` and `W11_Gmail-SA02_R{1,2,3}/`
- Short Unicode: `production_testing/Gmail/W11_Gmail-SU01_R{1,2,3}/` and `W11_Gmail-SU02_R{1,2,3}/`
- Long ASCII: `production_testing/Gmail/W11_Gmail-LA01_R{1,2,3}/` and `W11_Gmail-LA02_R{1,2,3}/`
- Long Unicode: `production_testing/Gmail/W11_Gmail-LU01_R{1,2,3}/` and `W11_Gmail-LU02_R{1,2,3}/`

The approved manifest is [`production_manifest.json`](production_manifest.json). The workflow and interpretation references reviewed were [`README.md`](README.md), [`guides/gmail.md`](guides/gmail.md), [`production_workflow.py`](production_workflow.py), [`src/week11_production.py`](../../src/week11_production.py), and [`src/failure_analysis.py`](../../src/failure_analysis.py).

## Data gaps and limitations

- All 24 expected Gmail trial records were found and their referenced evidence files were present and non-empty.
- No `production_testing/analysis/batch_analysis.json` was present at review time. The tables above were therefore derived directly from the 24 individual JSON records and their `measured_results` fields; no missing batch file was silently reconstructed.
- The summary does not make causal claims about Gmail's handling of the zero-width characters.
