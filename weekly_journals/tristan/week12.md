# Week 12 Journal — Tristan Koch

## Weekly Focus

Continue official production data collection by completing the Notepad++ trials and beginning Microsoft Word production testing. Prepare and conduct comparative experiments evaluating Baseline and Error-Corrected modes under controlled corruption conditions.

## Work Completed

- Completed all 24 official Notepad++ production trials across the eight approved corpus messages, with three repetitions per message.
- All 24 Notepad++ trials achieved 100% zero-width character retention and exact recovery of the original secret messages.
- Staged and committed the second batch of Notepad++ trial records and supporting evidence.
- Created a Gmail Reproducibility document outlining the manual send-and-retrieve workflow so that other team members can independently repeat the process and compare retention rates and decoding outcomes.
- Created a Microsoft Word production testing guide and temporary command reference for the initial four short-message corpus IDs (SA01, SA02, SU01, and SU02).
- Completed the first 12 official Microsoft Word production trials, covering SA01, SA02, SU01, and SU02 with three repetitions each.
- All 12 Microsoft Word trials resulted in complete zero-width payload removal, with 0.0% retention and no successful secret recovery. All three zero-width character types (U+200B, U+200C, and U+200D) were removed in every trial.
- All 12 Microsoft Word trial records passed analyzer validation with no validation errors.
- Successfully switched to Henry's `henry/week12-hamming-stabilization` branch and verified the updated implementation, with 74 tests and 546 subtests passing. The dedicated Hamming stability verification script also passed.
- Coordinated with Ifeanyi and Henry regarding the comparative experiment requirements, pilot scope, corruption methods, and automation approach.
- Received Ifeanyi's approval to proceed with an SA01 pilot comparing Baseline and Hamming across the five corruption conditions, using one repetition per condition and mode.

## What I Learned

- Notepad++ successfully preserved all encoded zero-width characters across the eight tested corpus messages during the paste-and-copy-back workflow.
- Microsoft Word demonstrated complete removal of all three tested zero-width character types across the first 12 production trials, regardless of whether the payload contained ASCII or Unicode messages.
- Reproducibility documentation is important because it allows other team members to independently repeat platform tests and verify whether similar results can be obtained.
- Controlled comparative experiments need equivalent corruption conditions, reproducible random seeds where applicable, and consistent measurements across Baseline and Error-Corrected modes.
- Hamming error correction introduces additional encoded-length overhead compared with Baseline encoding, so encoded size and recovery performance both need to be measured.
- Hamming can correct certain bit substitutions and detect certain uncorrectable errors, but deletion of encoded symbols presents a different challenge and must be evaluated separately.
- Automated testing could improve consistency and efficiency when running repeated comparative experiments locally.

## Problems and Challenges

- The remaining Microsoft Word production trials, covering the four long-message corpus IDs, are still outstanding.
- The first 12 Microsoft Word trials consistently resulted in complete payload removal, preventing successful decoding. The remaining trials are needed to determine whether this behavior is consistent across longer messages.
- Comparative experiment automation is awaiting confirmation from Henry regarding the deletion-percentage calculation and remaining testing parameters.
- The comparative pilot script must be prepared and reviewed by Henry before execution to ensure that both encoding modes receive equivalent corruption conditions.
- Remaining Week 11 production testing across the other approved platforms is still outstanding.
- Balancing the remaining production trials with the comparative experiments and documentation continues to be a workload challenge.

## Next Steps

- Confirm the remaining comparative experiment parameters with Henry, particularly the deletion-percentage calculation and corruption methodology.
- Use Codex to prepare the SA01 comparative pilot script covering Baseline and Hamming under the five approved corruption conditions.
- Have Henry review the pilot script before running any experiments.
- Run the pilot and share its results, methodology, and supporting evidence with Henry and Ifeanyi for review.
- After the pilot is verified and approved, use Codex to help develop the automated script for the full comparative experiment matrix, including individual trial results and summary statistics.
- Continue Microsoft Word production testing with LA01, LA02, LU01, and LU02, completing three repetitions for each corpus message.
- Update the Week 12 journal and GitHub contributions with completed work, supporting evidence, and experiment results.
- Include the completed Notepad++ and Microsoft Word trial records, screenshots, analysis results, Gmail Reproducibility document, and updated journal in the appropriate PR for Ifeanyi's review.
- Resume the remaining approved platform production testing after establishing the comparative experiment workflow and coordinating testing responsibilities with the team.