# Week 10 Workflow Verification's
**Prepared by:** Tristan Koch
**Date:** October 20, 2026
**Project:** Zero-Width Unicode Steganography with Social-Media Robustness Engineering
**Status:** In Progress

# Week 10 Workflow Verification — Gmail

**Platform:** Gmail
**Operation:** Send and Retrieve message
**Access Status:** Confirmed
**Verification status:** Pending
**Date verified:** Pending
**Tester:** Tristan Koch


## 1. Access

- **Application/site opened:** Gmail website opened in Google Chrome
- **Relevant feature accessible:** Compose window opened successfully
- **Version or environment:** Google Chrome, Version 156.0.8078.48 (Official Build) (64-bit); Windows 11 64-bit
- **Access limitations:** None Observed during access-only verification; the full encode/send/retrieve/compare/decode workflow has not been tested.

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

**Workflow result:** [Completed / Partially completed / Blocked]

## 3. Preliminary Feasibility Check

- **Test message/corpus ID:** [If a test was performed]
- **Codec configuration:** [Configuration used]
- **Operation attempted:** [Describe]
- **Message retrieved successfully:** [Yes / No / Not tested]
- **Decoder succeeded:** [Yes / No / Not tested]
- **Exact message recovery:** [Yes / No / Not tested]
- **Character counts and retention:** [Record if measured]
- **Result or limitation:** [Describe]

> These results are for workflow verification. Do not count them as official production trials unless the team confirms that they qualify.

## 4. Evidence

| Evidence | File path or link | What it demonstrates |
|---|---|---|
| Screenshot | [Path] | [What is shown] |
| Terminal output | [Path] | [What is shown] |
| Retrieved text or other record | [Path] | [What is shown] |

## 5. Notes and Blockers

- **Unexpected behavior:** [None / Describe]
- **Errors or limitations:** [None / Describe]
- **Questions requiring team confirmation:** [None / Describe]
- **Next action:** [Action or None]

---

# Week 10 Workflow Verification — Discord

**Platform:** Discord
**Operation:** Send and Retrieve message
**Access Status:** Confirmed
**Verification status:** Pending 
**Date verified:** Pending
**Tester:** Tristan Koch

## 1. Access

- **Application/site opened:** Discord app opened successfully
- **Relevant feature accessible:** Text chat accessed successfully
- **Version or environment:** Discord, Build number 643186; Windows 11 64-bit
- **Access limitations:** None Observed during access-only verification; the full encode/send/retrieve/compare/decode workflow has not been tested.

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

**Workflow result:** [Completed / Partially completed / Blocked]

## 3. Preliminary Feasibility Check

- **Test message/corpus ID:** [If a test was performed]
- **Codec configuration:** [Configuration used]
- **Operation attempted:** [Describe]
- **Message retrieved successfully:** [Yes / No / Not tested]
- **Decoder succeeded:** [Yes / No / Not tested]
- **Exact message recovery:** [Yes / No / Not tested]
- **Character counts and retention:** [Record if measured]
- **Result or limitation:** [Describe]

> These results are for workflow verification. Do not count them as official production trials unless the team confirms that they qualify.

## 4. Evidence

| Evidence | File path or link | What it demonstrates |
|---|---|---|
| Screenshot | [Path] | [What is shown] |
| Terminal output | [Path] | [What is shown] |
| Retrieved text or other record | [Path] | [What is shown] |

## 5. Notes and Blockers

- **Unexpected behavior:** [None / Describe]
- **Errors or limitations:** [None / Describe]
- **Questions requiring team confirmation:** [None / Describe]
- **Next action:** [Action or None]

---

# Week 10 Workflow Verification — Microsoft Word

**Platform:** Microsoft Word
**Operation:** Save, Reopen, and retrieve text
**Access Status:** Confirmed
**Verification status:** Pending 
**Date verified:** Pending
**Tester:** Tristan Koch

## 1. Access

- **Application/site opened:** Microsoft Word app opened successfully
- **Relevant feature accessible:** Blank document was opened with no issues
- **Version or environment:** Microsoft® Word for Microsoft 365 MSO (Version 2609 Build 16.0.20430.20032) 64-bit; Windows 11 64-bit
- **Access limitations:** None Observed during access-only verification; the full encode/send/retrieve/compare/decode workflow has not been tested.

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

**Workflow result:** [Completed / Partially completed / Blocked]

## 3. Preliminary Feasibility Check

- **Test message/corpus ID:** [If a test was performed]
- **Codec configuration:** [Configuration used]
- **Operation attempted:** [Describe]
- **Message retrieved successfully:** [Yes / No / Not tested]
- **Decoder succeeded:** [Yes / No / Not tested]
- **Exact message recovery:** [Yes / No / Not tested]
- **Character counts and retention:** [Record if measured]
- **Result or limitation:** [Describe]

> These results are for workflow verification. Do not count them as official production trials unless the team confirms that they qualify.

## 4. Evidence

| Evidence | File path or link | What it demonstrates |
|---|---|---|
| Screenshot | [Path] | [What is shown] |
| Terminal output | [Path] | [What is shown] |
| Retrieved text or other record | [Path] | [What is shown] |

## 5. Notes and Blockers

- **Unexpected behavior:** [None / Describe]
- **Errors or limitations:** [None / Describe]
- **Questions requiring team confirmation:** [None / Describe]
- **Next action:** [Action or None]

---

# Week 10 Workflow Verification — Microsoft Outlook

**Platform:** Microsoft Outlook
**Operation:** Send and Retrieve message
**Access Status:** Confirmed
**Verification status:** Pending
**Date verified:** Pending
**Tester:** Tristan Koch

## 1. Access

- **Application/site opened:** Microsoft Outlook website loaded successfully
- **Relevant feature accessible:** Compose window opened successfully.
- **Version or environment:** Could not find Outlook website version; Windows 11 64-bit
- **Access limitations:** Cannot seem to find Outlook website version during access-only verification, but access was successful, the full encode/send/retrieve/compare/decode workflow has not been tested.

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

**Workflow result:** [Completed / Partially completed / Blocked]

## 3. Preliminary Feasibility Check

- **Test message/corpus ID:** [If a test was performed]
- **Codec configuration:** [Configuration used]
- **Operation attempted:** [Describe]
- **Message retrieved successfully:** [Yes / No / Not tested]
- **Decoder succeeded:** [Yes / No / Not tested]
- **Exact message recovery:** [Yes / No / Not tested]
- **Character counts and retention:** [Record if measured]
- **Result or limitation:** [Describe]

> These results are for workflow verification. Do not count them as official production trials unless the team confirms that they qualify.

## 4. Evidence

| Evidence | File path or link | What it demonstrates |
|---|---|---|
| Screenshot | [Path] | [What is shown] |
| Terminal output | [Path] | [What is shown] |
| Retrieved text or other record | [Path] | [What is shown] |

## 5. Notes and Blockers

- **Unexpected behavior:** [None / Describe]
- **Errors or limitations:** [None / Describe]
- **Questions requiring team confirmation:** [None / Describe]
- **Next action:** [Action or None]

---

# Week 10 Workflow Verification — Telegram Web

**Platform:** Telegram Web
**Operation:** Send and Retrieve message
**Access Status:** Confirmed
**Verification status:** Pending 
**Date verified:** Pending
**Tester:** Tristan Koch

## 1. Access

- **Application/site opened:** Telegram Web - website opened successfully
- **Relevant feature accessible:** Telegram text chat opened successfully
- **Version or environment:** Could not find Telegram Web version number; Windows 11 64-bit
- **Access limitations:** Cannot seem to find Telegram Web version during access-only verification, but access was successful, the full encode/send/retrieve/compare/decode workflow has not been tested.

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

**Workflow result:** [Completed / Partially completed / Blocked]

## 3. Preliminary Feasibility Check

- **Test message/corpus ID:** [If a test was performed]
- **Codec configuration:** [Configuration used]
- **Operation attempted:** [Describe]
- **Message retrieved successfully:** [Yes / No / Not tested]
- **Decoder succeeded:** [Yes / No / Not tested]
- **Exact message recovery:** [Yes / No / Not tested]
- **Character counts and retention:** [Record if measured]
- **Result or limitation:** [Describe]

> These results are for workflow verification. Do not count them as official production trials unless the team confirms that they qualify.

## 4. Evidence

| Evidence | File path or link | What it demonstrates |
|---|---|---|
| Screenshot | [Path] | [What is shown] |
| Terminal output | [Path] | [What is shown] |
| Retrieved text or other record | [Path] | [What is shown] |

## 5. Notes and Blockers

- **Unexpected behavior:** [None / Describe]
- **Errors or limitations:** [None / Describe]
- **Questions requiring team confirmation:** [None / Describe]
- **Next action:** [Action or None]

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
- **Access limitations:** None observed during access-only verification; the full encode/send/retrieve/compare/decode workflow has not been tested.

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
    - Paste-and-Copy-Back: `tests/week10_testing/screenshots/tristan/preliminary-testing/Notepad++/PRELIM-NPP-01-Paste-Copy-Back.png` 
    - Terminal results: `tests/week10_testing/screenshots/tristan/preliminary-testing/Notepad++/PRELIM-NPP-01-Terminal.png`
- Limitations and observations: This was a preliminary feasibility check, not an official production trial. The encoded message was pasted into Notepad++ and copied back without saving it in Notepad++. The copied-back text was pasted into a separate plain-text file named week10_sa01_retrieved.txt so the retrieval and analysis commands could evaluate it. No manual repair was performed.
- Next steps: Commit the documentation and evidence associated with this preliminary check, push the changes to the existing tristan-week10 branch and pull request, and notify Ifeanyi that the preliminary check is complete and ready for review. After the pull request is reviewed and accepted, proceed with the remaining preliminary platform checks. Keep all preliminary results separate from official production data collection.

> These results are for workflow verification. Do not count them as official production trials unless the team confirms that they qualify.

## 4. Evidence

| Evidence | File path or link | What it demonstrates |
|---|---|---|
| Screenshot | tests/week10_testing/screenshots/tristan/preliminary-testing/Notepad++/PRELIM-NPP-01-Paste-Copy-Back.png | encoded message pasted into unsaved Notepad++ document |
| Terminal output | tests/week10_testing/screenshots/tristan/preliminary-testing/Notepad++/PRELIM-NPP-01-Terminal.png | terminal results from decode attempt |
| Retrieved text or other record | week10_sa01_retrieved.txt | Contains the text copied  |

## 5. Notes and Blockers

- **Unexpected behavior:** None observed during the preliminary Notepad++ paste-and-copy-back test.
- **Errors or limitations:** No command errors were observed. The preliminary check covers Notepad++ copy-back behavior only; it does not establish results for other platforms or count as an official production trial. The retrieved text was saved to a separate plain-text file for analysis without saving the encoded message within Notepad++.
- **Questions requiring team confirmation:**
  1. **Output file location:** The local encode/round-trip check currently saves the generated encoded message file in the repository root. Should future preliminary and production test files be saved in platform- and test-specific directories instead? For example, something like `tests/week10_testing/preliminary-testing/Notepad++/`.
  2. **Test-specific filenames:** Should we adopt filenames that identify the platform and corpus entry, rather than using generic names such as `week10_sa01_encoded.txt` and `week10_sa01_retrieved.txt`? For example, `week10_NPP_sa01_encoded.txt` and `week10_NPP_sa01_retrieved.txt`. This would make the files easier to associate with the correct test and reduce the risk of overwriting or confusing results from different platforms.
  For future production data collection, where the same corpus message may be tested across multiple trials, we could also include a unique trial ID in each filename. For example, `week10_NPP-01_sa01_encoded.txt` and `week10_NPP-01_sa01_retrieved.txt`, where NPP-01 identifies the Notepad++ trial and sa01 identifies the corpus entry. Should we adopt a consistent naming convention that includes the platform, trial ID when applicable, corpus ID, and file purpose across the preliminary and production testing guides?
    - For now, the files associated with this Notepad++ preliminary feasibility check will retain their original naming conventions and remain in the repository root. This preserves consistency with the commands used during the test and makes it clear where the encoded message is generated and where the user-created retrieved-text file must be saved if the test needs to be repeated. Any changes to file locations or naming conventions will be made after the team confirms the preferred approach.
  3. **Scope of changes:** If the team agrees on a new directory and naming convention, should we update the existing preliminary guides and future production-testing guides to use it consistently? I have not made these changes pending team confirmation.
- **Next action:** Commit the completed preliminary-check documentation and evidence, push the changes to the existing tristan-week10 branch and pull request, and notify Ifeanyi that the Notepad++ preliminary check is ready for review. After review and acceptance, continue with the remaining preliminary platform checks, keeping their results separate from production data collection.

---

# Week 10 Workflow Verification — Google Chrome Console

**Platform:** Google Chrome Console
**Operation:** Paste and copy back
**Access Status:** Confirmed
**Verification status:** Pending
**Date verified:** Pending
**Tester:** Tristan Koch

## 1. Access

- **Application/site opened:** Google Chrome developer tools console opened successfully
- **Relevant feature accessible:** Chrome developer tool console opened successfully
- **Version or environment:** Google Chrome, Version 156.0.8078.48 (Official Build) (64-bit); Windows 11 64-bit
- **Access limitations:** None Observed during access-only verification; the full encode/send/retrieve/compare/decode workflow has not been tested.

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

**Workflow result:** [Completed / Partially completed / Blocked]

## 3. Preliminary Feasibility Check

- **Test message/corpus ID:** [If a test was performed]
- **Codec configuration:** [Configuration used]
- **Operation attempted:** [Describe]
- **Message retrieved successfully:** [Yes / No / Not tested]
- **Decoder succeeded:** [Yes / No / Not tested]
- **Exact message recovery:** [Yes / No / Not tested]
- **Character counts and retention:** [Record if measured]
- **Result or limitation:** [Describe]

> These results are for workflow verification. Do not count them as official production trials unless the team confirms that they qualify.

## 4. Evidence

| Evidence | File path or link | What it demonstrates |
|---|---|---|
| Screenshot | [Path] | [What is shown] |
| Terminal output | [Path] | [What is shown] |
| Retrieved text or other record | [Path] | [What is shown] |

## 5. Notes and Blockers

- **Unexpected behavior:** [None / Describe]
- **Errors or limitations:** [None / Describe]
- **Questions requiring team confirmation:** [None / Describe]
- **Next action:** [Action or None]

---

# Verification Summary

| Platform | Approved operation | Access | Workflow verification |
|---|---|---|---|
| Gmail | Send and retrieve message | Confirmed | Still awaiting verification |
| Discord | Send and retrieve message | Confirmed | Still awaiting verification |
| Microsoft Word | Save, reopen, and retrieve text | Confirmed | Still awaiting verification |
| Microsoft Outlook | Send and retrieve message | Confirmed | Still awaiting verification |
| Telegram Web | Send and retrieve message | Confirmed | Still awaiting verification |
| Notepad++ | Paste and copy back | Confirmed | Verified |
| Browser Console | Paste and copy back | Confirmed | Still awaiting verification |

**Current status:** Workflow procedures documented; platform access verified, preliminary feasibility checks pending.

*Preliminary feasibility checks must remain separate from official production-trial results unless the team confirms otherwise.*