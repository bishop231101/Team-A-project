# Week 5 Progress Report

## Project
Zero-Width Unicode Steganography with Social-Media Robustness Engineering

## Week 5 Objective
The main objective for Week 5 was to continue platform robustness testing across additional platforms and evaluate the ability of the zero-width Unicode codec to recover hidden messages when zero-width characters are removed or altered.

## Work Completed

### Ifeanyi Emeka
- Tested the current project code and identified a Python package naming conflict caused by the `code` directory.
- Resolved the conflict by renaming the package from `code` to `src` and updating the test imports.
- Ran the automated test suite after the fix.
- Verified that 19 tests and 108 subtests passed successfully.
- Conducted and documented Week 5 platform and recovery testing.
- Completed the Week 5 weekly journal.

### Henry Smith
- Continued work on the zero-width Unicode encoder/decoder and supporting project code.
- Contributed to Week 5 project development and testing activities.
- Provided testing evidence in the Week 5 screenshot folder.
- Completed his Week 5 weekly journal.

### Tristan Koch
- Continued supporting platform testing and project documentation.
- Contributed to the team's Week 5 testing activities.
- Continued work related to platform compatibility and robustness evaluation.
- Completed his Week 5 weekly journal.

## Milestones and Deliverables
During Week 5, the team continued the testing phase of the project and expanded platform compatibility testing.

Major Week 5 deliverables included:

- Testing Microsoft Outlook, Telegram Web, and Notepad++.
- Completing 27 platform tests using nine test messages on each of the three platforms.
- Documenting platform testing results in `week5_platform_testing_results.md`.
- Conducting four recovery tests involving removal and alteration of zero-width characters.
- Documenting recovery testing results in `week5_recovery_testing_results.md`.
- Capturing screenshots and testing evidence.
- Fixing the Python package naming conflict.
- Running the automated test suite after the project structure change.
- Completing individual Week 5 journals.

## Detailed Testing Evidence
Week 5 platform robustness testing used the same nine test messages from previous testing so that the results could be compared consistently.

A total of 27 platform tests were completed across Microsoft Outlook, Telegram Web, and Notepad++. Each platform was tested with nine encoded messages.

| Platform | Tests | Successful Decodes | Failed Decodes | Average Survival Rate | Overall Result |
|---|---:|---:|---:|---:|---|
| Microsoft Outlook | 9 | 9 | 0 | 100.00% | PASS |
| Telegram Web | 9 | 9 | 0 | 100.00% | PASS |
| Notepad++ | 9 | 9 | 0 | 100.00% | PASS |

All three platforms preserved the complete zero-width payload across all nine test messages. All 27 hidden messages were successfully recovered and decoded with no zero-width characters lost or corrupted during the platform tests.

Week 5 also included recovery testing to determine whether the hidden messages could still be decoded after intentional removal or alteration of zero-width characters.

| Test | Scenario | Survival Rate | Decode Result |
|---|---|---:|---|
| 1 | Approximately 30% removal | 69.08% | FAILED |
| 2 | 50% removal | 50.00% | FAILED |
| 3 | Approximately 30% alteration | 100.00% | FAILED |
| 4 | Approximately 20% removal + approximately 20% alteration | 79.83% | FAILED |

All four corruption scenarios resulted in decode failure. The alteration test was especially important because all zero-width characters remained present, producing a 100.00% survival rate, but changing approximately 30% of the characters still prevented successful decoding.

The automated test suite was also executed after resolving the Python package naming conflict. The updated project successfully passed 19 tests and 108 subtests.

Detailed Week 5 testing results and screenshot evidence are available in the `week5_testing/` folder of the repository.

## Lessons Learned
The team learned that platform compatibility and payload integrity are two different issues. Microsoft Outlook, Telegram Web, and Notepad++ preserved the tested zero-width characters and allowed successful recovery of all hidden messages.

However, the recovery tests showed that the current codec is vulnerable when zero-width characters are removed or altered. Even when all characters remain present, changing the zero-width character values can make the encoded payload undecodable.

The team also learned the importance of project structure in Python. Using a package name that conflicts with a Python standard library module can cause import errors. Renaming the package and rerunning the automated tests confirmed that the project continued to function correctly after the change.

## Progress Compared to Project Plan
The team completed the planned Week 5 platform compatibility testing, recovery testing, documentation, and project integration activities. Testing was expanded to Microsoft Outlook, Telegram Web, and Notepad++, and recovery testing established a baseline for how the current codec responds to zero-width-character corruption.

The project continues to progress according to the semester plan. The Week 5 results identified an important limitation of the current codec: successful platform preservation does not guarantee recovery when the hidden payload is modified.

## Next Steps
During Week 6, the team will use the Week 5 results to continue improving the robustness of the zero-width Unicode steganography system.

The team will investigate redundancy and error-correction methods that may improve recovery when zero-width characters are removed or altered. Future testing will evaluate whether techniques such as repetition and Reed-Solomon error correction can improve recovery compared with the Week 5 baseline.

The team will also continue automated testing, documentation, weekly journals, meeting minutes, and GitHub integration as the project progresses.