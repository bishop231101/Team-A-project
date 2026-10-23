# CS481 Team 1 – Week 10 Data Quality Audit

**Prepared by:** Ifeanyi Emeka – Team Leader  
**Date:** October 23, 2026  
**Project:** Zero-Width Unicode Steganography with Social-Media Robustness Engineering  
**Status:** Preliminary Workflow Verification Completed – Production Testing Pending

## 1. Purpose

The purpose of this Week 10 audit is to monitor the quality, accuracy, and completeness of our testing data. As team leader, my responsibility is to ensure that our testing follows the approved protocol and that all reported results are supported by proper evidence.

This audit also addresses the challenges identified during Week 9, including incomplete production testing, unverified platform workflows, and the need for consistent documentation.

## 2. Approved Production Testing Scope

The team will use the revised testing scope authorized on October 17, 2026.

| Platform | Operation | Preliminary Status |
|---|---|---|
| Gmail | Send and retrieve message | Completed – Decode failed |
| Discord | Send and retrieve message | Completed – Passed |
| Microsoft Word | Save, reopen, and retrieve text | Completed – Decode failed |
| Microsoft Outlook | Send and retrieve message | Completed – Passed |
| Telegram Web | Send and retrieve message | Completed – Passed |
| Notepad++ | Paste and copy back | Completed – Passed |
| Browser Console | Paste and copy back | Completed – Passed |

The approved production scope includes:

- 7 platform-operation combinations
- 8 approved test messages
- 3 repetitions per message
- 24 trials per combination
- 168 total planned production trials

These figures represent the approved workload, not completed production testing.

## 3. Data Quality Requirements

Each production trial must include:

- Unique trial identification number
- Platform and operation tested
- Approved test message identifier
- Codec configuration
- Original and recovered zero-width character counts
- Character retention percentage
- Decoder success or failure
- Exact message recovery result
- Screenshot or other supporting evidence
- Relevant observations or failure notes

Character retention and successful message decoding must be recorded separately.

A trial with 100% character retention should not automatically be classified as a successful recovery unless the decoder returns the exact original secret.

All preliminary testing evidence must remain separate from official production records.

## 4. Week 10 Audit Checklist

- [x] Review the revised Week 9 testing scope.
- [x] Identify the seven approved platform-operation combinations.
- [x] Confirm the required production trial count.
- [x] Document workflow verification requirements.
- [x] Establish Week 10 team responsibilities.
- [x] Receive Tristan's platform workflow verification update.
- [x] Review Tristan's preliminary testing summary.
- [x] Review the updated file organization and naming conventions.
- [x] Confirm supporting preliminary evidence was submitted.
- [x] Review and merge Tristan's PR #21.
- [x] Coordinate with Henry regarding codec validation and PR corrections.
- [ ] Review official production trial logs.
- [ ] Independently verify production screenshots and raw evidence.
- [ ] Check production trial records for missing or duplicate entries.
- [ ] Validate production retention and exact recovery calculations.
- [ ] Update the production compatibility matrix with verified results.
- [ ] Review production decoder failures with Henry.
- [ ] Confirm production testing progress against the project plan.

## 5. Preliminary Testing and Evidence Review

### Week 9 – WeChat Feasibility Testing

Tristan submitted preliminary WeChat feasibility testing during Week 9.

The report documented two operations:

1. Send and retrieve message
2. Paste and copy back

Both preliminary tests reported retention of all 278 zero-width characters and successful recovery of the original secret.

However, WeChat is not included in the approved seven-combination production matrix.

### Week 10 – Seven-Platform Preliminary Verification

During Week 10, Tristan completed and documented preliminary workflow verification for all seven approved platform-operation combinations.

| Platform | Reported Retention | Decoder Result |
|---|---:|---|
| Gmail | 44.74% | Failed |
| Discord | 100% | Passed |
| Microsoft Word | 0% | Failed |
| Microsoft Outlook | 100% | Passed |
| Telegram Web | 100% | Passed |
| Notepad++ | 100% | Passed |
| Browser Console | 100% | Passed |

Five platform workflows successfully preserved the encoded message and supported decoding.

Gmail and Microsoft Word did not preserve enough information for successful decoding.

These failures are important experimental findings and must be documented accurately rather than excluded from future analysis.

Tristan also updated the platform-specific command guides, file organization, naming conventions, and workflow verification documentation. His changes were reviewed and merged through PR #21.

The reported results and supporting evidence are available in the Week 10 testing materials. The preliminary summary has been reviewed, but independent verification of every raw artifact and screenshot remains an additional quality-control task.

**Important:** Preliminary tests do not count toward the 168 planned production trials.

## 6. Outstanding Issues and Risks

### Issue 1 – Platform Compatibility

Gmail and Microsoft Word failed preliminary decoding tests.

**Action:** Preserve the observed failures, investigate potential character removal or transformation, and ensure the production testing protocol captures these outcomes accurately.

### Issue 2 – Production Testing Progress

All seven preliminary workflows have been tested, but official production trial completion has not been established.

**Action:** Begin production data collection after the team reviews preliminary findings and confirms readiness. The planned start date is October 26, 2026.

### Issue 3 – Evidence Quality

Production results must be reproducible and supported by raw records.

**Action:** Require clearly labeled screenshots, original and retrieved files, trial identifiers, and explanations of failures.

### Issue 4 – Repository Integrity

During Week 10, Henry identified PR #23 as an accidental reversal of his already merged PR #22.

**Action:** Preserve the validated work on the main branch and continue reviewing pull requests for unintended deletions before merging.

### Issue 5 – Communication and Coordination

Delays in reporting progress can affect the testing schedule and weekly submission.

**Action:** Continue regular team updates, maintain meeting minutes, and document responsibilities and completed work.

## 7. Individual Leadership Contributions

During Week 10, I:

- Reviewed the revised production testing protocol and confirmed the approved scope of 168 trials.
- Coordinated the Monday team meeting and established Week 10 responsibilities.
- Maintained the data-quality audit and testing evidence requirements.
- Reviewed Henry's validation contributions and coordinated the resolution of the accidental PR #23 revert.
- Reviewed Tristan's PR #21 and identified risks involving shared filenames and overwritten evidence.
- Requested separate platform folders, consistent naming conventions, and preservation of existing evidence.
- Reviewed Tristan's updated testing documentation and preliminary findings.
- Merged PR #21 after the requested corrections were submitted.
- Coordinated the plan to begin official production testing on October 26.
- Continued preparing the team's Week 10 report and individual documentation.

These activities support my responsibilities for leadership, quality assurance, repository management, and team coordination.

## 8. Progress Compared With the Project Plan

The project has progressed through codec validation, preliminary platform testing, workflow verification, and production testing preparation.

During Week 10:

- All seven approved platform workflows received preliminary testing.
- Five preliminary workflows passed decoding.
- Two preliminary workflows failed decoding.
- Testing guides and evidence organization were improved.
- Henry's codec validation work was preserved on the main branch.
- Tristan's completed Week 10 contributions were merged into the main branch.

The approved production workload remains 168 trials.

**Verified production trials: Not yet established.**

The team has made progress toward production readiness, but preliminary verification does not satisfy the outstanding production testing milestone.

## 9. Next Actions

1. Finalize the Week 10 team report and individual journals.
2. Complete and document the Friday, October 23, team meeting.
3. Confirm that all preliminary evidence is preserved in the repository.
4. Review Gmail and Microsoft Word failures with the team.
5. Begin official production testing on October 26, following team readiness confirmation.
6. Use Henry's validation tools to check production trial records.
7. Review incoming production data for completeness, accuracy, and duplicate entries.
8. Update the compatibility matrix using verified production results.
9. Continue documenting progress and challenges in future weekly reports.

## 10. Audit Conclusion

Week 10 produced meaningful progress in workflow verification, documentation, repository organization, and preparation for official production testing.

All seven approved platform workflows were tested preliminarily, and the results identified important compatibility differences. The failures observed in Gmail and Microsoft Word demonstrate why platform-specific testing is necessary.

As team leader, I reviewed the team's contributions, coordinated corrections, protected existing work from accidental deletion, and maintained the requirements for reliable evidence.

The next priority is to begin official production testing while maintaining accurate records and ensuring that preliminary results are not confused with production data.

**Current Audit Status:** Preliminary verification completed – Awaiting verified production testing records.