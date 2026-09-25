# Week 6 Weekly Journal - Tristan Koch

## Project

Zero-Width Unicode Steganography with Social-Media Robustness Engineering

## Week 6 Focus

Recovery testing using the improved zero-width Unicode codec with redundancy

## Work Completed

During Week 6, I focused on testing the improved zero-width Unicode steganography codec after the addition of repetition-based recovery. My assigned work was to develop additional corruption and recovery test cases, test the removal and alteration of zero-width characters, compare the recovery behavior with the Week 5 baseline, and document the testing evidence and results.

After reviewing Henry's Week 6 recovery demonstration script, I used it as a reference for the controlled corruption approach and used Codex to assist in creating a separate testing script tailored to my assigned Week 6 test scenarios. The script was designed to run my six tests, record the number of zero-width characters before and after corruption, calculate the survival rate, track removed and altered characters separately, attempt recovery, and report whether the recovered message matched the original. Henry's demonstration script and the codec implementation were not modified.

I reused the four test messages from the Week 5 recovery baseline so that the results could be compared consistently:

* `Hello`
* `Zero Width Test`
* `CS481 Test 123!`
* `This is a longer test message for Week 3.`

I also added two additional test messages from the previous Week 4 testing:

* `Team A`
* `CS481`

The six Week 6 recovery tests covered the scenarios specified in the Week 6 test plan:

* Approximately 10% zero-width character removal
* Approximately 20% zero-width character removal
* Approximately 30% zero-width character removal
* Approximately 10% zero-width character alteration
* Approximately 20% zero-width character alteration
* A mixed 30% removal and alteration scenario

I used the project's Week 6 recovery testing script to encode each message with the improved five-copy recovery mode, apply controlled corruption, attempt to recover the hidden message, and record the resulting character counts, survival rate, and recovery result.

## Testing and Results

A total of six Week 6 recovery tests were completed using the improved codec.

The removal tests successfully recovered all three messages. The 10% removal test resulted in a 91.71% survival rate, the 20% removal test resulted in an 83.38% survival rate, and the 30% removal test resulted in a 75.08% survival rate. In all three cases, the recovered message matched the original message.

The alteration tests also successfully recovered both messages. The 10% alteration test had a 100.00% survival rate because no zero-width characters were removed, while 212 characters were altered. The 20% alteration test also had a 100.00% survival rate, with 144 characters altered. Both altered messages were successfully recovered and matched their original messages.

The mixed corruption test combined removal and alteration at approximately 30% of the recoverable data symbols. This resulted in 102 zero-width characters being removed and 102 being altered. The resulting survival rate was 87.56%, and the original `CS481` message was successfully recovered.

Overall, all six Week 6 recovery tests passed. Unlike the Week 5 baseline, where all four tested corruption scenarios resulted in decode failure, the improved codec successfully recovered every Week 6 test message.

## Evidence and Documentation

I recorded the original zero-width character count, remaining zero-width character count, number of characters removed, number of characters altered, survival rate, decode result, and recovered message for each Week 6 recovery test.

I also captured terminal screenshots for each test and organized them in the Week 6 testing screenshots folder under the Tristan subfolder. The screenshots were included directly in the Week 6 testing results document with explanations of what each screenshot demonstrates.

I created and documented `week6_tristan_recovery_testing_results.md` to record the testing procedure, test messages, measurements, individual test results, screenshots, and comparison with the Week 5 recovery baseline.

## What I Learned

This week's testing demonstrated the difference that redundancy can make when recovering corrupted zero-width Unicode data. The Week 5 baseline showed that the original codec failed to recover messages after the tested removal and alteration scenarios. In Week 6, the improved codec successfully recovered every tested message despite controlled corruption.

The removal tests demonstrated that the codec could recover the original messages even when approximately 10%, 20%, and 30% of the recoverable data symbols were removed.

The alteration tests also showed that the codec could recover the original messages when zero-width characters were changed without being removed. Although the survival rate remained 100.00% because the altered characters were still present, the improved recovery method was able to correct the changes and recover the original messages.

The mixed corruption test further demonstrated that the recovery method could handle both removed and altered zero-width characters within the same corrupted payload.

## Problems and Challenges

One challenge during the Week 6 testing was ensuring that the new recovery tests could be compared meaningfully with the Week 5 baseline. I reused the same four Week 5 test messages for the corresponding Week 6 scenarios and added two messages from the Week 4 test cases for the additional Week 6 scenarios.

Another challenge was working with invisible zero-width characters while applying controlled corruption. The testing script was used to apply the specified removal and alteration percentages consistently while preserving the structure needed for the recovery decoder.

I also needed to carefully document the difference between character survival and successful recovery. In the alteration tests, the zero-width character survival rate remained 100.00% because characters were altered rather than removed, but the altered payload still required the recovery mechanism to restore the original hidden message.

## Next Steps

The next step is to incorporate the Week 6 recovery results into the team's overall project documentation and progress report.

The Week 6 results provide evidence that the added redundancy and recovery mechanism improved recovery performance under the controlled corruption scenarios tested in Week 6.

I will continue contributing to the testing, documentation, and statistical analysis portions of the project as the team moves forward.
