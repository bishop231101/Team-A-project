# CS481 Capstone Project
## Week 12 Progress Report
**Project:** Zero-Width Unicode Steganography and Error-Correction Evaluation  
**Team:** Team 1  
**Reporting Period:** November 2–8, 2026  
**Team Leader:** Ifeanyi Emeka  
**Team Members:** Ifeanyi Emeka, Henry Smith, Tristan Koch

---

## 1. Executive Summary

During Week 12, Team 1 focused on stabilizing the Hamming SECDED error-correction implementation, completing outstanding production-platform testing, validating software functionality, and preparing controlled comparative recovery experiments.

The team made substantial progress in implementation, testing, and documentation. Henry completed the Hamming stabilization work, while Tristan completed the remaining production trials across Gmail, Notepad++, and Microsoft Word. Ifeanyi coordinated team activities, conducted independent verification, reviewed contributions, and integrated the completed work into the main GitHub repository.

The updated automated regression suite successfully passed **74 tests and 546 subtests**, demonstrating that the implementation satisfied the covered regression checks.

A total of **72 production trials** were submitted across three applications. The reported results demonstrated significant differences in zero-width character preservation between platforms.

The initial comparative experiment pilot was also completed. However, the full Baseline-versus-Hamming evaluation and corresponding recovery analysis remain outstanding pending final review of the pilot methodology and results.

Overall, Week 12 achieved substantial technical and documentation progress, although the complete comparative evaluation milestone has not yet been satisfied.

## 2. Milestones Achieved

The following milestones were achieved during the reporting period:

1. Completed Hamming SECDED stabilization and expanded regression coverage.
2. Independently verified the updated implementation using the automated regression suite and dedicated Hamming verification script.
3. Completed and submitted the remaining Gmail, Notepad++, and Microsoft Word production-testing records.
4. Prepared Gmail reproducibility documentation and supporting testing evidence.
5. Completed the initial SA01 comparative experiment pilot.
6. Reviewed and merged Henry's PR #27 and Tristan's PR #28 into the main repository.
7. Conducted and documented both required weekly team meetings.
8. Updated team documentation, individual journals, and the Week 12 progress report.

The full comparative experiment and final recovery analysis remain pending.

## 3. Subtasks Completed

### 3.1 Hamming SECDED Stabilization

Henry expanded the protected-mode regression coverage across all eight approved corpus messages.

The updated implementation was evaluated for:

- Deterministic Baseline and Hamming encoding and decoding.
- Successful protected-mode round trips.
- Correction of single-bit corruption.
- Detection and rejection of double-bit corruption.
- Rejection of tested three-bit corruption patterns that could otherwise produce false-success outcomes.
- Damaged-format handling and Unicode boundary conditions.
- Encoded-length overhead associated with Hamming protection.

The stabilization work was submitted through PR #27 and merged following independent verification.

### 3.2 Production-Platform Testing

Tristan completed the outstanding production trials across three platforms.

| Platform | Trials Completed | Reported Exact Recovery | Reported Character Retention |
|---|---:|---|---|
| Gmail | 24 | 0 of 24 | Variable; substantial character loss |
| Notepad++ | 24 | 24 of 24 | 100% |
| Microsoft Word | 24 | 0 of 24 | 0% |
| **Total** | **72** | **24 of 72** | Platform-dependent |

The results indicate that the reliability of the zero-width steganography technique depends strongly on how the target application processes and preserves invisible Unicode characters.

The Gmail reproducibility procedure, individual production records, supporting screenshots, and updated journal were submitted through PR #28.

These findings are based on the submitted production-testing records. The successful automated regression suite does not independently validate every manual platform trial.

### 3.3 Comparative Experiment Preparation

Tristan completed the SA01 pilot to evaluate the behavior of Baseline and Hamming modes under controlled corruption.

The pilot included five conditions:

1. No corruption.
2. Single-bit corruption.
3. Double-bit corruption.
4. Approximately 1% deletion.
5. Approximately 5% deletion.

Each condition was evaluated once in both modes, producing **10 individual pilot trial records** and a generated `summary.json` file.

The script was revised following Henry's technical feedback. The pilot was kept separate from the production-testing PR to allow independent methodology and results review.

The full comparative experiment has not yet been executed.

## 4. Testing and Verification Results

### 4.1 Initial Independent Regression Testing

At the beginning of Week 12, Ifeanyi independently executed the existing automated Python test suite.

**Results:**
- Tests passed: 67
- Subtests passed: 148
- Execution time: 5.17 seconds
- Reported failures: None

![Initial Week 12 pytest results](../docs/evidence/week12_pytest_results.png)

**Figure 1. Initial Week 12 regression test results.**

The initial regression run established a passing baseline before the additional Week 12 stabilization tests were integrated.

### 4.2 Updated Regression Testing

Following Henry's stabilization changes, the complete automated regression suite was executed again.

**Results:**
- Tests passed: 74
- Subtests passed: 546
- Independently observed execution time: 4.62 seconds
- Reported failures: None

![Updated Hamming regression results](../tests/week12_testing/screenshots/henry/full_regression_74_passed.png)

**Figure 2. Updated regression suite following Hamming stabilization.**

The additional coverage increased the number of passing tests and subtests while preserving successful execution of the existing regression checks. This provides evidence of backward compatibility within the tested behaviors.

Following integration of the team's PRs, the complete suite was executed again and passed **74 tests and 546 subtests in 5.06 seconds**, providing additional post-integration regression evidence.

### 4.3 Hamming Stability and Encoded-Length Overhead

The dedicated Hamming verification script was independently executed.

The verification confirmed successful protected-mode round trips, recovery from supported single-bit corruption, and rejection of the tested double-bit and deleted-symbol corruption conditions.

Measured codec-character overhead ranged from **55.66% to 57.24%** across the approved corpus.

![Hamming stability and overhead verification](../tests/week12_testing/screenshots/henry/hamming_stability_overhead.png)

**Figure 3. Hamming SECDED stability and encoded-length overhead verification.**

These findings demonstrate the tradeoff between improved protection against certain corruption patterns and increased encoded-message length.

An important limitation is that Hamming protection does not restore zero-width characters completely deleted or stripped by an application.

Detailed reproduction procedures and technical findings are documented in `docs/week12_henry_hamming_stability.md`.

### 4.4 Production-Testing Evidence

The submitted production records indicate that Notepad++ preserved the invisible payloads and allowed exact recovery in all 24 trials.

In contrast, Microsoft Word removed the zero-width payload characters in all 24 trials, resulting in decoding failures.

Gmail produced no successful exact secret recovery in its 24 trials, with substantial character loss reported.

These findings demonstrate that platform-specific character handling is a major factor affecting the reliability of the technique.

The individual production records, supporting screenshots, and reproducibility documentation are maintained under the existing `tests/week11_testing/production_testing/` structure.

## 5. Individual Team Contributions

### 5.1 Ifeanyi Emeka — Team Leader

Ifeanyi coordinated the team's Week 12 activities and ensured that testing, documentation, and GitHub contributions were tracked.

His contributions included:

- Organized and documented the Monday and Friday team meetings.
- Assigned responsibilities and coordinated completion of outstanding work.
- Independently executed the initial automated regression suite.
- Reviewed Henry's stabilization work and ran the dedicated Hamming verification script.
- Independently verified the updated regression suite.
- Coordinated review and integration of PR #27 and PR #28.
- Resolved a Git merge conflict while preserving existing report updates.
- Maintained the weekly report, meeting documentation, and individual journal.
- Verified that the integrated repository continued to pass the automated regression suite.

### 5.2 Henry Smith — Error-Correction Development

Henry was responsible for Hamming stabilization and technical verification.

His contributions included:

- Stabilized the Hamming SECDED implementation.
- Expanded regression testing across the approved corpus.
- Added verification for supported corruption and rejection conditions.
- Documented encoded-length overhead and error-correction limitations.
- Prepared supporting scripts, screenshots, and technical documentation.
- Reviewed the comparative pilot methodology with Tristan.
- Submitted PR #27, which was successfully merged.

### 5.3 Tristan Koch — Production Testing and Comparative Experiments

Tristan was responsible for completing outstanding production-platform testing and preparing comparative experiments.

His contributions included:

- Completed 72 production trials across Gmail, Notepad++, and Microsoft Word.
- Documented platform-specific retention and recovery outcomes.
- Prepared Gmail reproducibility documentation.
- Submitted supporting trial records and screenshots.
- Completed the initial SA01 comparative pilot.
- Revised the pilot script following Henry's feedback.
- Generated 10 pilot trial records and a summary file.
- Updated his individual Week 12 journal.
- Submitted PR #28, which was successfully merged.

## 6. Progress Against the Project Plan

Week 12 was designated for error-correction recovery experiments, with an emphasis on implementation stability, controlled comparative testing, and analysis of recovery performance.

| Planned Deliverable | Week 12 Status |
|---|---|
| Hamming stabilization | Completed |
| Expanded automated regression testing | Completed |
| Outstanding production-platform testing | Completed for the three reported platforms |
| Comparative pilot | Completed; final review pending |
| Full comparative recovery experiment | Outstanding |
| Recovery statistics and comparative analysis | Outstanding |
| Overhead measurements | Completed for Hamming codec length |
| Overhead-versus-recovery-benefit analysis | Outstanding |
| Individual journals and meeting minutes | Updated |
| Team PR integration | Completed |

The team adjusted its priorities to ensure the implementation was stable and the outstanding production records were completed before expanding the comparative experiments.

This approach reduced the risk of generating a large dataset using an unverified methodology. However, it also delayed completion of the full comparative recovery analysis.

## 7. Challenges and Lessons Learned

### 7.1 Platform Compatibility

Production testing demonstrated substantial differences in the preservation of zero-width Unicode characters.

The results reinforce the need to evaluate steganographic techniques under actual application workflows rather than relying exclusively on local codec tests.

### 7.2 Error-Correction Limitations

Hamming SECDED protection successfully addressed supported bit-corruption scenarios but could not recover completely removed symbols.

This distinction is important when evaluating whether error correction can improve reliability on applications that sanitize or strip invisible characters.

### 7.3 Experimental Reproducibility

The comparative pilot highlighted the importance of defining corruption conditions consistently, documenting deletion calculations, preserving individual trial records, and verifying the testing script before large-scale execution.

### 7.4 Collaboration and Version Control

The integration of multiple pull requests required careful review and conflict resolution.

Independent testing, clear documentation, and disciplined GitHub workflows helped preserve project stability and trace individual contributions.

## 8. Outstanding Tasks and Next Steps

The following tasks remain priorities:

1. Complete the independent review of the SA01 comparative pilot, including the individual records and `summary.json`.
2. Confirm the final corruption methodology and approve the automated comparative experiment script.
3. Execute the complete Baseline-versus-Hamming comparative testing matrix.
4. Generate recovery statistics, comparative tables, and appropriate visualizations.
5. Evaluate the relationship between encoded-length overhead and recovery performance.
6. Incorporate the validated comparative results into the final project documentation and compatibility analysis.

Any remaining independent verification of production-platform records should also be documented.

## 9. Team Meetings and Documentation

Both required Week 12 meetings were held and documented.

| Meeting | Date | Documentation |
|---|---|---|
| Monday planning meeting | November 2, 2026 | `meeting_minutes/2026-11-02_week12.md` |
| Friday progress meeting | November 6, 2026 | `meeting_minutes/2026-11-06_week12.md` |

All three team members attended Friday's meeting.

The meetings covered implementation progress, testing results, experimental methodology, GitHub contributions, documentation requirements, and outstanding deliverables.

## 10. Conclusion

Week 12 represented significant progress toward completing the project's error-correction and platform-compatibility objectives.

The team stabilized the Hamming SECDED implementation, successfully executed the expanded regression suite, completed the remaining reported production trials across three applications, and established an initial comparative experiment pilot.

Independent verification confirmed that the integrated software continued to pass its automated regression tests.

The production-testing findings also identified important differences in zero-width character preservation between applications, reinforcing the practical limitations of the steganographic approach.

Although the full comparative recovery experiment remains outstanding, the completed stabilization, testing, and documentation provide a foundation for the remaining evaluation.

**Overall Week 12 Status: Partially Completed — Core stabilization and production testing completed; full comparative recovery analysis pending.**