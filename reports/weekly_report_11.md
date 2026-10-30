# CS481 – Team 1 Weekly Report 11

**Project:** Zero-Width Unicode Steganography with Social-Media Robustness Engineering  

**Team Leader:** Ifeanyi Emeka  

**Team Members:** Ifeanyi Emeka, Tristan Koch, Henry Smith  

**Reporting Period:** October 26 – November 1, 2026  

**Status:** In Progress – Production Workflow Merged; Official Trial Results and Error-Correction Evidence Pending

## 1. Weekly Overview

During Week 11, Team 1 is addressing unfinished Week 10 baseline testing requirements while beginning the error-correction design and implementation tasks outlined in the semester project plan.

The team is prioritizing accurate production testing, reproducible evidence, individual accountability, and timely completion of outstanding deliverables. On October 28, the team leader reviewed and merged Tristan’s PR #24, which adds the production-trial preparation and validation workflow. The prepared records are not counted as completed platform trials.

Our target is to have the work ready for review by Friday, October 30, before the Sunday submission deadline.

## 2. Milestones Achieved

### Completed

- Reviewed the Week 10 carryover requirements and Week 11 semester plan.

- Prepared Monday, October 26, meeting documentation.

- Established the Week 11 data-quality audit.

- Created the team leader's Week 11 individual journal.

- Communicated responsibilities and requested progress updates from Tristan and Henry.

- Identified outstanding production testing and error-correction requirements.
- Reviewed and merged Tristan’s PR #24 (merge commit `8646a48`) after independent automated testing.
- Verified that the updated workflow passed 56 tests and 132 subtests.
- Confirmed the workflow prepares 168 trial records without representing them as completed production trials.

### Pending Verification

- Completion of the approved 168 production trials.

- Validation of the baseline testing dataset.

- Baseline statistical analysis and updated compatibility matrix.

- Error-correction design decision and implementation.

- Automated testing and supporting evidence for the optional codec mode.

## 3. Subtasks Completed and Individual Contributions

### Ifeanyi Emeka – Team Leader

Prepared Week 11 planning and quality-assurance documentation, identified outstanding project requirements, coordinated responsibilities, and established a schedule for reviewing team contributions. Independently checked the approved eight-message corpus, executed the baseline regression suite, reviewed Tristan’s production-workflow safeguards, ran the updated automated suite, merged PR #24, and synchronized the local `main` branch. Authorized Tristan to begin official Gmail testing under the approved protocol after the merge.

Created or updated:

- `meeting_minutes/2026-10-26_week11.md`

- `docs/week11_data_quality_audit.md`

- `docs/week11_error_correction_design_review.md`

- `weekly_journals/ifeanyi/week11.md`

### Tristan Koch – Platform Testing

**Assigned work:**

- Complete baseline production testing across the seven approved platform workflows.

- Preserve raw testing files, trial logs, screenshots, and decoder results.

- Investigate observed platform failures.

- Create reproducible corruption fixtures for Week 11 experiments.

- Update testing documentation and individual journal.

**Verified Week 11 contribution:** Tristan submitted PR #24 with a guarded workflow for preparing and analyzing the approved production trials, including 168 prepared records, platform-specific organization, and validation of completion status, tester identity, UTC timestamps, and evidence references. The workflow distinguishes missing retrievals from genuinely empty completed retrievals and protects the production evidence directory. Ifeanyi independently reproduced 56 passing tests and 132 passing subtests before merging the PR.

**Current status:** Production workflow merged; official Gmail testing authorized. Completed trial counts, raw evidence, and platform results remain pending verification.

### Henry Smith – Codec Validation and Development

**Assigned work:**

- Validate incoming production testing data.

- Compare Reed–Solomon and Hamming error-correction approaches.

- Document the selected design and implementation tradeoffs.

- Develop an optional error-correction mode.

- Preserve compatibility with the baseline codec.

- Run automated and targeted tests with supporting evidence.

**Current status:** Week 11 implementation and validation results have not yet been verified.

### Team Leader Baseline Verification

On October 27, Ifeanyi independently verified the integrity of the eight-message testing corpus. All required fields were present, message identifiers were unique, and all eight SHA-256 checks passed.

Ifeanyi also executed the existing automated regression suite, which completed with 43 passing tests and 132 passing subtests, without reported failures.

These October 27 results establish a verified pre-merge baseline for subsequent testing and error-correction integration. On October 28, Ifeanyi independently ran the updated PR #24 suite, obtaining 56 passing tests and 132 passing subtests. Neither automated test run represents completion of the planned 168 production trials or validation of the proposed error-correction implementation.

**Evidence:** `docs/week11_data_quality_audit.md` and the corresponding Python and pytest terminal outputs.

## 4. Testing and Evidence

### 4.1 Approved Production Testing Scope

The approved testing protocol consists of seven platform-operation combinations, eight approved corpus messages, and three repetitions per message.

**Total planned production trials: 168.**

PR #24 prepared all 168 trial records for the approved protocol. These are templates for manual platform operations, not completed trial results. The number of completed official production trials remains unconfirmed because the required trial records and supporting evidence have not yet been submitted for independent review.

The preliminary Week 10 platform findings remain documented separately and are not counted as official production results.

### 4.2 Baseline Corpus Integrity Verification

During Week 11, Ifeanyi independently verified the approved testing corpus stored in `tests/fixtures/week9_corpus.json`.

The verification produced the following results:

- Total corpus entries: 8

- Required fields (`id`, `category`, `text`, `sha256`): PASS

- Unique message identifiers: PASS

- SHA-256 integrity checks: 8 of 8 passed

**Result:** All eight approved messages passed the structural and integrity checks performed.

**Evidence:** `docs/week11_data_quality_audit.md`

This verification establishes that the approved corpus is structurally valid and available for production testing. It does not demonstrate that production trials have been completed.

### 4.3 Automated Regression Testing

Ifeanyi executed the existing automated test suite using:

`python -m pytest -q`

**Results:**

- 43 tests passed.

- 132 subtests passed.

- No failures reported.

- Execution time: approximately 0.23 seconds.

These results establish a passing baseline for the current codebase and provide a reference for evaluating future changes.

**Evidence:** `docs/week11_data_quality_audit.md` and the corresponding terminal output.

The automated regression results do not establish completion of the 168 production trials or successful implementation of the proposed Week 11 error-correction feature.

### 4.4 Week 11 Production Workflow Validation and Merge (October 28)

Tristan submitted PR #24, **Week 11: Add Week 11 production testing workflow and trial setup**, containing four commits. The implementation prepares deterministic encoded inputs and trial records without performing external platform operations. It includes validation that completed trials have a tester, UTC timestamp, and valid evidence references, while genuinely empty retrieved text may be recorded as a completed recovery failure when supporting evidence exists.

**Independent verification by Ifeanyi:** `python -m pytest -q` — **56 tests passed and 132 subtests passed**, with no failures reported. The team leader merged PR #24 as commit `8646a48`, updated the local `main` branch, and verified a clean working tree before making further documentation changes.

**Evidence:** GitHub PR #24; merge commit `8646a48`; local pytest terminal output; `docs/week11_data_quality_audit.md`.

**Limitations:** The workflow has prepared 168 records but does not establish any completed manual platform trials. Production results, exact recovery, retention percentages, and supporting screenshots remain pending.

### 4.5 Previous Codec Validation

During Week 10, Henry reported successful local codec validation involving 38 tests and 132 subtests.

His work also included validation tools intended to identify missing evidence, duplicate trials, inconsistent metadata, and calculation errors.

These results support local codec readiness but do not establish successful message recovery across every external platform.

**Evidence:** `docs/week10_henry_codec_validation.md`

### 4.6 Week 11 Error-Correction Testing

The planned Week 11 error-correction tests include:

- Successful decoding without corruption.

- Recovery under correctable corruption.

- Detection of uncorrectable corruption.

- Unicode payload handling.

- Boundary conditions.

- Deterministic behavior.

- Prevention of incorrect successful recovery.

- Backward compatibility with baseline mode.

- Encoded-length overhead and payload capacity.

**Evidence Status:** Pending Henry's implementation, verified test results, and supporting screenshots.

No claim of successful error-correction functionality will be made until the implementation and corresponding tests have been reviewed.

### 4.7 Production Testing Evidence and Remaining Work

Tristan’s production workflow has been reviewed and merged, and official Gmail production testing has been authorized. His completed manual platform-trial submission remains pending verification.

The required evidence includes individual trial records, original and retrieved text, decoder results, character-retention calculations, screenshots, and explanations of successful and failed tests.

Once submitted, the team leader will review the evidence, use the available validation tools, identify missing or duplicate records, and update the production compatibility matrix.

**Current Status:** Baseline corpus verification and automated regression testing completed. Official production testing and error-correction verification remain outstanding.

## 5. Challenges and Lessons Learned

The main challenge is the delay in completing and verifying the Week 10 baseline production dataset. Reviewing a pull request containing hundreds of prepared trial files also required distinguishing generated data from the smaller set of workflow and validation changes.

This delay affects statistical analysis and the availability of real-world corruption examples for error-correction development.

The team has adjusted its schedule to work on baseline completion and error-correction development concurrently.

An important lesson is that preliminary testing, local codec validation, and official production results must be reported separately to maintain accuracy.

The team is also emphasizing early communication, careful pull-request reviews, and reproducible testing evidence. A further lesson from PR #24 is that a passing automated workflow and prepared trial records must not be confused with completed real-platform experiments.

## 6. Progress Against the Semester Plan

The semester plan originally scheduled baseline data completion and statistical analysis for Week 10.

Because those deliverables remain unverified, they have been carried into Week 11.

Week 11 also requires error-correction design and implementation. The team completed production workflow preparation and validation through PR #24 and is proceeding with planning and design review while awaiting verified testing results.

**Schedule Adjustment:** Target completion of outstanding Week 10 and Week 11 deliverables by Friday, October 30, followed by evidence review and report finalization.

Any unfinished work will be documented accurately and incorporated into the updated project schedule.

## 7. Next Steps

1. Obtain Tristan’s verified Gmail production testing progress and raw evidence.

2. Review raw production files and trial records.

3. Validate results and update the compatibility matrix.

4. Review Henry's error-correction design decision and implementation.

5. Run and document Week 11 error-correction tests.

6. Review pull requests and individual contributions.

7. Conduct and document Friday's team meeting.

8. Embed testing screenshots with detailed explanations.

9. Finalize the report before Sunday submission.

## 8. Supporting Repository Documents

### Planning and Quality Assurance

- `docs/semester_plan.md`

- `docs/week9_testing_protocol_draft.md`

- `docs/week10_data_quality_audit.md`

- `docs/week11_data_quality_audit.md`

- `docs/week11_error_correction_design_review.md`

### Meeting Minutes

- `meeting_minutes/2026-10-26_week11.md`

- Friday meeting minutes – To be added after the meeting.

### Individual Journals

- `weekly_journals/ifeanyi/week11.md`

- Tristan's Week 11 journal – Pending.

- Henry's Week 11 journal – Pending.

### Testing Evidence

- `tests/week10_testing/workflow_verification.md`

- GitHub PR #24 and merge commit `8646a48` – workflow reviewed and merged.
- Week 11 production trial logs – 168 records prepared; completed results pending verification.

- Week 11 error-correction tests and screenshots – Pending.

## 9. Report Status

**In Progress – Updated through October 28, 2026.**

This report now includes the verified PR #24 workflow merge and independent automated testing. It will be updated further to include actual production trial outcomes, error-correction implementation results, detailed test descriptions, embedded screenshots, any additional verified individual contributions, and Friday meeting minutes before final submission.

### Gmail Official Production Testing Update — October 29, 2026

**Responsible Team Member:** Tristan Koch
**Platform:** Gmail
**Status:** In Progress — Awaiting Independent Verification

During Week 11, Tristan reported completing 12 of the 24 planned official Gmail production trials. These trials covered four approved corpus messages (SA01, SA02, SU01, and SU02), each tested three times.

**Reported Testing Results:**

- Trials completed: 12 of 24 (50%).
- Analyzer validation: 12 of 12 records passed.
- Successful exact message recoveries: 0 of 12.
- U+200B characters: Removed in all 12 trials.
- U+200C characters: Retained in all 12 trials.
- U+200D characters: Retained in all 12 trials.
- Decoder outcome: Incomplete or malformed byte blocks.

**Analysis:**

The reported results indicate that Gmail removed U+200B characters while preserving U+200C and U+200D characters in the tested messages. This prevented successful recovery of the hidden messages.

These findings are consistent with the earlier Week 10 preliminary observations that Gmail does not fully preserve the zero-width encoded data.

**Evidence and Verification:**

Tristan confirmed that the 12 trial records passed analyzer validation and that the supporting evidence has been prepared locally. However, the complete evidence has not yet been submitted through GitHub for independent review.

Therefore, these results are documented as tester-reported progress rather than independently verified production findings.

**Next Steps:**

1. Complete the remaining 12 Gmail trials by Friday, October 30, 2026, at 5:00 PM ET.
2. Submit the complete Gmail testing records, screenshots, and supporting evidence through a GitHub pull request.
3. Independently review the evidence and verify retention and recovery calculations.
4. Update the official platform compatibility matrix after verification.
5. Continue testing other approved platforms as time permits.



### Week 11 Hamming Error-Correction Implementation and Independent Verification — October 30, 2026

**Contributor:** Henry Smith
**Reviewer:** Ifeanyi Emeka
**Pull Request:** #25
**Merge Commit:** `3d311e7`
**Status:** Successfully reviewed, tested, and merged into `main`.

#### Milestones Achieved

Henry completed the implementation and testing of an optional Hamming SECDED error-correction mode for the zero-width Unicode steganography codec.

The implementation supports single-bit error correction and double-bit error detection while maintaining compatibility with the existing codec functionality.

#### Testing and Verification

The team leader independently reviewed Henry's source-code changes, documentation, and supporting evidence.

The following tests were executed successfully:

- Full automated test suite: 54 tests passed and 148 subtests passed.
- Existing codec regression tests: 28 tests passed and 132 subtests passed.
- Hamming verification script: All five checks passed.

The five verification checks covered Unicode round-trip, single-bit correction, double-bit rejection, Gmail-style character stripping, and Word-style character stripping.

The Gmail-style and Word-style tests confirmed safe rejection of unrecoverable payloads, not successful message recovery.

#### Challenges and Lessons Learned

A major challenge is that some platforms remove hidden Unicode characters during text processing. Although Hamming error correction can repair certain bit errors, it cannot restore a payload when required characters have been completely removed.

This reinforced the importance of testing error-correction techniques against realistic platform behavior instead of relying only on local unit tests.

#### Individual Contributions

**Henry Smith:** Researched error-correction approaches, implemented Hamming SECDED mode, developed tests, prepared documentation and screenshots, and submitted PR #25.

**Ifeanyi Emeka:** Reviewed the pull request, examined source-code changes, independently executed automated and targeted tests, verified the implementation's limitations, and merged the approved contribution into the main branch.

#### Remaining Work

Tristan's official Gmail production-testing results still require complete evidence submission and independent verification before the platform compatibility matrix can be finalized.

**Verification Status:** Hamming implementation verified and merged. Official Gmail production results remain pending independent verification.**Current Status:** Gmail production testing is 50% complete based on Tristan's progress report. Final results and independent verification remain pending.