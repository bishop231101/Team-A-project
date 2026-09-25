# Week 6 Progress Report

## Project
Zero-Width Unicode Steganography with Social-Media Robustness Engineering

## Week 6 Objective
The main objective for Week 6 was to improve the robustness of the zero-width Unicode steganography system by introducing and testing a recovery method for corrupted encoded messages. The team continued building on the recovery-testing results from Week 5.

## Work Completed

### Ifeanyi Emeka
- Ran the complete automated test suite to verify the current project code.
- Confirmed that 19 tests and 108 subtests passed successfully.
- Tested the repetition-based recovery method for the zero-width Unicode codec.
- Intentionally corrupted one repeated symbol to evaluate whether the original hidden message could still be recovered.
- Successfully recovered the original secret after the intentional corruption.
- Documented the Week 6 recovery testing results.
- Captured screenshot evidence of the baseline automated tests and successful recovery test.
- Completed the Week 6 meeting documentation and individual weekly journal.

### Henry Smith
- Implemented the Week 6 recovery improvements for the zero-width Unicode codec.
- Worked on the repetition-based recovery method used to improve message recovery after corruption.
- Tested the improved recovery implementation and documented his Week 6 contribution.
- Completed his Week 6 individual weekly journal.

### Tristan Koch
- Created the Week 6 recovery testing script.
- Conducted six controlled corruption scenarios using removal, alteration, and mixed corruption.
- Tested approximately 10%, 20%, and 30% zero-width character removal.
- Tested approximately 10% and 20% zero-width character alteration.
- Conducted a mixed removal and alteration test.
- Documented the recovery results and compared them with the Week 5 baseline.
- Captured screenshot evidence for the Week 6 recovery tests.
- Completed his Week 6 individual weekly journal.

## Milestones and Deliverables

Major Week 6 deliverables completed included:

- Running the complete automated test suite and confirming 19 tests and 108 subtests passed.
- Evaluating the repetition-based recovery method implemented in the zero-width Unicode codec.
- Conducting an intentional corruption test by modifying one repeated symbol.
- Successfully recovering the original hidden message after the corruption.
- Documenting the recovery test results in `week6_recovery_testing_results.md`.
- Capturing baseline automated-test evidence in `week6_baseline_tests.png`.
- Capturing successful recovery-test evidence in `week6_recovery_test.png`.
- Completing the Week 6 meeting documentation.
- Completing all three team member's Week 6 individual journal.
- Integrating Henry Smith's Week 6 recovery implementation and testing contribution.
- Completing six controlled recovery scenarios covering zero-width character removal, alteration, and mixed corruption.
- Successfully recovering the original hidden messages during Tristan Koch's six Week 6 recovery tests.
- Comparing the Week 6 recovery results with the Week 5 baseline.
- Capturing and documenting Tristan Koch's Week 6 recovery-test evidence.
- Completing all three team members' Week 6 individual weekly journals.
- Reviewing and merging Henry Smith's and Tristan Koch's Week 6 pull requests into `main`.
## Detailed Testing Evidence

The Week 6 baseline automated test suite was executed before evaluating the recovery method. The test run completed successfully with 19 tests and 108 subtests passing. This confirmed that the existing codec functionality remained operational before recovery testing.

The Week 6 recovery test evaluated the repetition-based recovery method. The secret message `Week 6 recovery test` was encoded using recovery mode, and one repeated symbol was intentionally corrupted to simulate damage to the encoded payload.

The decoder successfully used the remaining repeated symbols to determine the majority bit value and recover the original secret.

| Test | Expected Result | Actual Result | Status |
|---|---|---|---|
| Baseline automated tests | Existing tests pass | 19 tests and 108 subtests passed | PASS |
| Single-symbol corruption | Original secret is recovered | `Week 6 recovery test` recovered successfully | PASS |

Screenshot evidence is stored in:

- `tests/week6_testing/screenshots/week6_baseline_tests.png`
- `tests/week6_testing/screenshots/week6_recovery_test.png`

These results demonstrate that the repetition-based recovery method can tolerate a single corrupted symbol within a protected bit group while still recovering the original hidden message.
### Extended Week 6 Recovery Testing

After the initial recovery test, Tristan Koch conducted six additional controlled corruption scenarios using the improved five-copy recovery method. The testing included zero-width character removal, alteration, and mixed corruption.

| Test | Corruption Scenario | Survival Rate | Recovery Result |
|---|---|---:|---|
| 1 | 10% removal | 91.71% | PASS |
| 2 | 20% removal | 83.38% | PASS |
| 3 | 30% removal | 75.08% | PASS |
| 4 | 10% alteration | 100.00% | PASS |
| 5 | 20% alteration | 100.00% | PASS |
| 6 | 30% mixed removal and alteration | 87.56% | PASS |

All six tests successfully recovered the original hidden messages. The results demonstrate that the five-copy recovery method improved the codec's ability to tolerate controlled corruption compared with the Week 5 baseline.

Detailed results and screenshot evidence are stored in:

- `tests/week6_testing/week6_tristan_recovery_testing_results.md`
- `tests/week6_testing/screenshots/tristan/`


## Lessons Learned

Week 6 demonstrated that adding redundancy can improve the ability of the codec to recover from limited corruption. The repetition-based method stores each bit multiple times, allowing the decoder to use the majority value when one symbol in a protected bit group is corrupted.

The completed Week 6 testing showed a clear improvement over the Week 5 baseline. The improved five-copy recovery method successfully recovered the original hidden messages in all six controlled corruption scenarios, including removal, alteration, and mixed corruption.

The team also learned that survival rate alone does not determine whether a hidden message can be recovered. Even when the zero-width character survival rate decreased to 75.08% during the 30% removal test, the original message was still successfully recovered. Running the complete automated test suite and controlled corruption tests helped confirm both normal codec functionality and the effectiveness of the new recovery method.

## Progress Compared to Project Plan

The Week 6 work continued the robustness improvements identified in the Week 5 progress report. Week 5 established the baseline behavior of the codec when zero-width characters were removed or altered, while Week 6 implemented and evaluated the five-copy recovery method.

The team successfully tested the improved recovery method through controlled corruption scenarios involving zero-width character removal, alteration, and mixed corruption. All six recovery tests successfully recovered the original hidden messages, demonstrating significant progress toward improving the robustness of the zero-width Unicode steganography system.

The team completed the planned Week 6 recovery implementation, testing, documentation, weekly journals, and integration of individual contributions. The project remains on track for continued testing and refinement during Week 7.

## Next Steps

During Week 7, the team will continue evaluating the robustness of the five-copy recovery method and compare additional testing results with the Week 5 baseline and Week 6 recovery results.

Additional corruption scenarios will be tested to identify the limits of the current recovery method, including higher levels of removal, alteration, and mixed corruption.

The team will continue automated testing, documentation, weekly journals, meeting minutes, and integration of individual contributions as the project progresses.