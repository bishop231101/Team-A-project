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
- Implemented and executed the approved full Week 12 Baseline-versus-Hamming comparative experiment using SA01, SU01, LA01, and LU01; both encoding modes; five corruption conditions; and three repetitions per combination, for exactly 120 trials.
- Used the approved repetition-specific deterministic seed pairs: R1 `481201/481202`, R2 `481211/481212`, and R3 `481221/481222`. The fixed logical bit targets were frame byte 9, bit 1 for single-bit corruption, and frame byte 9, bits 1 and 5 for double-bit corruption.
- Saved 120 individual JSON trial records, an aggregate `summary.json`, and `experiment_report.md` in `tests/week12_testing/comparative_experiment_output/`.
- Added automated validation and summary-aggregation tests. The relevant test run passed with 13 tests and 398 Hamming subtests.
- Independently audited every individual trial record against the codec, corpus, approved seed pairs, corruption metadata, decoder results, and aggregate summary. All 120 expected combinations were unique and valid.
- Verified that Baseline completed 12 successful recoveries out of 60 trials and Hamming completed 24 successful recoveries out of 60 trials. There were 84 detected failures, 0 undetected errors, and 0 unexpected execution errors.

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
- The full comparison showed the practical benefit of Hamming for bit substitutions: it recovered all 12 Hamming single-bit trials while Baseline detected all 12 corresponding failures. This benefit came with additional encoded length: 57.24% overhead for SA01 and SU01, 55.70% for LA01, and 55.77% for LU01.
- Both modes detected all tested double-bit and deletion failures. Hamming's additional redundancy did not make it recover deleted symbols, reinforcing that protection against bit substitutions does not guarantee recovery from structural symbol loss.
- Average retention for the deletion conditions was 99.22% for Baseline and 99.12% for Hamming at approximately 1% deletion, and 95.47% for Baseline and 95.37% for Hamming at approximately 5% deletion.

## Problems and Challenges

- Remaining official production testing across the other approved platforms is still outstanding, including Discord, Telegram Web, Microsoft Outlook, and Google Chrome Browser Console.
- Microsoft Word consistently removed the entire zero-width payload across all 24 trials, preventing successful decoding regardless of message length or character set.
- The full comparative experiment and its independent audit are complete. The separate comparative-experiment PR remains pending review and submission; no PR has been created yet.
- The generated human-readable experiment report records the totals and approved methodology, while the independently audited summary and individual records contain the detailed overhead, retention, and deletion statistics needed for final review.
- The comparative experiment work was prepared on the separate `tristan-week12-comparative-experiment` branch, and the submission workflow still needs to follow Ifeanyi's direction before staging or opening a PR.
- Balancing the remaining platform production trials with comparative experiments and documentation continues to be a workload challenge.

## Next Steps

- Submit the separate comparative-experiment implementation, 120 audited trial records, summary, report, methodology document, and tests for Henry and Ifeanyi's review; the PR remains pending and has not been created.
- Preserve the independently verified experiment results and include the validation evidence in the appropriate review workflow.
- Continue the remaining official production testing across Discord, Telegram Web, Microsoft Outlook, and Google Chrome Browser Console, completing the approved corpus messages and repetitions for each platform.
- Update the Week 12 journal and GitHub contributions with completed work, supporting evidence, and experiment results.
- Ensure the completed Notepad++ and Microsoft Word trial records, screenshots, analysis results, Gmail Reproducibility document, and updated journal are included in the appropriate PR for Ifeanyi's review.
- Coordinate with Henry and Ifeanyi regarding remaining platform-testing responsibilities and priorities after the comparative pilot review.
