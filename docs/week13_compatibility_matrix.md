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

**Final Week 13 verification:** An independent audit of all individual production-testing JSON records identified 168 planned trials across seven platforms. Of these, 165 were completed and three Discord LA02 trials were blocked before transmission. No production records remain pending.

Among the 165 completed trials, 112 achieved exact secret recovery, representing a 67.88% completed-trial exact recovery rate.

| Platform | Planned | Completed | Exact Recoveries | Blocked | Failed |
|---|---:|---:|---:|---:|---:|
| Discord | 24 | 21 | 21 | 3 | 0 |
| Gmail | 24 | 24 | 0 | 0 | 24 |
| Browser Console | 24 | 24 | 24 | 0 | 0 |
| Microsoft Outlook | 24 | 24 | 19 | 0 | 5 |
| Microsoft Word | 24 | 24 | 0 | 0 | 24 |
| Notepad++ | 24 | 24 | 24 | 0 | 0 |
| Telegram Web | 24 | 24 | 24 | 0 | 0 |
| **Total** | **168** | **165** | **112** | **3** | **53** |

The three blocked Discord LA02 trials have no retrieved payload or decoder measurements and are excluded from the completed-trial recovery denominator. These findings describe the tested application workflows and should not be interpreted as universal compatibility guarantees.

### Microsoft Outlook Compatibility Verification

Microsoft Outlook was evaluated using all 24 trial records. All 24 have completed analysis. Nineteen trials achieved exact recovery and five failed exact recovery. Aggregate retention was 90.27%, with U+200B at 90.32%, U+200C at 90.19%, and U+200D at 90.37%.

The restored SU02 records are included in these totals: SU02 R1 and R2 achieved exact recovery with 100% retention, while SU02 R3 was a completed failed recovery with complete payload removal and 0% retention. No suspected technical cause is asserted beyond the recorded outcomes.

## 3. Interpretation

The production-testing results demonstrate that compatibility depends on how each application processes zero-width Unicode characters. Gmail retained 5.41% aggregate character retention and achieved no exact recoveries. Microsoft Word showed 0% retention and no successful recoveries. Notepad++, Browser Console, and Telegram Web preserved all tested payloads and achieved exact recovery in all 24 trials. Discord preserved all zero-width characters and achieved exact recovery in all 21 executed trials; its three LA02 repetitions were blocked before transmission because the original encoded payload exceeded the standard message-size limit. Outlook retained 90.27% overall and achieved 19/24 exact recoveries.

Across the 165 completed platform-production trials, 112 achieved exact recovery. The three blocked Discord LA02 records have no retrieved payload or decoder measurements, so they are not decoding failures and are excluded from recovery comparisons. These totals cover platform production testing only; the separate Baseline-versus-Hamming comparative experiment is not included.

These findings apply to the documented test procedures and should not be interpreted as universal behavior across all application versions or workflows.

## 4. Final status and limitations

The matrix was cross-checked against the individual production-trial JSON records and supporting evidence. The three Discord LA02 platform blocks remain distinct from completed decoder failures, and the final results are integrated into the Week 13 report and chart datasets.

**Status:** Production testing is complete for all seven platforms represented in the final records. Three Discord trials remain blocked by the platform message-size limitation; no trials remain pending. Platform-result verification and report integration are complete for the current Week 13 dataset.
