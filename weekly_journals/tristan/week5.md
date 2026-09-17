# Week 5 Weekly Journal - Tristan Koch

## Project

Zero-Width Unicode Steganography with Social-Media Robustness Engineering

## Week 5 Focus

Additional platform robustness testing and recovery testing

## Work Completed

During Week 5, I continued testing how well the project's zero-width Unicode steganography codec survives when encoded messages are transferred through different platforms. I also performed recovery testing to evaluate how the codec responds when zero-width Unicode characters are intentionally removed or altered.

I tested three additional platforms assigned for Week 5:

* Microsoft Outlook
* Telegram Web
* Notepad++

For each platform, I ran all 9 test messages using the same general testing methodology from Week 4. The testing process involved generating an encoded message with the project's Python codec, transferring or saving the encoded message through the selected platform, retrieving the resulting text, measuring how many zero-width characters survived, and attempting to decode the recovered payload.

I also completed four recovery tests using intentionally corrupted encoded messages. These tests evaluated partial zero-width character removal, greater character removal, character alteration, and a combination of removal and alteration.

## Testing and Results

A total of 27 additional platform tests were completed during Week 5.

Microsoft Outlook successfully preserved all zero-width characters in every test. All 9 Outlook tests had a 100.00% survival rate, and all 9 recovered messages decoded successfully.

Telegram Web also successfully preserved all zero-width characters in every test. All 9 Telegram Web tests had a 100.00% survival rate, and all 9 recovered messages decoded successfully.

Notepad++ successfully preserved all zero-width characters in every test. All 9 Notepad++ tests had a 100.00% survival rate, and all 9 recovered messages decoded successfully.

Overall, all 27 Week 5 platform tests passed, with a 100.00% survival rate and no failed decodes.

The recovery testing produced different results. In Test 1, approximately 30% of the zero-width characters were removed, resulting in a 69.08% survival rate and a failed decode. Test 2 removed 50% of the zero-width characters, resulting in a 50.00% survival rate and a failed decode. Test 3 altered approximately 30% of the zero-width characters without removing them. The survival rate remained 100.00%, but the altered payload failed to decode. Test 4 combined approximately 20% removal with approximately 20% alteration. The resulting survival rate was 79.83%, and the payload failed to decode.

## Evidence and Documentation

I recorded the number of zero-width characters sent and recovered for each platform test and calculated the survival rate. I also recorded whether decoding succeeded or failed and documented the results of the additional platform testing.

Screenshots were captured as evidence of the platform testing and recovery testing. The platform screenshots were organized into separate folders for Microsoft Outlook, Telegram, and Notepad++. The recovery screenshots were organized in the recovery folder.

I also created and documented `week5_platform_testing_results.md` and `week5_recovery_testing_results.md` to record the procedures, measurements, results, and conclusions from the Week 5 testing.

## What I Learned

This week's testing reinforced the importance of testing a steganography codec across multiple platforms rather than assuming that encoded data will behave the same way everywhere. Microsoft Outlook, Telegram Web, and Notepad++ preserved the zero-width characters in all of the tests performed this week.

The recovery testing also helped me understand the difference between character survival and successful data recovery. In the alteration test, all of the zero-width characters remained present, resulting in a 100.00% survival rate, but changing approximately 30% of the characters still caused decoding to fail.

I also learned that intentional corruption testing provides a useful baseline for evaluating the effectiveness of redundancy and error-correction techniques. The current codec was unable to recover the tested messages after the corruption scenarios used this week.

## Problems and Challenges

One challenge during the recovery testing was working with invisible Unicode characters while intentionally removing or altering them. The testing required carefully tracking the original and damaged zero-width character counts so that the resulting survival rates could be calculated accurately.

Another challenge was ensuring that the recovery tests produced controlled levels of corruption while leaving the visible cover text unchanged. Using Python commands to modify the encoded data allowed the removal and alteration scenarios to be measured consistently.

I also had to keep the platform testing and recovery testing results organized separately so that the screenshots and measurements could be clearly associated with the correct test scenarios.

## Next Steps

The next step is to review the Week 5 platform and recovery testing results with the team and incorporate the relevant findings into the project report.

The recovery results provide a baseline for evaluating whether the project's planned redundancy and Reed-Solomon error-correction techniques can improve recovery when zero-width characters are removed or altered.

I will continue contributing to the testing, documentation, and statistical analysis portions of the project as the team moves forward.