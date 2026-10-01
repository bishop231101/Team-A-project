# Week 7 Weekly Journal - Tristan Koch

## Project

Zero-Width Unicode Steganography with Social-Media Robustness Engineering

## Week 7 Focus

Expanded recovery testing using higher levels of controlled corruption with the five-copy recovery method

## Work Completed

During Week 7, I continued testing the improved zero-width Unicode steganography codec with the five-copy recovery method. My assigned work was to expand the controlled corruption testing to higher corruption levels, collect recovery and survival statistics, capture screenshots and testing evidence, and document the results for comparison with the previous Week 5 and Week 6 recovery testing.

I created a separate Week 7 testing script based on the controlled corruption approach used during the Week 6 testing. The script was designed to run the expanded corruption scenarios, record the number of zero-width characters before and after corruption, calculate the survival rate, track removed and altered characters separately, attempt recovery, and report whether the recovered message matched the original. The Week 6 testing scripts and the codec implementation were not modified.

The Week 7 tests reused the same test messages used during the Week 6 recovery testing so that the results could be compared consistently.

The seven Week 7 recovery tests covered higher corruption levels:

* Approximately 40% zero-width character removal
* Approximately 50% zero-width character removal
* Approximately 60% zero-width character removal
* Approximately 30% zero-width character alteration
* Approximately 40% zero-width character alteration
* Approximately 50% zero-width character alteration
* Approximately 40% mixed removal and alteration

I used the Week 7 recovery testing script to encode each message with the five-copy recovery mode, apply controlled corruption, attempt to recover the hidden message, and record the resulting character counts, survival rate, recovery result, and any decoding errors.

The Week 7 testing script was run from the repository root using:

`python tests/week7_testing/run_tristan_expanded_recovery_tests.py`

## Testing and Results

A total of seven Week 7 recovery tests were completed using the improved five-copy recovery codec.

The removal tests showed different recovery behavior as the corruption level increased. The 40% removal test successfully recovered `Hello` with a 66.83% survival rate. The 50% removal test resulted in a 58.46% survival rate but failed to recover `Zero Width Test`. The 60% removal test resulted in a 50.15% survival rate and also failed to recover `CS481 Test 123!`.

![Week 7 Test 1 terminal results](/tests/week7_testing/screenshots/tristan/Week7_Test1.png)

*Figure 1. Terminal evidence for the 40% removal test. The test removed 272 zero-width characters, leaving a 66.83% survival rate, and successfully recovered the original `Hello` message.*

![Week 7 Test 2 terminal results](/tests/week7_testing/screenshots/tristan/Week7_Test2.png)

*Figure 2. Terminal evidence for the 50% removal test. The test removed 540 zero-width characters, leaving a 58.46% survival rate. The recovery decoder failed with a missing or malformed bit group.*

![Week 7 Test 3 terminal results](/tests/week7_testing/screenshots/tristan/Week7_Test3.png)

*Figure 3. Terminal evidence for the 60% removal test. The test removed 648 zero-width characters, leaving a 50.15% survival rate. The recovery decoder failed with a missing or malformed bit group.*

The alteration tests also showed a change in recovery behavior at higher corruption levels. The 30% alteration test successfully recovered the original message with a 100.00% survival rate. The 40% alteration test also successfully recovered its message with a 100.00% survival rate. The 50% alteration test retained all zero-width characters and therefore also had a 100.00% survival rate, but the altered payload failed to decode.

![Week 7 Test 4 terminal results](/tests/week7_testing/screenshots/tristan/Week7_Test4.png)

*Figure 4. Terminal evidence for the 30% alteration test. The test altered 636 zero-width characters without removing any, resulting in a 100.00% survival rate. The recovery decoder successfully recovered the original message.*

![Week 7 Test 5 terminal results](/tests/week7_testing/screenshots/tristan/Week7_Test5.png)

*Figure 5. Terminal evidence for the 40% alteration test. The test altered 288 zero-width characters without removing any, resulting in a 100.00% survival rate. The recovery decoder successfully recovered `Team A`.*

![Week 7 Test 6 terminal results](/tests/week7_testing/screenshots/tristan/Week7_Test6.png)

*Figure 6. Terminal evidence for the 50% alteration test. The test altered 340 zero-width characters without removing any, so the survival rate remained 100.00%. However, the recovery decoder failed with an unrecognized format marker.*

The mixed corruption test combined removal and alteration at approximately 40% of the recoverable data symbols. The test removed 136 zero-width characters and altered another 136 characters. The resulting survival rate was 83.41%, and the original `CS481` message was successfully recovered.

![Week 7 Test 7 terminal results](/tests/week7_testing/screenshots/tristan/Week7_Test7.png)

*Figure 7. Terminal evidence for the 40% mixed corruption test. The test removed 136 zero-width characters and altered another 136, resulting in an 83.41% survival rate. The recovery decoder successfully recovered `CS481`.*

Overall, four of the seven Week 7 recovery tests successfully recovered their original hidden messages, while three tests resulted in decoding failure. The successful tests were the 40% removal, 30% alteration, 40% alteration, and 40% mixed corruption scenarios.

## Evidence and Documentation

I recorded the original zero-width character count, remaining zero-width character count, number of characters removed, number of characters altered, actual corruption percentage, survival rate, decode result, recovered message, and any decoding error for each Week 7 recovery test.

I captured terminal screenshots for all seven tests and organized them in the Week 7 testing screenshots folder under the Tristan subfolder. The screenshots were included directly in the Week 7 testing results document and in this weekly journal as evidence of the testing results.

I created and documented `week7_tristan_expanded_testing_results.md` to record the testing procedure, test messages, measurements, individual test results, screenshots, and comparison with the Week 5 and Week 6 recovery testing.

## What I Learned

This week's testing demonstrated how the recovery behavior of the five-copy method changes as the amount of controlled corruption increases.

The removal tests showed that the codec successfully recovered the original message at 40% removal, but the 50% and 60% removal tests failed to recover their messages. This provided additional information about recovery behavior at higher levels of zero-width character removal.

The alteration tests showed that the codec successfully recovered the original messages at 30% and 40% alteration. At 50% alteration, the zero-width character survival rate remained 100.00% because no characters were removed, but the recovery decoder still failed. This reinforced that character survival and successful message recovery are separate measurements.

The mixed corruption test showed that the codec was able to recover the original message when 40% of the recoverable data symbols were corrupted through a combination of removal and alteration.

Comparing the Week 7 results with Week 6 also showed that increasing the corruption level can change a previously successful recovery process into a decoding failure. This provides additional data for evaluating the behavior of the five-copy recovery method under higher controlled corruption levels.

## Problems and Challenges

One challenge during the Week 7 testing was expanding the corruption levels while keeping the testing procedure consistent with the Week 6 results. The same general controlled corruption approach and test messages were used so that the Week 7 results could be compared with the previous testing.

Another challenge was interpreting alteration results correctly. In alteration tests, zero-width characters were changed rather than removed, so the zero-width character survival rate remained 100.00%. However, the altered data could still fail to decode, as demonstrated by the 50% alteration test.

The higher corruption levels also produced decoding failures that needed to be documented accurately rather than treated as errors in the testing process. Recording the decoder's error messages provides additional evidence about how the recovery method behaves when the corruption becomes too severe for successful recovery under the tested conditions.

I also needed to organize seven separate terminal screenshots and ensure that each screenshot corresponded to the correct test scenario and result in both the testing results document and weekly journal.

## Next Steps

The next step is to incorporate the Week 7 recovery results into the team's overall project documentation and progress report.

The Week 7 results provide additional evidence about the recovery behavior of the five-copy method under higher controlled corruption levels, including both successful recovery and decoding failure scenarios.

I will continue contributing to the testing, documentation, and statistical analysis portions of the project as the team moves forward.
