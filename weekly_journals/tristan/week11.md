# Week 11 Journal — Official Production Data Collection: Gmail Trials

## Weekly Focus

This weeks focus was completing the official production testing for Gmail across all 8 approved corpus messages and 3 repetitions per message, for a total of 24 trials. Additonal work focused on preparing the testing environment, organizing trial evidence, automating analysis and bookkeeping tasks, and documenting the results for independent team review.

## Work Completed

- Used Codex to help create an automated test suite that ran checks to verify that the testing componnents were functioning properly.
- Prepared the bookkeeping structure for the production trials. The automation created the required folder and subfolder organization, generated correctly encoded text files for each corpus message, and created blank retrieved-text files using the required naming convention for each corpus message and repetition number.
- Manually conducted all 24 official Gmail production trials. For each trial, I copied the encoded text into Gmail, sent the email, captured a screenshot of the sent email, retrieved and copied the message text, and pasted it into the corresponding retrieved-text file.
- Ran the production analyzer command for each trial, updating the command to match the appropriate trial ID.
- Ran a separate command to obtain the UTC timestamp for each trial.
- Used the analyzer to compare the original sent zero-width character counts against the retrieved counts. It automatically calculated retention percentages, checked decoder success and exact-match results, recorded any recovered secret or decode error, and assigned a failure category.
- Manually updated each trial's JSON record with the appropriate status, tester information, UTC timestamp, and evidence paths.
- After completing the 24 manual Gmail production trials and their automated analysis, used Codex to review the collected trial data and generate a consolidated summary of the official Gmail production findings for easier team review.

## What I Learned

The official Gmail production results showed that none of the 24 trials successfully recovered the original secret. The decoder consistently reported malformed or incomplete byte blocks, resulting in structural corruption failures.

U+200B characters were removed across all 24 trials. U+200C and U+200D characters were preserved in the short ASCII (SA) and short Unicode (SU) tests, while only partial amounts of these characters were preserved in the long ASCII (LA) and long Unicode (LU) tests.

This demonstrated that the presence of some surviving zero-width characters does not necessarily mean the encoded payload can be recovered successfully. The analyzer was useful for consistently measuring character retention and documenting decoding outcomes across the trials.

I also gained experience using automated preparation and analysis tools alongside manual platform testing. Automating the folder structure, file naming, and calculations helped keep the testing process organized while allowing the actual Gmail interactions and evidence collection to remain manual.

## Problems and Challenges

The primary challenge was Gmail's handling of the zero-width characters in the encoded messages. The complete removal of U+200B and partial preservation of other zero-width characters prevented successful secret recovery across all 24 trials.

Another challenge was maintaining accurate bookkeeping across the production workload. Each repetition required its own sent and retrieved text files, screenshot, analyzer execution, UTC timestamp, and JSON record. The automated folder and file preparation helped manage this workload, but the platform interactions, evidence collection, and record updates still required manual attention.

One evidence-reference issue was also identified during validation of the LU02 R3 record. The evidence reference was corrected, and the subsequent analyzer run confirmed that the record passed validation.

## Next Steps

- Review all 24 Gmail trial records to ensure their statuses, tester information, UTC timestamps, measurements, and evidence references are correct.
- Confirm that all encoded files, retrieved files, screenshots, raw evidence, and analyzer results are included in the appropriate project directories.
- Stage, Commit, and push the completed Gmail production testing work to my Github branch.
- Open a pull request containing all 24 trial records, supporting evidence, calculations, analyzer results, and the updated individual journal for Ifeanyi's independent review.
- Address any feedback or corrections identified during the review.
- If time permits after the Gmail submission is ready for review, proceed with next assigned platform, Notepad++.