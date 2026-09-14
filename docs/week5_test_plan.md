# Week 5 Test and Development Plan

## Project
Zero-Width Unicode Steganography with Social-Media Robustness Engineering

## Week 5 Objective
The objective for Week 5 is to build on the Week 4 platform robustness results by investigating additional platform compatibility and identifying methods for improving payload recovery when zero-width Unicode characters are removed or altered.

## Week 4 Baseline
Week 4 testing established the following baseline:

- Discord preserved the zero-width encoded payload successfully.
- Gmail removed a significant portion of the zero-width characters.
- Microsoft Word also removed a significant portion of the zero-width characters.
- Platform-specific Unicode processing has a major effect on successful payload recovery.

These results will guide the team's Week 5 development and testing activities.

## Week 5 Tasks

### Ifeanyi Emeka - Team Leader
- Coordinate Week 5 activities and monitor team progress.
- Review Week 4 platform testing results.
- Develop and maintain the Week 5 testing and recovery strategy.
- Review and integrate team contributions.
- Maintain Week 5 meeting minutes and project documentation.
- Complete individual Week 5 journal.
- Prepare the Week 5 progress report.
- Ensure important testing screenshots are included and explained in the weekly report.

### Henry Smith - Team Member A
- Research methods for recovering damaged encoded payloads.
- Investigate an appropriate error-detection or error-correction approach.
- Continue improving the zero-width encoder/decoder.
- Test any recovery-related codec improvements.
- Document implementation and testing results.
- Complete individual Week 5 journal.

### Tristan Koch - Team Member B
- Continue platform compatibility and robustness testing.
- Test additional platforms or recovery-focused scenarios.
- Record zero-width character survival and payload recovery results.
- Capture screenshots showing important testing results.
- Document the testing procedure and findings.
- Complete individual Week 5 journal.

## Testing Strategy
Week 5 testing will compare original encoded payloads with payloads after platform processing. Testing will focus on:

1. Zero-width character survival rate.
2. Successful or unsuccessful payload decoding.
3. Differences among tested platforms.
4. The effect of removed or altered zero-width characters.
5. Whether recovery techniques improve decoding reliability.

## Evidence Requirements
Important Week 5 tests will include screenshots as evidence. Each selected screenshot used in the weekly report will include a brief explanation describing:

- What was tested.
- What the screenshot demonstrates.
- The result of the test.
- Why the result is important to the project.

## Expected Week 5 Deliverables
- Updated code or recovery research.
- Additional platform/recovery testing results.
- Testing screenshots and supporting evidence.
- Updated project documentation.
- Week 5 meeting minutes.
- Individual Week 5 journals from all team members.
- Week 5 progress report.
- Meaningful GitHub commits from each team member.

## Success Criteria
Week 5 will be successful if the team expands its understanding of platform compatibility, identifies or begins implementing a method for improving payload recovery, documents the results with supporting evidence, and remains aligned with the semester project plan.