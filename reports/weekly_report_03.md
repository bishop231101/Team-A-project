# Week 3 Progress Report

## Team A

### Week 3 Objective
The objective for Week 3 was to implement the initial zero-width Unicode encoder/decoder, establish testing procedures, and verify that hidden messages could be encoded and decoded without changing the visible cover text.

## Work Completed

### Henry
- Implemented the initial zero-width Unicode encoder and decoder.
- Created automated unit tests for the codec.
- Verified reusable test vectors, deterministic encoding, invalid argument handling, missing payload rejection, truncated payload rejection, and unchanged visible cover text.
- All 6 automated unit tests passed successfully.

### Tristan
- Conducted manual testing of the zero-width encoder and decoder.
- Tested 9 different message types, including basic text, course/team identifiers, numbers, longer messages, multiple spaces, special characters, and mixed content.
- Verified that decoded messages matched the original messages.
- Verified that the visible cover text remained unchanged.
- Documented the results and provided screenshots as testing evidence.
- All 9 manual tests passed.

### Ifeanyi
- Coordinated Week 3 team activities and monitored completion of assigned tasks.
- Reviewed and merged team member pull requests into the main branch.
- Resolved the Git merge conflict that occurred during integration.
- Reviewed testing results and evidence submitted by team members.
- Performed integration testing after merging the Week 3 work.
- Confirmed that all 6 automated tests still passed after integration.

## Testing and Results

The team completed both automated and manual testing during Week 3.

- Automated tests: 6 passed, 0 failed.
- Manual tests: 9 passed, 0 failed.
- Integrated test run: 6 passed, 0 failed.
- Visible cover text remained unchanged during testing.
- Decoded messages matched the original messages.

Overall, the Week 3 implementation and testing were successful.

## Problems Encountered

A Git merge conflict occurred in the `.gitignore` file after one team member's work was merged into the main branch. The affected branch was updated with the latest version of `main`, the conflict was resolved, and the pull request was successfully merged.

The team also had to coordinate development and testing so that testing could be completed after the initial encoder/decoder implementation became available.

## Evidence

Testing evidence is stored in the `week3_testing/screenshots` directory. The repository also contains the Week 3 testing results, automated unit tests, and individual weekly journals.

## Lessons Learned

This week demonstrated the importance of testing software with multiple types of input instead of relying on a single example. The team also gained additional experience using Git branches, pull requests, merge conflict resolution, and integration testing.

The successful test results showed that the initial zero-width Unicode codec can encode and recover hidden messages while preserving the visible cover text.

## Plan for Week 4

During Week 4, the team will continue according to the semester project plan and begin expanding platform testing. The team will use the Week 3 codec and testing results as the baseline for evaluating how encoded messages behave when transferred through different platforms. Testing results and evidence will continue to be documented in the repository.

## Progress Compared to Project Plan

The team is progressing according to the semester project plan. During Week 3, we completed the initial encoder/decoder implementation and testing as planned. The successful results provide the baseline needed to begin expanded platform testing during Week 4. No major adjustment to the semester plan is required at this time.