# CS481 – Team 1 Weekly Report 10

**Project:** Zero-Width Unicode Steganography with Social-Media Robustness Engineering  
**Team Leader:** Ifeanyi Emeka  
**Team Members:** Ifeanyi Emeka, Tristan Koch, Henry Smith  
**Reporting Period:** Week 10 (October 19–25, 2026)  
**Status:** Week 10 Documentation Completed – Production Testing Pending

## 1. Weekly Overview

During Week 10, our team focused on completing preliminary platform workflow verification, strengthening codec validation, organizing testing evidence, and preparing for official production testing.

Tristan completed preliminary testing for all seven approved platform-operation combinations and documented the results, screenshots, and limitations. Five platforms successfully preserved and decoded the hidden message, while Gmail and Microsoft Word failed.

Henry completed additional codec validation and developed tools to verify future production testing records.

As team leader, I coordinated team responsibilities, reviewed pull requests, identified documentation and repository issues, and ensured that completed work was properly preserved. I also updated the data-quality audit and maintained our Monday and Friday meeting documentation.

Although preliminary verification was completed, official production testing remains pending. Our planned production testing start date is October 26, 2026.

## 2. Milestones and Progress

### Completed

- Conducted the Monday, October 19, team meeting with all members present.
- Conducted the Friday, October 23, team meeting with all members present.
- Documented both meetings in the repository.
- Completed preliminary workflow verification for all seven approved platform-operation combinations.
- Documented preliminary testing results, screenshots, and limitations.
- Updated seven platform-specific testing command guides.
- Improved testing file organization and naming conventions.
- Preserved preliminary evidence using separate platform folders.
- Completed Henry's additional codec validation work.
- Developed production trial validation tools.
- Reviewed and merged Henry's PR #22.
- Identified PR #23 as an accidental revert that should not be merged.
- Reviewed and merged Tristan's PR #21.
- Updated the Week 10 data-quality audit.
- Completed individual Week 10 documentation.
- Confirmed the approved production testing scope of 168 planned trials.

### Pending

- Begin official production testing.
- Collect complete production trial logs and supporting evidence.
- Validate production records and identify missing or duplicate trials.
- Investigate Gmail and Microsoft Word decoding failures.
- Update the compatibility matrix with verified production results.

## 3. Individual Team Contributions

### Ifeanyi Emeka – Team Leader

During Week 10, I focused on team coordination, quality assurance, documentation, and repository management.

My contributions included:

- Coordinated and documented the Monday and Friday team meetings.
- Reviewed the approved testing protocol and confirmed the production scope.
- Created and updated the Week 10 data-quality audit.
- Reviewed Henry's validation contributions and coordinated the resolution of the accidental PR #23 revert.
- Reviewed Tristan's PR #21 and identified problems with shared testing filenames and evidence organization.
- Requested separate platform folders and consistent naming conventions to prevent evidence from being overwritten.
- Reviewed Tristan's updated testing documentation and preliminary results.
- Merged PR #21 into the main branch after the requested corrections were submitted.
- Coordinated the planned transition to official production testing.
- Updated my individual journal and prepared the Week 10 team report.

These activities supported team accountability, testing quality, documentation accuracy, and project progress.

### Tristan Koch – Platform Testing and Workflow Verification

Tristan completed preliminary workflow verification for all seven approved platform-operation combinations.

His contributions included:

- Confirmed platform access and testing workflows.
- Created and updated seven platform-specific testing guides.
- Completed preliminary testing for Gmail, Discord, Microsoft Word, Microsoft Outlook, Telegram Web, Notepad++, and Google Chrome Browser Console.
- Documented character retention, decoder outcomes, screenshots, and platform limitations.
- Identified preliminary decoding failures on Gmail and Microsoft Word.
- Reorganized testing files into platform-specific directories.
- Implemented consistent file naming conventions.
- Corrected newline-preserving comparisons.
- Protected existing Notepad++ evidence from accidental overwriting.
- Finalized the workflow verification documentation.
- Completed his Week 10 individual journal.
- Submitted his changes through PR #21, which was reviewed and merged.

**Current status:** Preliminary workflow verification completed. Production testing pending.

### Henry Smith – Codec Validation and Failure Analysis

Henry focused on strengthening codec reliability and preparing tools for validating production testing data.

His contributions included:

- Completed additional codec verification and regression testing.
- Reported successful execution of 38 tests and 132 subtests.
- Added five new validation tests.
- Developed a production trial validation tool to examine testing records.
- Implemented checks for missing evidence, inconsistent metadata, duplicate trials, and calculation errors.
- Reproduced the preliminary WeChat baseline zero-width character counts.
- Documented the limitations of independently verifying WeChat results without the raw retrieved text.
- Completed his Week 10 validation documentation and individual journal.
- Confirmed that his completed work was included in merged PR #22.
- Identified PR #23 as an accidental revert that should not be merged.

**Current status:** Codec validation completed for the reported Week 10 checks. Further analysis of production platform failures remains pending.

## 4. Testing and Evidence

### Approved Production Testing Scope

The revised protocol authorizes seven platform-operation combinations:

1. Gmail – Send and retrieve message.
2. Discord – Send and retrieve message.
3. Microsoft Word – Save, reopen, and retrieve text.
4. Microsoft Outlook – Send and retrieve message.
5. Telegram Web – Send and retrieve message.
6. Notepad++ – Paste and copy back.
7. Browser Console – Paste and copy back.

The testing plan uses eight approved corpus messages with three repetitions per message.

**Total planned production trials: 168.**

### Week 10 Preliminary Platform Testing Results

| Platform | Character Retention | Decoder Result |
|---|---:|---|
| Gmail | 44.74% | Failed |
| Discord | 100% | Passed |
| Microsoft Word | 0% | Failed |
| Microsoft Outlook | 100% | Passed |
| Telegram Web | 100% | Passed |
| Notepad++ | 100% | Passed |
| Browser Console | 100% | Passed |

Five platform workflows passed preliminary decoding, while two failed.

Gmail retained only 44.74% of the zero-width characters, and Microsoft Word retained 0%. Both failed to recover the hidden message.

These results indicate that platform behavior can affect the reliability of zero-width Unicode steganography.

The failures are valid preliminary findings and will remain documented for further investigation.

### Preliminary WeChat Evidence Review

During Week 9, Tristan documented two preliminary WeChat feasibility workflows that reported successful recovery.

Henry independently reproduced the local baseline counts for the message `WeChat test message`:

- U+200B: 137
- U+200C: 111
- U+200D: 30
- Total: 278 zero-width characters

The screenshots were consistent with the reported counts. However, the raw post-platform retrieved text was not available for independent decoder verification.

WeChat remains outside the approved seven-combination production scope.

### Codec Validation and Production Readiness

Henry reported that the Week 10 codec validation suite passed 38 tests and 132 subtests.

His production trial validation tools are intended to support reproducible testing by checking raw evidence, trial metadata, duplicates, and calculated metrics.

### Production Testing Status

**Official production testing has not yet been verified as started.**

The preliminary platform checks do not count toward the 168 planned production trials.

The team plans to begin production testing on October 26, 2026, after confirming readiness.

### Supporting Evidence

The repository contains preliminary workflow verification documentation, platform-specific command guides, testing screenshots, and individual validation records.

Evidence should be reviewed alongside the reported findings rather than relying only on summary percentages.

## 5. Challenges and Lessons Learned

### Platform Compatibility

Gmail and Microsoft Word failed preliminary decoding tests.

This demonstrated that successful local encoding and decoding do not guarantee that every external platform will preserve the hidden information.

### Evidence Organization

The initial testing commands reused common filenames, creating a risk of accidentally overwriting evidence.

We addressed this by introducing separate platform directories and more descriptive filenames.

### Repository Management

An accidental revert in PR #23 created a risk of removing Henry's completed work.

This reinforced the importance of reviewing pull requests before merging.

### Production Testing Delays

Our planned production testing schedule was delayed while the team verified platform workflows and strengthened documentation.

Although this affected the original timeline, completing these checks improved our preparation for reproducible testing.

### Team Communication

Regular updates and clear responsibilities helped the team identify issues early and coordinate corrections.

## 6. Progress Against Semester Plan

Our semester plan originally targeted controlled survival-rate data collection beginning in Week 9.

However, full production testing was delayed because the approved platform workflows and supporting evidence required further verification.

During Week 10, the team made measurable progress by completing preliminary verification across all seven approved platform-operation combinations.

We also strengthened codec validation, improved evidence organization, and prepared tools for checking production testing records.

| Milestone | Week 10 Status |
|---|---|
| Approved testing protocol | Completed |
| Seven platform workflow verifications | Completed |
| Preliminary results and evidence | Documented |
| Codec validation | Completed for reported checks |
| Production trial validation tools | Developed |
| Official production testing | Pending |
| Verified production dataset | Not yet established |
| Production compatibility matrix | Pending |

The production workload remains 168 planned trials.

The team intends to begin official production data collection on October 26, 2026.

## 7. Next Steps

- Begin official production testing after final readiness confirmation.
- Collect raw encoded and retrieved text, screenshots, and trial records.
- Maintain unique identifiers for every production trial.
- Use Henry's validation tools to check evidence and calculations.
- Investigate the Gmail and Microsoft Word failures.
- Preserve both successful and unsuccessful experimental results.
- Update the compatibility matrix using verified production data.
- Continue documenting individual contributions and meeting minutes.
- Review testing progress during the next scheduled team meeting.

## 8. Supporting Repository Documents

### Protocol and Quality Assurance

- `docs/week9_testing_protocol_draft.md`
- `docs/week10_data_quality_audit.md`
- `docs/week10_henry_codec_validation.md`

### Meeting Minutes

- `meeting_minutes/2026-10-19_week10.md`
- `meeting_minutes/2026-10-23_week10.md`

### Individual Journals

- `weekly_journals/ifeanyi/week10.md`
- `weekly_journals/henry/2026-10-22.md`
- Tristan's Week 10 individual journal, included in PR #21.

### Testing and Validation

- `tests/week9_testing/preliminary_feasibility_testing_WeChat.md`
- `tests/week10_testing/workflow_verification.md`
- `tests/week10_testing/verify_henry_week10.py`
- `tests/week10_testing/validate_production_trials.py`
- Platform-specific preliminary testing guides and supporting screenshots under `tests/week10_testing/`.

## 9. Report Status

**Week 10 report prepared for final repository and evidence review.**

The team completed the week's preliminary workflow verification, codec validation work, documentation improvements, and meeting requirements.

The remaining major milestone is official production testing, scheduled to begin October 26, 2026.

Preliminary findings have been reported separately from production results to maintain accuracy and avoid overstating progress.

All Week 10 contributions and supporting documents must be committed and pushed to the main branch before final submission.