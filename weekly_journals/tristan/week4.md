# Week 4 Weekly Journal - Tristan Koch

## Project

Zero-Width Unicode Steganography with Social-Media Robustness Engineering

## Week 4 Focus

Platform robustness testing

## Work Completed

During Week 4, I focused on testing how well the project's zero-width Unicode steganography codec survives when encoded messages are transferred through different platforms. I used the Week 3 test messages and followed the testing procedure established by the team.

I tested three platforms assigned for Week 4:

* Gmail
* Discord
* Microsoft Word

For each platform, I ran all 9 Week 3 test messages. The testing process involved generating an encoded message with the project's Python codec, transferring or saving the encoded message through the selected platform, retrieving the resulting text, measuring how many zero-width characters survived, and attempting to decode the recovered payload.

## Testing and Results

A total of 27 platform tests were completed during Week 4.

Discord successfully preserved all zero-width characters in every test. All 9 Discord tests had a 100.00% survival rate, and all 9 recovered messages decoded successfully and matched their original messages.

Gmail removed a substantial portion of the zero-width characters in every test. Survival rates ranged from 42.11% to 50.63%, and none of the 9 recovered payloads could be decoded successfully.

Microsoft Word also removed a substantial portion of the zero-width characters. Survival rates ranged from 42.11% to 50.63%, and none of the 9 recovered payloads could be decoded successfully.

These results showed a significant difference in zero-width Unicode preservation between the tested platforms. Discord was reliable for the current codec, while Gmail and Microsoft Word were not.

## Evidence and Documentation

I recorded the number of zero-width characters sent and recovered for each test and calculated the survival rate. I also recorded whether decoding succeeded or failed and documented the decoder errors when the recovered payload was incomplete or malformed.

Screenshots were captured as evidence of the testing process and results. Platform-specific screenshots were organized into separate folders for Gmail, Discord, and Microsoft Word.

I also documented the overall results and comparison between the three tested platforms in the Week 4 testing documentation.

## What I Learned

This week's testing helped me understand that a steganography codec can work correctly during local testing but still fail when its encoded data passes through another application or platform. Zero-width Unicode characters can be removed or altered during transfers, saving, or other processing.

I also learned the importance of measuring platform behavior rather than only checking whether a decoded message succeeds. Recording the number of characters sent and recovered provided a measurable way to compare platform robustness.

The Week 4 results also provided a useful baseline for determining which platforms should be tested in future weeks and where additional robustness techniques may be necessary.

## Problems and Challenges

One challenge during testing was handling invisible Unicode characters in the Windows PowerShell environment. Printing the encoded zero-width characters directly to the terminal caused encoding problems, so I used text files and clipboard-based retrieval instead.

Another challenge was ensuring that each platform test used the same general procedure and that the results were recorded consistently. Using separate test files, screenshots, and documented measurements helped keep the testing organized.

## Next Steps

The next step is to review the Week 4 platform results with the team and determine which additional platforms or testing conditions should be evaluated. The results may also help guide future work on redundancy and error-correction techniques for improving recovery when zero-width characters are lost.

I will continue contributing to the testing, documentation, and statistical analysis portions of the project as the team moves forward.
