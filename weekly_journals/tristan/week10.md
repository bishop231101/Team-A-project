# Week 10 Journal — Preliminary Workflow Verification and Feasibility Testing

## Weekly Focus

This week focused on completing preliminary workflow verification and feasibility testing across the seven approved platform-operation combinations before beginning official production data collection.

## Work Completed

With assistance from Codex and input from Ifeanyi and Henry, I created platform-specific command guide files for all seven approved platform-operation combinations. These guides provide a consistent, repeatable process for conducting preliminary tests and recording the results.

The guides include commands to:

- Verify the current working directory and Git branch.
- Confirm that the codec is functioning correctly and that the unit tests complete successfully.
- Generate the initial encoded text file using the approved corpus message and codec configuration.
- Perform a local encode/decode round-trip test before interacting with the platform.
- Save the retrieved platform text to a properly named file, such as `week10_NPP-01_sa01_retrieved.txt`.
- Compare the encoded and retrieved text, count the retained zero-width characters, calculate the retention rate, and attempt to decode the recovered payload.
- Record whether the encoded text matches exactly, whether decoding succeeds, any errors encountered, and other relevant observations.

I also created and refined the `workflow_verification.md` document to serve as a central record for the seven platform access and preliminary workflow verification checks.

After conducting the preliminary tests, I reviewed the encoded and retrieved text files, screenshots, filenames, evidence paths, and recorded results. I corrected inconsistencies in the workflow verification document so that it distinguishes platform access, workflow completion, decoding success or failure, and official production testing.

## Preliminary Findings and What I Learned

The preliminary tests demonstrated that even with the improved codec, different platforms can handle zero-width characters differently.

For example, Gmail retained 44.74% of the encoded zero-width characters. The retrieved text contained no U+200B characters, while U+200C and U+200D characters remained. Decoding failed with an error indicating that the payload contained an incomplete or malformed byte block.

Microsoft Word presented a different result. After the encoded text was pasted into a document, saved, and reopened, the retrieved text contained none of the three zero-width character types. Retention was 0%, and decoding failed because no zero-width payload was found.

In contrast, Discord, Microsoft Outlook, Telegram Web, Notepad++, and Google Chrome Browser Console retained 100% of the encoded zero-width characters in their preliminary checks and successfully recovered the original secret message, `Hello`.

These results reinforced the importance of testing the actual platform workflows instead of assuming that successful local encoding and decoding guarantees that a platform will preserve the payload.

## Problems and Challenges

One challenge was locating application version or build information for documentation purposes. The availability and location of this information varied between platforms.

Another important consideration was maintaining consistent documentation across seven platform guides and ensuring that filenames, evidence paths, measurements, and workflow statuses remained accurate as the preliminary results were recorded and the documentation was revised.

## Next Steps

My next steps are to finalize and commit the Week 10 changes, including the platform command guides, workflow verification document, preliminary test artifacts, screenshots, and weekly journal. I will then inform Ifeanyi that my work is complete and ready for review before the latest changes to PR #21 are merged.

Following the team's review of the preliminary results and confirmation that the testing process is ready, official production data collection is planned to begin on Monday, October 26, 2026, per my communication with Ifeanyi. This will allow the team to address any outstanding issues before starting formal data collection and help maintain accurate, reliable testing records.