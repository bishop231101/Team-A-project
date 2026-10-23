# Week 10 Workflow Verification's
**Prepared by:** Tristan Koch
**Date:** October 20, 2026
**Project:** Zero-Width Unicode Steganography with Social-Media Robustness Engineering
**Status:** Complete

# Week 10 Workflow Verification — Gmail

**Platform:** Gmail
**Operation:** Send and Retrieve message
**Access Status:** Confirmed
**Verification status:** Verified
**Date verified:** 10/23/2026
**Tester:** Tristan Koch


## 1. Access

- **Application/site opened:** Gmail website opened in Google Chrome
- **Relevant feature accessible:** Compose window opened successfully
- **Version or environment:** Google Chrome, Version 156.0.8078.48 (Official Build) (64-bit); Windows 11 64-bit
- **Access limitations:** None observed during access and preliminary workflow verification. This was not an official production trial.

## 2. Workflow Steps

### Steps

1. Confirm access to the platform and open the relevant messaging interface.
2. Select an approved corpus message and record its corpus ID.
3. Encode the message using the project encoder and the approved codec configuration.
4. Perform a local encode/decode round-trip test to verify that the original message can be recovered exactly.
5. Save the encoded text and record the number of zero-width characters sent, including counts for U+200B, U+200C, and U+200D.
6. Copy the encoded text and paste it into the platform's message composer.
7. Send the message using the approved test account or destination.
8. Retrieve the sent message through the approved workflow and copy the retrieved text without manually correcting or altering it.
9. Save the retrieved text and any required screenshots or terminal output.
10. Run the decoder on the retrieved text and compare the recovered message with the original corpus message.
11. Record the retrieved zero-width character counts, retention rate, decoder success, exact-recovery result, and any errors or limitations.
12. Document the workflow outcome and any deviations from the approved procedure.

**Workflow result:** Completed

## 3. Preliminary Feasibility Check

- Preliminary check ID: PRELIM_GMAIL-01
- Platform-operation: Gmail — send and retrieve message
- Expected behavior: SA01 is loaded from the approved corpus; local recovery is exactly Hello; platform result is measured without text repair.
- Observed result: Local encode/decode round-trip succeeded. After sending the encoded message over Gmail and copying it back, only 68 zero-width characters were preserved with all U+200B characters seemingly removed. The retrieved cover text matched the encoded cover text exactly, however decoding failed due to the payload containing malformed or incomplete byte block.
- Corpus ID: SA01
- Expected SHA-256: 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
- Codec configuration: src/zero_width_codec.py; cover "Team 1 compatibility test."; recovery_mode=False; repetition_factor: not used
- Gmail/browser version: Google Chrome, Version 156.0.8078.48 (Official Build) (64-bit);
- Operating system: Windows 11 64-bit
- Encoded U+200B / U+200C / U+200D / total: 84 / 52 / 16 / 152
- Retrieved U+200B / U+200C / U+200D / total: 0 / 52 / 16 / 68
- Retention percentage: 44.74%
- Exact encoded-text match: False
- Decode result: Success / Failure; error if any: decode succeeded: False; decode error: DecodeError payload contains an incomplete or malformed byte block
- Recovered secret exactly equals Hello: No
- Evidence references:
    - Send message: `tests/week10_testing/preliminary_testing/Gmail/evidence/PRELIM_GMAIL-01_Sent.png`
    - Terminal results: `tests/week10_testing/preliminary_testing/Gmail/evidence/PRELIM_GMAIL-01_Terminal.png`
- Limitations and observations: This was a preliminary feasibility check, not an official production trial. The encoded message was sent over Gmail to myself and the sent message copied back. The copied-back text was pasted into a separate plain-text file named `week10_Gmail-01_sa01_retrieved.txt` so the retrieval and analysis commands could evaluate it. No manual repair was performed.
- **Next steps:** Retain the verification summary entry showing that the preliminary Gmail workflow was completed and decoding failed.

> These results are for workflow verification. Do not count them as official production trials unless the team confirms that they qualify.

## 4. Evidence

| Evidence | File path or link | What it demonstrates |
|---|---|---|
| Screenshot | tests/week10_testing/preliminary_testing/Gmail/evidence/PRELIM_GMAIL-01_Sent.png | Encoded text sent via gmail |
| Terminal output | tests/week10_testing/preliminary_testing/Gmail/evidence/PRELIM_GMAIL-01_Terminal.png | Terminal results from decode attempt |
| Retrieved text or other record | tests/week10_testing/preliminary_testing/Gmail/week10_Gmail-01_sa01_retrieved.txt | Contains copied text from sent email |

## 5. Notes and Blockers

- **Unexpected behavior:** When running the decode and compare commands from the guide using the copied email contents, found in `week10_Gmail-01_sa01_retrieved.txt`, the retrieved counts showed no U+200B characters and retained the recorded U+200C and U+200D counts. Decode attempt failed.
- **Errors or limitations:** Decode attempt failed. Error listed: DecodeError payload contains an incomplete or malformed byte block
- **Questions requiring team confirmation:**
    1. Gmail appears to have removed U+200B (ZERO WIDTH SPACE) characters during message transmission, resulting in 44.74% overall zero-width character retention and a decode failure with the error: “payload contains an incomplete or malformed byte block.” Should Gmail remain in the approved platform matrix for official production testing, with these results recorded as an observed platform failure, or should the team review its suitability before production testing begins?
    2. Should any additional diagnostic checks be performed to distinguish Gmail's handling of U+200B from the loss or corruption of other zero-width characters, while preserving the approved testing protocol and avoiding any manual repair of the retrieved text?
- **Next action:** Retain the verification summary entry showing that the Gmail preliminary workflow was completed but resulted in a failed decode.

---

# Week 10 Workflow Verification — Discord

**Platform:** Discord
**Operation:** Send and Retrieve message
**Access Status:** Confirmed
**Verification status:** Verified
**Date verified:** 10/23/2026
**Tester:** Tristan Koch

## 1. Access

- **Application/site opened:** Discord app opened successfully
- **Relevant feature accessible:** Text chat accessed successfully
- **Version or environment:** Discord, Build number 643186; Windows 11 64-bit
- **Access limitations:** None observed during access and preliminary workflow verification. This was not an official production trial.

## 2. Workflow Steps

### Steps

1. Confirm access to the platform and open the relevant messaging interface.
2. Select an approved corpus message and record its corpus ID.
3. Encode the message using the project encoder and the approved codec configuration.
4. Perform a local encode/decode round-trip test to verify that the original message can be recovered exactly.
5. Save the encoded text and record the number of zero-width characters sent, including counts for U+200B, U+200C, and U+200D.
6. Copy the encoded text and paste it into the platform's message composer.
7. Send the message using the approved test account or destination.
8. Retrieve the sent message through the approved workflow and copy the retrieved text without manually correcting or altering it.
9. Save the retrieved text and any required screenshots or terminal output.
10. Run the decoder on the retrieved text and compare the recovered message with the original corpus message.
11. Record the retrieved zero-width character counts, retention rate, decoder success, exact-recovery result, and any errors or limitations.
12. Document the workflow outcome and any deviations from the approved procedure.

**Workflow result:** Completed

## 3. Preliminary Feasibility Check

- Preliminary check ID: PRELIM_DISCORD-01
- Platform-operation: Discord — send and retrieve message
- Expected behavior: local SA01 recovery is exactly Hello; platform preservation is measured without repair.
- Observed result: Local encode/decode round-trip succeeded. After sending the encoded message into Discord and copying it back, all 152 zero-width characters were preserved. The retrieved text matched the encoded text exactly, and decoding recovered Hello.
- Corpus ID / expected SHA-256: SA01 / 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
- Codec configuration: src/zero_width_codec.py; cover "Team 1 compatibility test."; recovery_mode=False
- Discord/client or browser version: Discord, Build number 643186
- Operating system: Windows 11 64-bit
- Encoded U+200B / U+200C / U+200D / total: 84 / 52 / 16 / 152
- Retrieved U+200B / U+200C / U+200D / total: 84 / 52 / 16 / 152
- Retention percentage: 100.00%
- Exact encoded-text match: True
- Decode result and error: decode succeeded: True; recovered secret: 'Hello'; no error reported
- Recovered secret exactly equals Hello: Yes
- Evidence references:
    - Send message: `tests/week10_testing/preliminary_testing/Discord/evidence/PRELIM_DISCORD-01_sent.png`
    - Terminal results: `tests/week10_testing/preliminary_testing/Discord/evidence/PRELIM_DISCORD-01_terminal.png`
- Limitations and observations: This was a preliminary feasibility check, not an official production trial. The encoded message was sent over Discord - Capstone Project Server and the sent message copied back. The copied-back text was pasted into a separate plain-text file named `week10_Discord-01_sa01_retrieved.txt` so the retrieval and analysis commands could evaluate it. No manual repair was performed.
- **Next steps:** Retain the verification summary entry showing that the Discord preliminary workflow was completed and decoding succeeded.

> These results are for workflow verification. Do not count them as official production trials unless the team confirms that they qualify.

## 4. Evidence

| Evidence | File path or link | What it demonstrates |
|---|---|---|
| Screenshot | tests/week10_testing/preliminary_testing/Discord/evidence/PRELIM_DISCORD-01_sent.png | Encoded message sent in discord |
| Terminal output | tests/week10_testing/preliminary_testing/Discord/evidence/PRELIM_DISCORD-01_terminal.png | Terminal results from decode attempt |
| Retrieved text or other record | tests/week10_testing/preliminary_testing/Discord/week10_Discord-01_sa01_retrieved.txt | Contains message copied back from discord |

## 5. Notes and Blockers

- **Unexpected behavior:** None observed during Discord Send-and-Retrieve preliminary test.
- **Errors or limitations:** No command errors were observed. The preliminary check covers Discord Send-and-Retrieve behavior only; it does not establish results for other platforms or count as an official production trial. The retrieved text was saved to a separate plain-text file for analysis
- **Questions requiring team confirmation:** No questions
- **Next action:** Retain the verification summary entry showing that the Discord preliminary workflow was completed and decoding succeeded.

---

# Week 10 Workflow Verification — Microsoft Word

**Platform:** Microsoft Word
**Operation:** Save, Reopen, and retrieve text
**Access Status:** Confirmed
**Verification status:** Verified
**Date verified:** 10/23/2026
**Tester:** Tristan Koch

## 1. Access

- **Application/site opened:** Microsoft Word app opened successfully
- **Relevant feature accessible:** Blank document was opened with no issues
- **Version or environment:** Microsoft® Word for Microsoft 365 MSO (Version 2609 Build 16.0.20430.20032) 64-bit; Windows 11 64-bit
- **Access limitations:** None observed during access and preliminary workflow verification. This was not an official production trial.

## 2. Workflow Steps

### Steps

1. Confirm access to Microsoft Word and create or open the approved test document.
2. Select an approved corpus message and record its corpus ID.
3. Encode the message using the project encoder and the approved codec configuration.
4. Perform a local encode/decode round-trip test to verify that the original message can be recovered exactly.
5. Save the encoded text and record the number of zero-width characters sent, including counts for U+200B, U+200C, and U+200D.
6. Copy the encoded text into the Word document without intentionally modifying it.
7. Save the document using the approved test procedure.
8. Close and reopen the saved document.
9. Retrieve and copy the encoded text from the reopened document without manually correcting or altering it.
10. Save the retrieved text and any required screenshots or terminal output.
11. Run the decoder on the retrieved text and compare the recovered message with the original corpus message.
12. Record the retrieved zero-width character counts, retention rate, decoder success, exact-recovery result, and any errors or limitations.
13. Document the workflow outcome and any deviations from the approved procedure.

**Workflow result:** Completed

## 3. Preliminary Feasibility Check

- Preliminary check ID: PRELIM_WORD-01
- Platform-operation: Microsoft Word — save, reopen, and retrieve text
- Expected behavior: local SA01 recovery is exactly Hello; saved/reopened text is measured unchanged.
- Observed result: Local encode/decode round-trip succeeded. After saving the encoded message in a word document, closing and reopening the document, and copying it back, all 152 zero-width characters were lost. The retrieved text did not match the encoded text, and decoding failed.
- Corpus ID / expected SHA-256: SA01 / 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
- Codec configuration: src/zero_width_codec.py; cover "Team 1 compatibility test."; recovery_mode=False
- Microsoft Word version / document format: Microsoft® Word for Microsoft 365 MSO (Version 2609 Build 16.0.20430.20032) 64-bit; Word Document (.docx)
- Operating system: Windows 11 64-bit
- Encoded U+200B / U+200C / U+200D / total: 84 / 52 / 16 / 152
- Retrieved U+200B / U+200C / U+200D / total: 0 / 0 / 0 / 0
- Retention percentage: 0.00%
- Exact encoded-text match: False
- Decode result and error: decode succeeded: False; decode error: DecodeError no zero-width payload was found
- Recovered secret exactly equals Hello: No
- Evidence references:
    - Send message: `tests/week10_testing/preliminary_testing/Microsoft_Word/evidence/PRELIM-WORD-01_Save.png`
    - Terminal results: `tests/week10_testing/preliminary_testing/Microsoft_Word/evidence/PRELIM-WORD-01_Terminal.png`
- Limitations and observations: The encoded payload was not detected after the save-and-reopen workflow.
- **Next steps:** Retain the verification summary entry showing that the Microsoft Word preliminary workflow was completed and decoding failed.

> These results are for workflow verification. Do not count them as official production trials unless the team confirms that they qualify.

## 4. Evidence

| Evidence | File path or link | What it demonstrates |
|---|---|---|
| Screenshot | tests/week10_testing/preliminary_testing/Microsoft_Word/evidence/PRELIM-WORD-01_Save.png | Encoded message saved in Microsoft Word document titled 'Week10_Word_Prelim_test.docx' |
| Terminal output | tests/week10_testing/preliminary_testing/Microsoft_Word/evidence/PRELIM-WORD-01_Terminal.png | Terminal results from decode attempt |
| Retrieved text or other record | tests/week10_testing/preliminary_testing/Microsoft_Word/week10_Word-01_sa01_retrieved.txt | Contains message copied back from 'Week10_Word_Prelim_test.docx' |

## 5. Notes and Blockers

- **Unexpected behavior:** After conducting the workflow for Microsoft Word which is;
    1. Paste encoded message into brand new blank document
    2. Save document using name Week10_Word_Prelim_test.docx
    3. Close document and Re-open it
    4. Copy document contents and paste into `week10_Word-01_sa01_retrieved.txt`
    5. run the comparison/decode commands and record results.

    After that workflow it appears that Microsoft Word had lost or removed all encoded zero-width characters resulting in the error detailed below.

- **Errors or limitations:** DecodeError no zero-width payload was found
- **Questions requiring team confirmation:** Microsoft Word returned 0.00% zero-width character retention after the encoded text was pasted into a blank document, saved as a DOCX file, closed, reopened, and copied back. The decoder reported “No zero-width payload was found.” Should Microsoft Word remain in the approved platform matrix for official production testing, with this behavior recorded as an observed platform failure, or should the team review the result before production testing begins?
- **Next action:** Retain the verification summary entry showing that the Microsoft Word preliminary workflow was completed and decoding failed.

---

# Week 10 Workflow Verification — Microsoft Outlook

**Platform:** Microsoft Outlook
**Operation:** Send and Retrieve message
**Access Status:** Confirmed
**Verification status:** Verified
**Date verified:** 10/23/2026
**Tester:** Tristan Koch

## 1. Access

- **Application/site opened:** Microsoft Outlook website loaded successfully
- **Relevant feature accessible:** Compose window opened successfully.
- **Version or environment:** Could not find Outlook website version; Windows 11 64-bit
- **Access limitations:** Could not find the Outlook website version during access verification, but access was successful and the preliminary workflow was completed. This was not an official production trial.

## 2. Workflow Steps

### Steps

1. Confirm access to the platform and open the relevant messaging interface.
2. Select an approved corpus message and record its corpus ID.
3. Encode the message using the project encoder and the approved codec configuration.
4. Perform a local encode/decode round-trip test to verify that the original message can be recovered exactly.
5. Save the encoded text and record the number of zero-width characters sent, including counts for U+200B, U+200C, and U+200D.
6. Copy the encoded text and paste it into the platform's message composer.
7. Send the message using the approved test account or destination.
8. Retrieve the sent message through the approved workflow and copy the retrieved text without manually correcting or altering it.
9. Save the retrieved text and any required screenshots or terminal output.
10. Run the decoder on the retrieved text and compare the recovered message with the original corpus message.
11. Record the retrieved zero-width character counts, retention rate, decoder success, exact-recovery result, and any errors or limitations.
12. Document the workflow outcome and any deviations from the approved procedure.

**Workflow result:** Completed

## 3. Preliminary Feasibility Check

- Preliminary check ID: PRELIM_OUTLOOK-01
- Platform-operation: Microsoft Outlook — send and retrieve message
- Expected behavior: local SA01 recovery is exactly Hello; platform result is measured without repair.
- Observed result: Local encode/decode round-trip succeeded. After sending the encoded message to myself on Microsoft Outlook and copying it back, all 152 zero-width characters were preserved. The retrieved text matched the encoded text exactly, and decoding recovered Hello.
- Corpus ID / expected SHA-256: SA01 / 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
- Codec configuration: src/zero_width_codec.py; cover "Team 1 compatibility test."; recovery_mode=False
- Outlook version / account mode: Could not find Outlook website version; school email
- Operating system: Windows 11 64-bit
- Encoded U+200B / U+200C / U+200D / total: 84 / 52 / 16 / 152
- Retrieved U+200B / U+200C / U+200D / total: 84 / 52 / 16 / 152
- Retention percentage: 100.00%
- Exact encoded-text match: True
- Decode result and error: decode succeeded: True; recovered secret: 'Hello'; no error reported
- Recovered secret exactly equals Hello: Yes
- Evidence references:
    - Sent message: `tests/week10_testing/preliminary_testing/Microsoft_Outlook/evidence/PRELIM-OUTLOOK-01_Send.png`
    - Terminal output: `tests/week10_testing/preliminary_testing/Microsoft_Outlook/evidence/PRELIM-OUTLOOK-01_Terminal.png`
- Limitations and observations: This was a preliminary feasibility check, not an official production trial. The encoded message was sent over Microsoft Outlook to myself and the sent message copied back. The copied-back text was pasted into a separate plain-text file named `week10_Outlook-01_sa01_retrieved.txt` so the retrieval and analysis commands could evaluate it. No manual repair was performed.
- **Next steps:** Retain the verification summary entry showing that the Outlook preliminary workflow was completed and decoding succeeded.

> These results are for workflow verification. Do not count them as official production trials unless the team confirms that they qualify.

## 4. Evidence

| Evidence | File path or link | What it demonstrates |
|---|---|---|
| Screenshot | tests/week10_testing/preliminary_testing/Microsoft_Outlook/evidence/PRELIM-OUTLOOK-01_Send.png | Email over Outlook containing the encoded message |
| Terminal output | tests/week10_testing/preliminary_testing/Microsoft_Outlook/evidence/PRELIM-OUTLOOK-01_Terminal.png | Terminal results from decode attempt |
| Retrieved text or other record | tests/week10_testing/preliminary_testing/Microsoft_Outlook/week10_Outlook-01_sa01_retrieved.txt | Contains text copied back from sent email |

## 5. Notes and Blockers

- **Unexpected behavior:** None observed during Microsoft Outlook Send-and-Retrieve preliminary test.
- **Errors or limitations:** No command errors were observed. The preliminary check covers Microsoft Outlook Send-and-Retrieve behavior only; it does not establish results for other platforms or count as an official production trial. The retrieved text was saved to a separate plain-text file for analysis
- **Questions requiring team confirmation:** No questions
- **Next action:** Retain the verification summary entry showing that the Outlook preliminary workflow was completed and decoding succeeded.

---

# Week 10 Workflow Verification — Telegram Web

**Platform:** Telegram Web
**Operation:** Send and Retrieve message
**Access Status:** Confirmed
**Verification status:** Verified
**Date verified:** 10/23/2026
**Tester:** Tristan Koch

## 1. Access

- **Application/site opened:** Telegram Web - website opened successfully
- **Relevant feature accessible:** Telegram text chat opened successfully
- **Version or environment:** Could not find Telegram Web version number; Windows 11 64-bit
- **Access limitations:** Could not find the Telegram Web version during access verification, but access was successful and the preliminary workflow was completed. This was not an official production trial.

## 2. Workflow Steps

### Steps

1. Confirm access to the platform and open the relevant messaging interface.
2. Select an approved corpus message and record its corpus ID.
3. Encode the message using the project encoder and the approved codec configuration.
4. Perform a local encode/decode round-trip test to verify that the original message can be recovered exactly.
5. Save the encoded text and record the number of zero-width characters sent, including counts for U+200B, U+200C, and U+200D.
6. Copy the encoded text and paste it into the platform's message composer.
7. Send the message using the approved test account or destination.
8. Retrieve the sent message through the approved workflow and copy the retrieved text without manually correcting or altering it.
9. Save the retrieved text and any required screenshots or terminal output.
10. Run the decoder on the retrieved text and compare the recovered message with the original corpus message.
11. Record the retrieved zero-width character counts, retention rate, decoder success, exact-recovery result, and any errors or limitations.
12. Document the workflow outcome and any deviations from the approved procedure.

**Workflow result:** Completed

## 3. Preliminary Feasibility Check

- Preliminary check ID: PRELIM_TELEGRAM-01
- Platform-operation: Telegram Web — send and retrieve message
- Expected behavior: local SA01 recovery is exactly Hello; platform result is measured without repair.
- Observed result: Local encode/decode round-trip succeeded. After sending the encoded message to my saved messages chat on Telegram Web and copying it back, all 152 zero-width characters were preserved. The retrieved text matched the encoded text exactly, and decoding recovered Hello.
- Corpus ID / expected SHA-256: SA01 / 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
- Codec configuration: src/zero_width_codec.py; cover "Team 1 compatibility test."; recovery_mode=False
- Telegram Web/browser version: Could not find Telegram Web version number
- Operating system: Windows 11 64-bit
- Encoded U+200B / U+200C / U+200D / total: 84 / 52 / 16 / 152
- Retrieved U+200B / U+200C / U+200D / total: 84 / 52 / 16 / 152
- Retention percentage: 100.00%
- Exact encoded-text match: True
- Decode result and error: decode succeeded: True; recovered secret: 'Hello'; no error reported
- Recovered secret exactly equals Hello: Yes
- Evidence references:
    - Sent message: `tests/week10_testing/preliminary_testing/Telegram_Web/evidence/PRELIM-TELEGRAM-01_Send.png`
    - Terminal output: `tests/week10_testing/preliminary_testing/Telegram_Web/evidence/PRELIM-TELEGRAM-01_Terminal.png`
- Limitations and observations: This was a preliminary feasibility check, not an official production trial. The encoded message was sent over Telegram Web saved messages chat to myself and the sent message copied back. The copied-back text was pasted into a separate plain-text file named `week10_TelegramWeb-01_sa01_retrieved.txt` so the retrieval and analysis commands could evaluate it. No manual repair was performed.
- **Next steps:** Retain the verification summary entry showing that the Telegram Web preliminary workflow was completed and decoding succeeded.

> These results are for workflow verification. Do not count them as official production trials unless the team confirms that they qualify.

## 4. Evidence

| Evidence | File path or link | What it demonstrates |
|---|---|---|
| Screenshot | tests/week10_testing/preliminary_testing/Telegram_Web/evidence/PRELIM-TELEGRAM-01_Send.png | [What is shown] |
| Terminal output | tests/week10_testing/preliminary_testing/Telegram_Web/evidence/PRELIM-TELEGRAM-01_Terminal.png | Terminal results from decode attempt |
| Retrieved text or other record | tests/week10_testing/preliminary_testing/Telegram_Web/week10_TelegramWeb-01_sa01_retrieved.txt | Contains text copied back from sent telegram message |

## 5. Notes and Blockers

- **Unexpected behavior:** None observed during Telegram Web Send-and-Retrieve preliminary test.
- **Errors or limitations:** No command errors were observed. The preliminary check covers Telegram Web Send-and-Retrieve behavior only; it does not establish results for other platforms or count as an official production trial. The retrieved text was saved to a separate plain-text file for analysis
- **Questions requiring team confirmation:** No questions
- **Next action:** Retain the verification summary entry showing that the Telegram Web preliminary workflow was completed and decoding succeeded.

---

# Week 10 Workflow Verification — Notepad++

**Platform:** Notepad++
**Operation:** Paste and copy back
**Access Status:** Confirmed
**Verification status:** Verified
**Date verified:** 10/22/2026
**Tester:** Tristan Koch

## 1. Access

- **Application/site opened:** Notepad++ application opened successfully
- **Relevant feature accessible:** New blank notepad opened successfully
- **Version or environment:** Notepad++ v8.9.8.1 (64-bit); Windows 11 64-bit
- **Access limitations:** None observed during access and preliminary workflow verification. This was not an official production trial.

## 2. Workflow Steps

### Steps

1. Confirm access to the application and open the relevant editing or input area.
2. Select an approved corpus message and record its corpus ID.
3. Encode the message using the project encoder and the approved codec configuration.
4. Perform a local encode/decode round-trip test to verify that the original message can be recovered exactly.
5. Save the encoded text and record the number of zero-width characters sent, including counts for U+200B, U+200C, and U+200D.
6. Copy the encoded text and paste it into the target application or console.
7. Follow the approved procedure to copy the text back out of the application or console without intentionally modifying it.
8. Save the retrieved text and any required screenshots or terminal output.
9. Run the decoder on the retrieved text and compare the recovered message with the original corpus message.
10. Record the retrieved zero-width character counts, retention rate, decoder success, exact-recovery result, and any errors or limitations.
11. Document the workflow outcome and any deviations from the approved procedure.

**Workflow result:** Completed

## 3. Preliminary Feasibility Check

- Preliminary check ID: PRELIM-NPP-01
- Platform-operation: Notepad++ — paste and copy back
- Expected behavior: local SA01 recovery is exactly Hello; copy-back is measured without repair.
- Observed result: Local encode/decode round-trip succeeded. After copying the encoded message into Notepad++ and copying it back, all 152 zero-width characters were preserved. The retrieved text matched the encoded text exactly, and decoding recovered Hello.
- Corpus ID / expected SHA-256: SA01 / 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
- Codec configuration: src/zero_width_codec.py; cover "Team 1 compatibility test."; recovery_mode=False
- Notepad++ version / encoding / line endings: Notepad++ v8.9.8.1 (64-bit) / utf-8 / Windows (CR LF)
- Operating system: Windows 11 64-bit
- Encoded U+200B / U+200C / U+200D / total: 84 / 52 / 16 / 152
- Retrieved U+200B / U+200C / U+200D / total: 84 / 52 / 16 / 152
- Retention percentage: 100.00%
- Exact encoded-text match: True
- Decode result and error: Decode succeeded: True; recovered secret: 'Hello'; no error reported.
- Recovered secret exactly equals Hello: True
- Evidence references: 
    - Paste-and-Copy-Back: `tests/week10_testing/preliminary_testing/Notepad++/evidence/PRELIM-NPP-01-Paste-Copy-Back.png` 
    - Terminal results: `tests/week10_testing/preliminary_testing/Notepad++/evidence/PRELIM-NPP-01-Terminal.png`
- Limitations and observations: This was a preliminary feasibility check, not an official production trial. The encoded message was pasted into Notepad++ and copied back without saving it in Notepad++. The copied-back text was pasted into a separate plain-text file named `week10_NPP-01_sa01_retrieved.txt` so the retrieval and analysis commands could evaluate it. No manual repair was performed.
- Next steps: Commit the documentation and evidence associated with this preliminary check, push the changes to the existing tristan-week10 branch and pull request, and notify Ifeanyi that the preliminary check is complete and ready for review. After the pull request is reviewed and accepted, proceed with the remaining preliminary platform checks. Keep all preliminary results separate from official production data collection.

> These results are for workflow verification. Do not count them as official production trials unless the team confirms that they qualify.

## 4. Evidence

| Evidence | File path or link | What it demonstrates |
|---|---|---|
| Screenshot | tests/week10_testing/preliminary_testing/Notepad++/evidence/PRELIM-NPP-01-Paste-Copy-Back.png | encoded message pasted into unsaved Notepad++ document |
| Terminal output | tests/week10_testing/preliminary_testing/Notepad++/evidence/PRELIM-NPP-01-Terminal.png | terminal results from decode attempt |
| Retrieved text or other record | tests/week10_testing/preliminary_testing/Notepad++/week10_NPP-01_sa01_retrieved.txt | Contains the text copied  |

## 5. Notes and Blockers

- **Unexpected behavior:** None observed during the preliminary Notepad++ paste-and-copy-back test.
- **Errors or limitations:** No command errors were observed. The preliminary check covers Notepad++ copy-back behavior only; it does not establish results for other platforms or count as an official production trial. The retrieved text was saved to a separate plain-text file for analysis without saving the encoded message within Notepad++.
- **File organization and naming convention:** Preliminary artifacts are stored by platform under `tests/week10_testing/preliminary_testing/`. Text artifacts use `week10_<Platform>-<TrialNumber>_<CorpusID>_<Purpose>.txt`; this completed check uses `week10_NPP-01_sa01_encoded.txt` and `week10_NPP-01_sa01_retrieved.txt`. Future production records must remain separate and use their assigned trial identifiers.
- **Questions requiring team confirmation:** None for this completed preliminary-check file organization. Official production testing remains separate from these preliminary checks.
- **Next action:** Commit the completed preliminary-check documentation and evidence, push the changes to the existing tristan-week10 branch and pull request, and notify Ifeanyi that the Notepad++ preliminary check is ready for review. After review and acceptance, continue with the remaining preliminary platform checks, keeping their results separate from production data collection.

---

# Week 10 Workflow Verification — Google Chrome Console

**Platform:** Google Chrome Console
**Operation:** Paste and copy back
**Access Status:** Confirmed
**Verification status:** Verified
**Date verified:** 10/23/2026
**Tester:** Tristan Koch

## 1. Access

- **Application/site opened:** Google Chrome developer tools console opened successfully
- **Relevant feature accessible:** Chrome developer tool console opened successfully
- **Version or environment:** Google Chrome, Version 156.0.8078.48 (Official Build) (64-bit); Windows 11 64-bit
- **Access limitations:** None observed during access and preliminary workflow verification. This was not an official production trial.

## 2. Workflow Steps

### Steps

1. Confirm access to the Google Chrome console and open the relevant editing or input area.
2. Select an approved corpus message and record its corpus ID.
3. Encode the message using the project encoder and the approved codec configuration.
4. Perform a local encode/decode round-trip test to verify that the original message can be recovered exactly.
5. Save the encoded text and record the number of zero-width characters sent, including counts for U+200B, U+200C, and U+200D.
6. Copy the encoded text and paste it into the target application or console.
7. Follow the approved procedure to copy the text back out of the application or console without intentionally modifying it.
8. Save the retrieved text and any required screenshots or terminal output.
9. Run the decoder on the retrieved text and compare the recovered message with the original corpus message.
10. Record the retrieved zero-width character counts, retention rate, decoder success, exact-recovery result, and any errors or limitations.
11. Document the workflow outcome and any deviations from the approved procedure.

**Workflow result:** Completed

## 3. Preliminary Feasibility Check

- Preliminary check ID: PRELIM-CHROME_CONSOLE-01
- Platform-operation: Google Chrome Browser Console — paste and copy back
- Expected behavior: local SA01 recovery is exactly Hello; Console copy-back is measured without repair.
- Observed result: Local encode/decode round-trip succeeded. After copying the encoded message into Google Chrome Browser Console and copying it back, all 152 zero-width characters were preserved. The retrieved text matched the encoded text exactly, and decoding recovered Hello.
- Corpus ID / expected SHA-256: SA01 / 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
- Codec configuration: src/zero_width_codec.py; cover "Team 1 compatibility test."; recovery_mode=False
- Browser (must be Google Chrome): Google Chrome;
- Precise Chrome version: Version 156.0.8078.48(Official Build) (64-bit);
- Operating system: Windows 11 64-bit
- Encoded U+200B / U+200C / U+200D / total: 84 / 52 / 16 / 152
- Retrieved U+200B / U+200C / U+200D / total: 84 / 52 / 16 / 152
- Retention percentage: 100.00%
- Exact encoded-text match: True
- Decode result and error: decode succeeded: True; recovered secret: 'Hello'; no error reported
- Recovered secret exactly equals Hello: Yes
- Evidence references:
    - Paste-and-Copy-Back: `tests/week10_testing/preliminary_testing/Google_Chrome_Browser_Console/evidence/PRELIM-Chrome-01-Paste-Copy-Back.png`
    - Terminal results: `tests/week10_testing/preliminary_testing/Google_Chrome_Browser_Console/evidence/PRELIM-Chrome-01-Terminal.png`
- Limitations and observations: This was a preliminary feasibility check, not an official production trial. The encoded message was pasted into Chrome Browser Console and copied back. The copied-back text was pasted into a separate plain-text file named `week10_Chrome-01_sa01_retrieved.txt` so the retrieval and analysis commands could evaluate it. No manual repair was performed.
- **Next steps:** Retain the verification summary entry showing that the Google Chrome Browser Console preliminary workflow was completed and decoding succeeded.

> These results are for workflow verification. Do not count them as official production trials unless the team confirms that they qualify.

## 4. Evidence

| Evidence | File path or link | What it demonstrates |
|---|---|---|
| Screenshot | tests/week10_testing/preliminary_testing/Google_Chrome_Browser_Console/evidence/PRELIM-Chrome-01-Paste-Copy-Back.png | Encoded message pasted into Google Chrome Browser Console |
| Terminal output | tests/week10_testing/preliminary_testing/Google_Chrome_Browser_Console/evidence/PRELIM-Chrome-01-Terminal.png | Terminal results from decode attempt |
| Retrieved text or other record | tests/week10_testing/preliminary_testing/Google_Chrome_Browser_Console/week10_Chrome-01_sa01_retrieved.txt | Contains message copied back from Google Chrome Browser Console |

## 5. Notes and Blockers

- **Unexpected behavior:** None observed during Google Chrome Browser Console Paste-and-Copy-Back preliminary test.
- **Errors or limitations:** No command errors were observed. The preliminary check covers Google Chrome Console copy-back behavior only; it does not establish results for other platforms or count as an official production trial. The retrieved text was saved to a separate plain-text file for analysis
- **Questions requiring team confirmation:** No questions
- **Next action:** Retain the verification summary entry showing that the Google Chrome Browser Console preliminary workflow was completed and decoding succeeded.

---

# Verification Summary

| Platform | Approved operation | Access | Workflow verification; Decode Success/Fail |
|---|---|---|---|
| Gmail | Send and retrieve message | Confirmed | Verified; decode failed |
| Discord | Send and retrieve message | Confirmed | Verified; decode success |
| Microsoft Word | Save, reopen, and retrieve text | Confirmed | Verified; decode failed |
| Microsoft Outlook | Send and retrieve message | Confirmed | Verified; decode success |
| Telegram Web | Send and retrieve message | Confirmed | Verified; decode success |
| Notepad++ | Paste and copy back | Confirmed | Verified; decode success |
| Google Chrome Browser Console | Paste and copy back | Confirmed | Verified; decode success |

**Current status:** Preliminary workflow checks documented as completed, with Gmail and Microsoft Word decoding failures recorded separately from successful recoveries; official production testing has not begun.

*Preliminary feasibility checks must remain separate from official production-trial results unless the team confirms otherwise.*
