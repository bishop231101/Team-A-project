# CS481 Team 1 — Week 9 Data Quality Audit

**Week:** 9 (October 12–18, 2026)  
**Responsible:** Ifeanyi — Team Leader  
**Project:** Zero-Width Unicode Steganography with Social-Media Robustness Engineering

## 1. Purpose

The purpose of this audit is to ensure that production trial data is complete, accurate, consistent, and suitable for statistical analysis.

The Week 9 milestone is to complete at least 50% of the planned production data collection.

## 2. Data Validation Checklist

Each production trial will be reviewed for the following:

- [ ] Platform name is recorded.
- [ ] Test number or unique trial identifier is recorded.
- [ ] Original message or approved test-case reference is recorded.
- [ ] Number of zero-width characters sent is recorded.
- [ ] Number of zero-width characters recovered is recorded.
- [ ] Number of characters lost or corrupted is recorded.
- [ ] Character survival rate is calculated correctly.
- [ ] Exact-match decoding success or failure is recorded.
- [ ] Platform behavior and anomalies are documented.
- [ ] Duplicate records are identified.
- [ ] Missing fields and impossible values are flagged.
- [ ] Manual transcription errors are checked against original evidence.

## 3. Validation Rules

- Character counts must be nonnegative integers.
- The number of recovered characters cannot exceed the number sent without an explanation of inserted or duplicated characters.
- Survival rate = (matching zero-width characters recovered / zero-width characters sent) × 100.
- Exact-match recovery must be recorded separately from character survival.
- Any unexpected result must be documented for further review.
- Zero-length encoded trials require separate handling because the survival-rate denominator would be zero.

## 4. Compatibility Matrix Audit

The following platforms were identified in the original testing requirements:

| Platform | Week 9 Production Trials | Validation Status | Notes |
|---|---|---|---|
| WeChat | Pending | Not reviewed | |
| Telegram | Pending | Not reviewed | |
| Gmail | Pending | Not reviewed | |
| Microsoft Word | Pending | Not reviewed | |
| Notepad++ | Pending | Not reviewed | |
| Browser Console | Pending | Not reviewed | |
| Microsoft Outlook | Pending | Not reviewed | |
| Discord | Pending | Not reviewed | |

The final matrix will be updated using Tristan's actual production data. Previous prototype results will remain separate from the Week 9 production dataset.

## 5. Audit Findings

**Records reviewed:** Pending  
**Missing or incomplete records:** Pending  
**Duplicate records:** Pending  
**Invalid values:** Pending  
**Unexplained anomalies:** Pending

No Week 9 production dataset has been audited at the time this document was created.

## 6. Team Coordination

**Tristan:** Provide production trial logs, supporting evidence, and preliminary statistics.

**Henry:** Investigate codec-related anomalies and verify decoding behavior on recovered sequences.

**Ifeanyi:** Audit trial records, document data-quality findings, and maintain the compatibility matrix.

## 7. Week 9 Progress

**Target:** At least 50% of planned production trials completed.

**Current verified progress:** Pending review of production trial logs.

**Next Action:** Review Tristan's first production data batch and record validation findings.

## 8. Methodology Review and Production Data Requirements

**Review Date:** October 12, 2026  
**Reviewed By:** Ifeanyi  
**Reference:** Tristan's Week 8 Testing Methodology

### Previous Testing Methodology

The team previously evaluated platform compatibility and recovery performance under controlled corruption conditions.

Testing recorded zero-width characters sent and recovered, character survival rates, decoding outcomes, and platform behavior.

### Data Quality Improvements for Week 9

The following requirements will be checked during the production data audit:

- [ ] Record the platform and application/browser version.
- [ ] Record the exact operation performed during each trial.
- [ ] Use a unique identifier for each trial.
- [ ] Record the test message or approved corpus reference.
- [ ] Verify character counts and survival-rate calculations.
- [ ] Record exact-match decoding success separately from survival rate.
- [ ] Document decoder errors and unexpected platform behavior.
- [ ] Preserve supporting evidence for each trial.
- [ ] Check for missing fields, duplicate trials, and inconsistent results.
- [ ] Confirm that the approved frozen protocol was followed.

### Production Dataset Verification

**Frozen testing protocol:** Awaiting confirmation of the approved Week 9 version.

**Balanced test corpus:** Awaiting confirmation of the approved corpus and its test-case distribution.

**Total planned production trials:** Pending.

**Completed production trials:** Pending verification.

**Week 9 milestone:** At least 50% of the planned production dataset completed.

### Audit Status

The Week 8 testing methodology has been reviewed to identify required measurements and previous documentation limitations.

The Week 9 production dataset has not yet been independently validated. Audit findings and completion percentages will be updated after Tristan provides the production trial logs.