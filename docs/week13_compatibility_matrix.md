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

### Updated Week 13 Compatibility Verification — November 12, 2026

An independent PowerShell audit of the production-testing JSON records identified 168 planned trials across seven platforms. Of these, 150 were completed, 15 Microsoft Outlook trials remained pending manual transfer, and three Discord trials were blocked.

Among the 150 completed trials, 99 achieved exact secret recovery, representing a 66.00% exact recovery rate.

| Platform | Planned | Completed | Exact Recoveries | Pending/Blocked |
|---|---:|---:|---:|---:|
| Discord | 24 | 21 | 21 | 3 blocked |
| Gmail | 24 | 24 | 0 | 0 |
| Browser Console | 24 | 24 | 24 | 0 |
| Microsoft Outlook | 24 | 9 | 6 | 15 pending |
| Microsoft Word | 24 | 24 | 0 | 0 |
| Notepad++ | 24 | 24 | 24 | 0 |
| Telegram Web | 24 | 24 | 24 | 0 |
| **Total** | **168** | **150** | **99** | **18** |

The verification identified three blocked Discord LA02 trials and 15 Microsoft Outlook trials with `ready_for_manual_transfer` status. No other incomplete records were identified.

These findings are based on the recorded production-testing results. They describe the tested application workflows and should not be interpreted as universal compatibility guarantees.

The remaining Outlook trials will be incorporated into the final statistics after testing, analysis, and evidence verification are completed.

### Microsoft Outlook Compatibility Verification

Microsoft Outlook was evaluated using 24 prepared trial records. Nine trials have completed analysis, while 15 remain pending manual transfer and retrieval.

Of the nine completed trials, six achieved exact recovery with 100% character retention, while three failed exact recovery with 0% retention.

An additional verification of the 15 pending records confirmed that their JSON files contain no measured results and their retrieved-text files are empty (0 bytes). These records remain pending and are excluded from the completed-trial success rate.

The completed Outlook trials therefore achieved a 66.67% exact recovery rate (6 of 9). These findings apply only to the tested Outlook workflows and should not be interpreted as universal Outlook compatibility.

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
