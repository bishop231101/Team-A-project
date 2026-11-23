# CS481 Capstone Project — Week 14 Progress Report

**Project:** Zero-Width Unicode Steganography with Error Correction  
**Team:** Team A  
**Reporting Period:** November 16–22, 2026  
**Team Members:** Ifeanyi Emeka, Henry Smith, and Tristan Koch

## 1. Milestones Achieved

- Conducted both scheduled Week 14 meetings with all three team members present. The Monday meeting established the week’s priorities, and the Friday meeting reviewed the work completed during the week.
- Reviewed and integrated Henry Smith’s code-quality improvements, automated tests, documentation updates, and codec verification script into the main branch.
- Passed all five targeted codec verification checks covering backward compatibility, Unicode round-trip behavior, single-bit correction, and double-bit error detection.
- Completed post-integration regression testing with 87 tests and 549 subtests passed. A subsequent local rerun reproduced both passing totals.

## 2. Subtasks Completed

### 2.1 Team Coordination

On Monday, November 16, the team discussed the remaining development work and established priorities for code completion, integration testing, documentation, and the final deliverables. Ifeanyi recorded and committed the meeting minutes to GitHub.

On Friday, November 20, all three team members met again to review the work completed during Week 14. This meeting provided a shared review of the week’s progress as the team prepared for the final report and presentation.

### 2.2 Code Quality and Integration

Henry completed a code-quality review, added automated quality tests, updated the project documentation, and prepared a script for verifying key codec behaviors. Ifeanyi reviewed the contribution and ran the verification script before integrating the changes into the main branch. The full regression suite was then run against the integrated project.

### 2.3 Documentation and Test Evidence

The documentation describes the Hamming mode’s ability to correct single-bit substitutions and detect double-bit errors. It also records that deleted or stripped zero-width symbols fall outside the mode’s correction capability.

The regression results below identify each run by its purpose and timing. The embedded screenshot documents the earlier independent run, while the table also records the post-integration run and the final local rerun.

## 3. Individual Contributions

### 3.1 Ifeanyi Emeka — Team Leader

- Coordinated the Monday team meeting, documented the discussion, and committed the minutes to GitHub.
- Established the Week 14 report structure and coordinated integration, testing, and documentation.
- Reviewed Henry’s contribution, ran the targeted codec verification script, and integrated the changes into the main branch.
- Ran the automated regression suite and recorded the post-integration results.
- Performed a final local rerun that reproduced the post-integration passing totals.
- Participated in Friday’s review of the week’s work.

### 3.2 Henry Smith — Error-Correction Development

- Completed the Week 14 code-quality review.
- Added automated quality tests and prepared the codec verification script.
- Updated project documentation, including the scope and limitations of Hamming error correction.
- Participated in both Week 14 team meetings.

### 3.3 Tristan Koch — Testing and Statistical Analysis

- Participated in Monday’s planning meeting and Friday’s review of the week’s work.
- Specific Week 14 testing and statistical analysis deliverables are pending confirmation against the repository records.

## 4. Testing and Verification Results

### 4.1 Targeted Codec Verification

The codec verification script checked that existing encoding modes remained compatible and that Hamming mode behaved as documented for the tested cases.

| Check | Behavior verified | Result |
| --- | --- | --- |
| Baseline backward compatibility | The codec remained compatible with the original format. | Passed |
| Repetition-mode backward compatibility | The codec remained compatible with the existing repetition mode. | Passed |
| Hamming-mode Unicode round trip | A Unicode payload was recovered after encoding and decoding. | Passed |
| Single-bit correction | Hamming mode corrected a single-bit error in the tested case. | Passed |
| Double-bit error detection | Hamming mode detected a double-bit error in the tested case. | Passed |

All five checks passed. These results covered the specified compatibility and error-handling cases. Recovery from deleted or stripped zero-width symbols remains outside the documented capability of Hamming mode.

### 4.2 Automated Regression Testing

The full automated suite was run using `python -m pytest -q`. The earlier independent run established a Week 14 reference point. The post-integration run verified the project after Henry’s contribution was merged, and the final local rerun checked whether the post-integration result could be reproduced.

| Regression run | Tests passed | Subtests passed | Runtime |
| --- | ---: | ---: | ---: |
| Earlier independent Week 14 run | 83 | 546 | 5.20 seconds |
| Post-integration run | 87 | 549 | 5.01 seconds |
| Final local verification rerun | 87 | 549 | 5.30 seconds |

All three runs completed with no reported failures. The post-integration run and the final local rerun both recorded 87 passing tests and 549 passing subtests.

![Terminal output from the earlier Week 14 regression run showing 83 tests and 546 subtests passed](../docs/evidence/week14_regression_83_passed.png)

*Figure 1. The earlier independent Week 14 regression run completed in 5.20 seconds with 83 tests and 546 subtests passed.*

## 5. Lessons Learned

Running targeted checks before integration helped verify the specific codec behaviors affected by the changes. Running the full suite after integration provided broader coverage of the project, and repeating the suite confirmed that the passing totals were reproducible.

The week’s testing also reinforced the importance of recording which run produced each result. The earlier screenshot shows 83 tests and 546 subtests, while both later runs show 87 tests and 549 subtests. Labeling the evidence by run makes the sequence clear and keeps each figure tied to the result it supports.

## 6. Progress Compared With the Semester Plan

Week 13 focused on compatibility and statistical analysis. Week 14 advanced the project into code-quality review, integration, and final regression verification. The team completed the targeted codec checks and verified the integrated project through two full regression runs with matching passing totals.

The remaining work centers on completing the Week 14 submission records and using the verified results to prepare the final project report and presentation.

## 7. Meeting Documentation

| Meeting | Attendance | Purpose and outcome |
| --- | --- | --- |
| Monday, November 16 | Ifeanyi Emeka, Henry Smith, and Tristan Koch | Established priorities for development, integration, testing, and documentation. Meeting minutes were committed to GitHub. |
| Friday, November 20 | Ifeanyi Emeka, Henry Smith, and Tristan Koch | Reviewed the work completed during Week 14. |

## 8. Remaining Work and Next Steps

- Verify that the Friday meeting minutes are available on GitHub.
- Confirm Tristan’s specific Week 14 deliverables against the repository records and update the individual contributions section.
- Verify that the embedded regression screenshot renders in the GitHub report.
- Finalize the Week 14 progress report and individual journals.
- Prepare the final project report and presentation using the verified test results and documented codec limitations.

## 9. Conclusion

The team held both scheduled Week 14 meetings with full attendance and integrated Henry’s code-quality and verification work into the main branch. All five targeted codec checks passed, and the final local run reproduced the post-integration results of 87 tests and 549 subtests passed. These results provide the testing evidence for the final project report and presentation.