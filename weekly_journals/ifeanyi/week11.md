# Week 11 Individual Journal — Ifeanyi Emeka

**Course:** CS481 — Capstone Project  
**Role:** Team 1 Leader  
**Reporting period:** October 26–November 1, 2026  
**Status:** Week 11 work documented; remaining project testing continues in Week 12

## 1. Work Completed and Leadership

I coordinated Team 1's Week 11 priorities, reviewed the semester plan and Week 10 carryover tasks, prepared Monday's meeting minutes, and communicated responsibilities to Tristan Koch and Henry Smith. I maintained the Week 11 data-quality audit and weekly report, monitored testing progress, and reviewed pull requests before approving merges. Our Friday meeting reviewed completed implementation work, Gmail testing progress, verification requirements, and Week 12 responsibilities.

## 2. Independent Baseline Verification — October 27

I checked `tests/fixtures/week9_corpus.json` using Python and confirmed that all eight corpus entries contained the required fields (`id`, `category`, `text`, `sha256`), had unique identifiers, and matched their recorded SHA-256 hashes. I also ran `python -m pytest -q`: **43 tests and 132 subtests passed**, with no reported failures. These results verified corpus integrity and the existing local test baseline, not external platform compatibility.

**Evidence:** `docs/week11_data_quality_audit.md`.

## 3. Production Workflow Review — PR #24

I reviewed Tristan's production workflow, including preparation of **168 planned trial records** (seven approved workflows × eight corpus messages × three repetitions), evidence organization, metadata validation, and safeguards against confusing incomplete trials with genuinely empty retrieved messages. I independently ran the workflow tests: **56 tests and 132 subtests passed**. I approved and merged PR #24 (merge commit `8646a48`) and authorized Gmail production testing. The 168 prepared records were **not** 168 completed platform operations.

## 4. Hamming SECDED Review — PR #25, October 30

I reviewed Henry's optional Hamming SECDED implementation, documentation, and tests. My independent verification included **54 tests and 148 subtests passed** in the full suite, **28 tests and 132 subtests passed** in the existing codec regression tests, and **five successful targeted checks**. The checks covered Unicode round-trip, single-bit correction, double-bit rejection, Gmail-style stripping, and Word-style stripping. The stripping cases demonstrated safe rejection of unrecoverable data, **not successful recovery**. After verification, PR #25 was merged (merge commit `3d311e7`).

## 5. Gmail Production Testing Review — PR #26

I monitored Tristan's Gmail testing, initially documenting the first 12 reported trials and then reviewing the final submission of **24 of 24 planned Gmail trials**. I examined the trial-record structure, analyzer outputs, screenshot references, and the distinction between a valid analysis record and successful secret recovery. The reviewed Gmail evidence showed substantial loss of zero-width characters and failed recovery in the representative long-ASCII trial: **25 of 1,727 zero-width characters retained (about 1.45%)**, with a structural-corruption decoder error. I reviewed the submission and merged PR #26 into `main`.

Tristan confirmed that repetitions R1–R3 were separate Gmail send-and-retrieve operations using the same prepared input. Matching SHA-256 hashes across repetitions were documented as an issue for further investigation; identical hashes alone do not establish whether the operations were independent or whether the retrieved outputs were correct. I did not treat analyzer validation as proof of successful decoding.

**Evidence:** PR #26; `tests/week11_testing/production_testing/Gmail/` (trial records, sent/retrieved text, and screenshots); `reports/weekly_report_11.md`.

## 6. Challenges and Lessons Learned

Week 10 carryover delayed the planned baseline analysis. I learned to distinguish prepared trial templates, completed platform operations, valid analysis records, and successful message recovery. Reviewing raw evidence and reproducible calculations is necessary before accepting compatibility conclusions. I also learned that bit-error correction has limits when platforms delete required zero-width characters entirely.

## 7. Individual Contribution and Progress Against Plan

My Week 11 contributions included team coordination, two meeting records, corpus integrity checks, independent test execution, review and merge of PRs #24, #25, and #26, tracking Gmail evidence concerns, and consolidation of the weekly report with screenshots and explanations. Gmail's **24 planned trials were completed**, but the complete **168-trial** cross-platform dataset, statistical analysis, and final compatibility matrix were **not** completed during Week 11.

## 8. Next Steps

Complete and verify production testing for the remaining approved platforms; investigate matching hashes and confirm trial provenance where necessary; finish the cross-platform compatibility matrix and statistical analysis; and evaluate the optional Hamming mode against observed platform corruption while documenting its limitations. Continue individual journals and Monday/Friday meeting records.

**Week 11 conclusion:** I completed the leadership, verification, review, and reporting tasks described above. The production workflow, Hamming implementation, and Gmail trial submission were merged, while broader platform testing and final analysis remain outstanding.
