# Week 6 Test Plan

## Project
Zero-Width Unicode Steganography with Social-Media Robustness Engineering

## Week 6 Objective
The objective of Week 6 is to improve the robustness of the zero-width Unicode steganography system by investigating methods that can recover hidden messages when zero-width characters are removed or altered.

## Week 6 Tasks

### Ifeanyi Emeka
- Coordinate Week 6 testing and integration.
- Establish the Week 5 recovery results as the baseline.
- Test and compare recovery performance after redundancy or error-correction improvements are implemented.
- Document testing results and screenshots.
- Complete Week 6 meeting minutes and individual weekly journal.

### Henry Smith
- Investigate and implement a redundancy or error-correction method for the zero-width Unicode codec.
- Evaluate repetition and/or Reed-Solomon error correction.
- Integrate the selected method with the existing encoder/decoder.
- Test the updated code.
- Complete Week 6 individual weekly journal.

### Tristan Koch
- Develop additional corruption and recovery test cases.
- Test removal and alteration of zero-width characters against the improved codec.
- Compare recovery behavior with the Week 5 baseline.
- Document testing evidence and results.
- Complete Week 6 individual weekly journal.

## Testing Plan
The Week 5 recovery tests will serve as the baseline. The team will repeat similar corruption scenarios after implementing redundancy or error correction.

The following scenarios will be evaluated:

1. Approximately 10% zero-width character removal.
2. Approximately 20% zero-width character removal.
3. Approximately 30% zero-width character removal.
4. Approximately 10% zero-width character alteration.
5. Approximately 20% zero-width character alteration.
6. Mixed removal and alteration.

For each test, the team will record:
- Original hidden message.
- Corruption method.
- Approximate corruption percentage.
- Survival rate.
- Decode result.
- Recovered message, if successful.
- Screenshot evidence.

## Expected Deliverables
- Updated encoder/decoder or recovery implementation.
- Week 6 recovery test results.
- Automated testing results.
- Screenshot evidence.
- Two Week 6 meeting records.
- Individual Week 6 journals.
- Week 6 progress report.
- GitHub commits from each team member.

## Success Criteria
Week 6 will be considered successful if the team implements and evaluates at least one method intended to improve recovery of corrupted zero-width payloads and compares the results with the Week 5 baseline.