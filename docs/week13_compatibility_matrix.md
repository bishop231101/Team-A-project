# Week 13 — Platform Compatibility Matrix

**Project:** Zero-Width Unicode Steganography  
**Reporting Period:** November 9–15, 2026  
**Prepared by:** Ifeanyi Emeka

## 1. Objective

Evaluate and document how different applications handle zero-width Unicode characters and whether embedded messages can be recovered after platform processing.

## 2. Existing Production-Testing Results

| Platform | Trials | Exact Recovery | Observed Behavior |
|---|---:|---:|---|
| Gmail | 24 | 0/24 (0%) | Zero-width character stripping prevented exact recovery. |
| Notepad++ | 24 | 24/24 (100%) | Zero-width characters were preserved, allowing exact recovery. |
| Microsoft Word | 24 | 0/24 (0%) | Zero-width payload characters were removed. |
| Discord | 24 planned; 21 completed, 3 blocked | 21/21 (100%) across completed trials | Discord preserved all zero-width characters and achieved exact recovery in all 21 executed trials. LA02 R1-R3 were blocked before transmission because the original encoded payload exceeded the standard Discord message-size limit; sending it would require Discord Nitro. |

**Completed analyzed trials:** 93. **Additional blocked Discord trials:** 3. **Total accounted-for trial records:** 96. The 93 completed trials consist of 24 Gmail, 24 Notepad++, 24 Microsoft Word, and 21 Discord trials.

## 3. Interpretation

The existing results demonstrate that compatibility depends on how each application processes zero-width Unicode characters.

Notepad++ and Discord preserved the tested payloads in their completed trials, while Gmail and Microsoft Word did not support exact recovery under the tested conditions.

Analysis of the 93 completed production-testing records confirmed significant differences in zero-width Unicode character preservation across Gmail, Notepad++, Microsoft Word, and Discord. Notepad++ achieved 100% average character retention and exact recovery in all 24 trials. Gmail retained an average of 23.87% of encoded characters but achieved no exact recoveries. Microsoft Word showed 0% retention and no successful recoveries. Discord preserved all zero-width characters across its 21 executed trials and achieved exact recovery in all 21. The three Discord LA02 repetitions were blocked before transmission because the original encoded payload exceeded the standard message-size limit; they have no retrieval or decoder measurements and must not be counted as decoding failures or included in recovery comparisons.

These findings apply to the documented test procedures and should not be interpreted as universal behavior across all application versions or workflows.

## 4. Remaining Week 13 Work

- Cross-check matrix entries against the original production-trial records.
- Add references to supporting evidence and screenshots.
- Document tested operations and application limitations.
- Identify platforms and operations not yet evaluated, including Telegram Web, Microsoft Outlook, and Chrome Browser Console.
- Incorporate validated findings into the Week 13 report.

**Status:** Initial matrix prepared; source verification and additional analysis pending.
