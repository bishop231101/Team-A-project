# Week 9 Weekly Journal - Tristan Koch

## Project

Zero-Width Unicode Steganography with Social-Media Robustness Engineering

## Week 9 Focus

This week, my focus was on reviewing the Week 9 testing documentation, evaluating the proposed testing methodology, conducting preliminary WeChat feasibility tests, and documenting recommendations before official production testing begins.

## Work Completed

Reviewed the Week 9 testing protocol draft, data quality audit, and Henry’s codec validation report.

Conducted preliminary feasibility tests using WeChat Desktop version 4.1.15.12 to examine whether zero-width characters survived two operations: paste-and-copy-back and send-and-retrieve.

Tested the secret message `WeChat test message`. Both operations recovered all 278 zero-width characters, with 137 U+200B characters, 111 U+200C characters, and 30 U+200D characters. Both tests had a 100% character survival rate and successfully recovered the exact original message.

Saved screenshots of the preliminary results and documented the procedures, measurements, and findings in the [WeChat Feasibility Report](../../tests/week9_testing/preliminary_feasibility_testing_WeChat.md).

Communicated concerns about testing workload, workflow definitions, and the need to finalize the protocol and assignments before collecting official production data.

These WeChat results are preliminary feasibility findings and have not been included as official production data.

## What I Learned

Reviewing the testing documentation helped me better understand the importance of using consistent procedures and recording enough information to make platform results reproducible. Each platform and operation needs a clearly defined workflow so that results can be compared fairly. The Week 9 testing protocol and data quality audit emphasize standardized test messages, complete trial records, and consistent measurements.

I also learned that character retention and exact message recovery must be measured separately. A platform may preserve some or all zero-width characters without necessarily producing the correct decoded message. Therefore, both character counts and exact-match decoding results must be recorded.

The preliminary WeChat tests demonstrated that the two tested operations were feasible under the conditions used. However, two preliminary tests using the same message are not sufficient to establish general platform reliability or replace the planned production trials.

As a recommendation for the proposed production testing, I identified three possible operations depending on each platform's functionality:

* Paste and Copy Back - Paste the encoded message into the platform, copy the resulting text back, and record the recovered text for character counting and decoding.
* Send and Retrieve (messaging platforms) - Paste the encoded message into a message or email composition window, send it, and retrieve the delivered message text for character counting and decoding.
* Save and Reopen (text editors) - Paste the encoded message into a text editor, save the document using an agreed naming convention, reopen it, and retrieve the text for character counting and decoding.

To help ensure reliable and reproducible results, I recommend using a consistent trial-naming convention to organize results and supporting evidence. 

For example, a Microsoft Word trial using Long Unicode test case LU01, repetition 1, could use the identifier MSW_LU01_01.

This is a proposed naming convention and would need to be agreed upon by the team.

These operations and the proposed naming convention are recommendations for discussion, not finalized protocol requirements.

## Problems and Challenges

The main challenge this week was determining how to proceed with production testing while the protocol, workflow definitions, and testing assignments were still being finalized. Collecting data before these decisions are confirmed could lead to inconsistent procedures or results that cannot be compared reliably.

The proposed workload also made it important to clarify the scope of testing and responsibilities across the team. I communicated these concerns to Ifeanyi so that the team could agree on the testing process before proceeding.

## Next Steps

I recommend finalizing the testing protocol, platform-operation matrix, and team assignments before official production data collection begins. I will submit my Week 9 journal and preliminary WeChat feasibility report through a GitHub pull request, then proceed with my assigned Gmail testing once the protocol and responsibilities are confirmed.