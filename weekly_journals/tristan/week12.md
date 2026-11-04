# Week 12 Journal — Tristan Koch

## Weekly Focus

Continue official production data collection by completing the Notepad++ trials and beginning the remaining Microsoft Word trials. Begin preparations for comparative experiments evaluating Baseline and Error-Corrected modes under controlled corruption conditions.

## Work Completed

- Completed all 24 official Notepad++ production trials across the eight approved corpus messages, with three repetitions per message.
- All 24 Notepad++ trials achieved 100% zero-width character retention and exact recovery of the original secret messages.
- Staged and committed the second batch of Notepad++ trial records and supporting evidence.
- Created a Gmail Reproducibility document outlining the manual send-and-retrieve workflow so that Ifeanyi or Henry can independently repeat the process and compare retention rates and decoding outcomes.
- Coordinated with Ifeanyi regarding the comparative experiment requirements, automation approach, and next production-testing platform.

## What I Learned

- Notepad++ successfully preserved all encoded zero-width characters across the eight tested corpus messages during the paste-and-copy-back workflow.
- Reproducibility documentation is important because it allows other team members to independently repeat platform tests and verify whether similar results can be obtained.
- Controlled comparative experiments need equivalent corruption conditions, reproducible random seeds where applicable, and consistent measurements across Baseline and Error-Corrected modes.
- Automated testing could help improve consistency and efficiency when running repeated comparative experiments locally.

## Problems and Challenges

- Still awaiting Henry's confirmation regarding the current test suite's support for the requested comparative experiment conditions, including Baseline and Error-Corrected mode selection and corruption methods.
- Remaining Week 11 production testing across the other approved platforms is still outstanding.
- Microsoft Word has been prioritized as the next platform because preliminary testing indicated significant zero-width character loss. Its full production behavior still needs to be verified.
- Comparative experiment automation cannot be finalized until the test suite and corruption methods have been confirmed and a small pilot has been completed successfully.

## Next Steps

- Follow up with Henry and confirm the test suite's capabilities and the implementation of the required corruption conditions.
- Develop and run a small comparative experiment pilot before proceeding with the full testing matrix.
- If the pilot is successful, use Codex to help develop an automated script for the full Baseline versus Error-Corrected experiment.
- Prepare for and begin the initial batch of Microsoft Word production trials, prioritizing the Long ASCII and Long Unicode corpus messages.
- Include the completed Notepad++ trial records, screenshots, analysis results, Gmail Reproducibility document, and updated individual journal in the PR for Ifeanyi's review.