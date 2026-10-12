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