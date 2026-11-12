# Week 13 — Platform Compatibility Matrix

**Project:** Zero-Width Unicode Steganography  
**Reporting Period:** November 9–15, 2026  
**Prepared by:** Ifeanyi Emeka

## 1. Objective

Evaluate and document how different applications handle zero-width Unicode characters and whether embedded messages can be recovered after platform processing.

## 2. Existing Production-Testing Results

| Platform | Trials | Exact Recovery | Observed Behavior |
|---|---:|---:|---|
| Gmail | 24 completed | 0/24 (0%) | Zero-width character stripping prevented exact recovery. |
| Notepad++ | 24 completed | 24/24 (100%) | Zero-width characters were preserved, allowing exact recovery. |
| Microsoft Word | 24 completed | 0/24 (0%) | Zero-width payload characters were removed. |
| Discord | 24 planned; 21 completed, 3 blocked | 21/21 (100%) across completed trials | Discord preserved all zero-width characters and achieved exact recovery in all 21 executed trials. LA02 R1-R3 were blocked before transmission because the original encoded payload exceeded the standard message-size limit; sending it would require Discord Nitro. |
| Telegram Web | 24 completed | 24/24 (100%) | Telegram Web preserved all zero-width characters and achieved exact recovery in every completed trial. |

**Pre-Telegram baseline:** 96 planned trials, 93 completed and analyzed trials, 3 blocked Discord trials, and 45 exact recoveries out of 93 completed trials.

**Overall:** 120 planned trials, 117 completed and analyzed trials, 3 blocked Discord trials, and 69 exact recoveries out of 117 completed trials (approximately 59.0%).

## 3. Interpretation

The production-testing results demonstrate that compatibility depends on how each application processes zero-width Unicode characters. Gmail retained an average of 23.87% of encoded characters and achieved no exact recoveries. Microsoft Word showed 0% retention and no successful recoveries. Notepad++ preserved all tested payloads and achieved exact recovery in all 24 trials. Discord preserved all zero-width characters and achieved exact recovery in all 21 executed trials; its three LA02 repetitions were blocked before transmission because the original encoded payload exceeded the standard message-size limit. Telegram Web preserved all zero-width characters and achieved exact recovery in all 24 completed trials.

Across the 117 completed platform-production trials, 69 achieved exact recovery. The three blocked Discord LA02 records have no retrieved payload or decoder measurements, so they are not decoding failures and are excluded from recovery comparisons. These totals cover platform production testing only; the separate Baseline-versus-Hamming comparative experiment is not included.

These findings apply to the documented test procedures and should not be interpreted as universal behavior across all application versions or workflows.

## 4. Remaining Week 13 Work

- Cross-check matrix entries against the original production-trial records.
- Add references to supporting evidence and screenshots.
- Document tested operations and application limitations.
- Identify platforms and operations not yet evaluated, including Microsoft Outlook and Chrome Browser Console.
- Incorporate validated findings into the Week 13 report.

**Status:** Gmail, Notepad++, Microsoft Word, Discord, and Telegram Web production testing is complete. Microsoft Outlook and Chrome Browser Console remain to be evaluated; platform-result verification and report integration remain in progress.
