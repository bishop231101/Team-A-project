# Week 12 Journal — Tristan Koch

## Weekly Focus

Complete official production data collection for Notepad++ and Microsoft Word, including the remaining long-message trials. Prepare, execute, and document the SA01 comparative pilot evaluating Baseline and Hamming Error-Corrected modes under controlled corruption conditions. Coordinate with Henry and Ifeanyi to verify the pilot methodology and results before proceeding with the full comparative experiment.

## Work Completed

- Completed all 24 official Notepad++ production trials across the eight approved corpus messages, with three repetitions per message.
- All 24 Notepad++ trials achieved 100% zero-width character retention and exact recovery of the original secret messages.
- Staged and committed the second batch of Notepad++ trial records and supporting evidence.
- Created a Gmail Reproducibility document outlining the manual send-and-retrieve workflow so that other team members can independently repeat the process and compare retention rates and decoding outcomes.
- Created a Microsoft Word production testing guide and temporary command reference for the eight approved corpus messages.
- Completed all 24 official Microsoft Word production trials, covering all eight corpus messages (SA01, SA02, SU01, SU02, LA01, LA02, LU01, and LU02) with three repetitions each.
- All 24 Microsoft Word trials resulted in complete zero-width payload removal, with 0.0% retention and no successful secret recovery. All three zero-width character types (U+200B, U+200C, and U+200D) were removed in every trial.
- All 24 Microsoft Word trial records passed analyzer validation with no validation errors.
- Successfully switched to Henry's `henry/week12-hamming-stabilization` branch and verified the updated implementation, with 74 tests and 546 subtests passing. The dedicated Hamming stability verification script also passed.
- Coordinated with Ifeanyi and Henry regarding the comparative experiment requirements, pilot scope, corruption methods, deletion methodology, and automation approach.
- Prepared the SA01 comparative pilot script covering Baseline and Hamming modes across five corruption conditions, incorporating Henry's requested revisions.
- Received Henry's approval of the revised pilot script and completed the SA01 comparative pilot using one repetition per condition and mode, producing ten individual trial records and a `summary.json` file.
- Shared the ten pilot trial records, summary JSON, and pilot results with Henry and Ifeanyi in the group chat for review.
- The pilot produced three successful recoveries and seven detected failures across both modes, with no undetected incorrect recoveries.
- The Hamming mode successfully corrected the tested single-bit corruption that caused Baseline decoding to fail. Both modes detected or rejected the tested double-bit corruption and deletion conditions.
- Recorded the encoded-length overhead of Hamming compared with Baseline, along with the actual deletion counts, percentages, and recovery outcomes.

## What I Learned

- Notepad++ successfully preserved all encoded zero-width characters across the eight tested corpus messages during the paste-and-copy-back workflow.
- Microsoft Word demonstrated complete removal of all three tested zero-width character types across all 24 production trials, regardless of whether the payload contained short or long ASCII and Unicode messages.
- Reproducibility documentation is important because it allows other team members to independently repeat platform tests and verify whether similar results can be obtained.
- Controlled comparative experiments need equivalent corruption conditions, reproducible random seeds where applicable, and consistent measurements across Baseline and Error-Corrected modes.
- Hamming error correction introduces additional encoded-length overhead compared with Baseline encoding, so encoded size and recovery performance both need to be measured.
- The SA01 pilot demonstrated that Hamming could correct the tested single-bit corruption, while Baseline detected the resulting checksum mismatch and failed to recover the original message.
- Both modes detected or rejected the tested double-bit corruption and deletion conditions, demonstrating that error correction does not guarantee recovery from every type of corruption.
- Deletion of encoded symbols presents a different challenge from bit substitutions because removing symbols can disrupt the structure of the encoded payload.
- Automated testing improves consistency and efficiency when running repeated comparative experiments locally, while saving individual trial records and summary statistics makes results easier to verify.

## Problems and Challenges

- Remaining official production testing across the other approved platforms is still outstanding, including Discord, Telegram Web, Microsoft Outlook, and Google Chrome Browser Console.
- Microsoft Word consistently removed the entire zero-width payload across all 24 trials, preventing successful decoding regardless of message length or character set.
- The SA01 comparative pilot is complete, but its methodology, individual trial records, and summary statistics are awaiting review and approval from Henry and Ifeanyi.
- The full comparative experiment matrix cannot proceed until the pilot results are reviewed and the team approves the methodology.
- The comparative experiment script and pilot evidence were prepared while working with Henry's branch, so the submission and branch workflow for the full experiment needs to follow Ifeanyi's direction to use a separate branch and PR based on the updated main branch.
- Balancing the remaining platform production trials with comparative experiments and documentation continues to be a workload challenge.

## Next Steps

- Obtain Henry and Ifeanyi's feedback and approval on the SA01 comparative pilot, including the script, ten individual trial records, deletion methodology, recovery outcomes, and summary statistics.
- Follow Ifeanyi's direction regarding the submission of the comparative pilot artifacts and include them in the appropriate PR or review workflow.
- After Henry's required changes are merged into `main`, create a separate branch and PR for the full comparative experiment, as requested by Ifeanyi.
- If the pilot is approved, prepare and execute the full comparative experiment matrix using the approved methodology, preserving individual trial results, supporting evidence, and summary statistics.
- Continue the remaining official production testing across Discord, Telegram Web, Microsoft Outlook, and Google Chrome Browser Console, completing the approved corpus messages and repetitions for each platform.
- Update the Week 12 journal and GitHub contributions with completed work, supporting evidence, and experiment results.
- Ensure the completed Notepad++ and Microsoft Word trial records, screenshots, analysis results, Gmail Reproducibility document, and updated journal are included in the appropriate PR for Ifeanyi's review.
- Coordinate with Henry and Ifeanyi regarding remaining platform-testing responsibilities and priorities after the comparative pilot review.