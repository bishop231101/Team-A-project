# Week 4 Progress Report

## Project
Zero-Width Unicode Steganography with Social-Media Robustness Engineering

## Week 4 Objective
The main objective for Week 4 was to conduct platform robustness testing using the test cases developed during Week 3, document the results, and evaluate how well zero-width Unicode characters survive across different platforms.

## Work Completed

### Henry Smith
- Continued development and testing support for the zero-width Unicode encoder/decoder.
- Improved codec validation and testing.
- Addressed issues related to the project's code and testing.
- Completed his Week 4 journal.

### Tristan Koch
- Conducted platform robustness testing on Gmail, Discord, and Microsoft Word.
- Used all 9 Week 3 test messages on each platform.
- Completed a total of 27 platform tests.
- Recorded zero-width character survival rates and decoding results.
- Captured screenshots as testing evidence.
- Documented the Week 4 testing procedure and results.
- Completed his Week 4 journal.

### Ifeanyi Emeka
- Coordinated Week 4 activities and monitored team progress.
- Reviewed team members' commits, documentation, and pull requests.
- Reviewed and merged completed contributions into the main branch.
- Reviewed platform testing results and supporting evidence.
- Maintained the Week 4 meeting minutes and project documentation.
- Performed integration checks after the team's contributions were merged.

## Testing Results

The Week 4 platform testing produced clear differences among the three platforms.

- **Discord:** All 9 tests achieved a 100% zero-width character survival rate. The encoded information was preserved successfully.
- **Gmail:** Zero-width character survival rates ranged from approximately 42.11% to 50.63%. A substantial portion of the hidden characters was removed.
- **Microsoft Word:** Zero-width character survival rates also ranged from approximately 42.11% to 50.63%. A substantial portion of the hidden characters was removed.

The results demonstrate that the reliability of zero-width Unicode steganography depends heavily on how a platform processes Unicode characters.

## Problems and Challenges

The primary challenge was that some platforms removed or altered invisible Unicode characters during transfer or processing. This prevented reliable decoding even though the encoder/decoder worked correctly during local testing.

The team also had to carefully organize screenshots, test results, and documentation so that each platform test could be reviewed and compared.

## Week 4 Accomplishments

- Completed 27 platform robustness tests.
- Tested Gmail, Discord, and Microsoft Word.
- Established initial platform survival-rate data.
- Documented the testing procedure and results.
- Collected screenshot evidence.
- Continued improving codec validation and testing.
- Maintained individual weekly journals and team documentation.

## Detailed Testing Evidence

Week 4 platform robustness testing used the nine test messages developed during Week 3. Each message was encoded using the zero-width Unicode encoder, transferred through the selected platform, retrieved, and decoded. The original and recovered payloads were then compared to determine character survival and successful recovery.

A total of 27 tests were completed across Gmail, Discord, and Microsoft Word. Screenshots were captured during testing to document the platform behavior, encoded payloads, and resulting output. The detailed testing procedure, results, and screenshot evidence are available in the `week4_testing/` folder of the repository.

## Lessons Learned

The team learned that successful local encoding and decoding does not guarantee successful recovery after the message passes through another platform. Discord preserved the tested zero-width characters, while Gmail and Microsoft Word removed or altered a significant portion of them. This showed that platform-specific Unicode processing is a major factor in the reliability of zero-width steganography.

## Progress Compared to Project Plan

The team completed the planned Week 4 platform testing, documentation, integration, and weekly reporting activities. The project remains aligned with the semester project plan. Based on the Week 4 results, Week 5 will focus on additional platform compatibility testing and methods for improving payload recovery when zero-width characters are removed or altered.

## Next Steps

During Week 5, the team will review the Week 4 results and determine the next testing and development priorities. The team will continue investigating platform compatibility and methods for improving payload recovery when zero-width characters are removed or altered.