# CS481 – Team 1 Weekly Report 10

**Project:** Zero-Width Unicode Steganography with Social-Media Robustness Engineering  
**Team Leader:** Ifeanyi Emeka  
**Team Members:** Ifeanyi Emeka, Tristan Koch, Henry Smith  
**Reporting Period:** Week 10 (October 19–25, 2026)  
**Status:** In Progress

## 1. Weekly Overview

During Week 10, our team is transitioning from testing preparation and protocol development into controlled production testing. Our primary focus is verifying the approved testing workflows, collecting reliable results, and maintaining proper documentation.

As team leader, I have continued coordinating responsibilities, documenting meetings, monitoring contributions, and preparing our data-quality audit.

Production testing results will be added only after the supporting logs and evidence have been reviewed.

## 2. Milestones and Progress

### Completed

- Conducted the Monday, October 19, team meeting with all members present.
- Documented the meeting in `meeting_minutes/2026-10-19_week10.md`.
- Established the Week 10 data-quality audit in `docs/week10_data_quality_audit.md`.
- Created the team leader's Week 10 individual journal in `weekly_journals/ifeanyi/week10.md`.
- Confirmed that the approved production testing scope consists of seven platform-operation combinations and 168 planned trials.
- Identified outstanding workflow verification and production testing requirements.

### In Progress

- Confirming access to the approved platforms and their exact testing workflows.
- Preparing controlled production testing using the approved message corpus.
- Collecting screenshots, testing logs, and measurable results.
- Reviewing decoder behavior and any failures observed during testing.

## 3. Individual Team Contributions

### Ifeanyi Emeka – Team Leader

- Organized and documented the Monday team meeting.
- Created the Week 10 data-quality audit.
- Updated the individual journal.
- Continued monitoring the testing protocol, GitHub contributions, and team progress.
- Coordinated outstanding responsibilities and documentation requirements.

### Tristan Koch – Platform Testing

**Assigned responsibilities:**
- Confirm platform access and testing workflows.
- Conduct controlled testing using the approved corpus and protocol.
- Record trial results, screenshots, and supporting evidence.
- Report limitations or testing problems promptly.

**Current status:** Awaiting confirmation and verified Week 10 production testing evidence.

### Henry Smith – Codec Verification

**Assigned responsibilities:**
- Support decoder verification during production testing.
- Analyze failures and recovered character sequences.
- Assist with testing scripts and reproducibility.
- Document results and provide supporting evidence.

**Current status:** Henry completed local codec verification and added a
production-trial validation tool. The full suite passes 38 tests and 132
subtests. Review of actual platform failures remains pending because the Week
10 raw sent/retrieved files have not yet been submitted.

## 4. Testing and Evidence

### Approved Testing Scope

The revised protocol authorizes seven platform-operation combinations:

1. Gmail – Send and retrieve message.
2. Discord – Send and retrieve message.
3. Microsoft Word – Save, reopen, and retrieve text.
4. Microsoft Outlook – Send and retrieve message.
5. Telegram Web – Send and retrieve message.
6. Notepad++ – Paste and copy back.
7. Browser Console – Paste and copy back.

The testing plan uses eight approved messages with three repetitions per message, producing 24 trials per combination and 168 planned production trials.

### Testing Evidence Status

The Week 9 preliminary WeChat feasibility tests demonstrated successful recovery in the two tested workflows. However, those preliminary findings are separate from the approved Week 10 production dataset.

**Week 10 production testing:** Pending verified logs, screenshots, and results.

Evidence will be added to this report as team members complete and submit their assigned testing.

Henry independently reproduced the preliminary WeChat baseline counts for
`WeChat test message` as 137 U+200B, 111 U+200C, and 30 U+200D, for a total of
278. The screenshots are internally consistent with those counts and report
exact recovery. The raw retrieved WeChat text was not committed, so this is an
evidence review rather than an independent post-platform decoder rerun.

## 5. Challenges and Lessons Learned

The main challenge is moving from a documented testing plan to consistent, reproducible testing across multiple platforms.

Previous weeks also demonstrated the importance of communication, clearly defined responsibilities, and supporting reported results with actual evidence.

To address these issues, we are prioritizing workflow verification, accurate recordkeeping, and regular communication before accepting production results.

## 6. Progress Against Semester Plan

Our semester plan originally targeted controlled survival-rate data collection beginning in Week 9.

Although preliminary testing and protocol development progressed, full production testing was delayed because platform workflows and access required further verification.

Week 10 is therefore focused on completing those outstanding checks and beginning controlled data collection.

The revised scope contains 168 planned trials. These remain planned rather than completed until evidence supports their completion.

## 7. Next Steps

- Obtain Tristan's confirmation of the approved platform workflows.
- Begin production testing once the required workflows are verified.
- Have Henry support decoder validation and failure analysis.
- Review incoming testing records against the data-quality audit.
- Update the team report with actual test results and screenshots.
- Conduct and document the Friday, October 23, team meeting.
- Ensure all individual journals, meeting minutes, and contributions are committed to GitHub.

## 8. Supporting Repository Documents

- `docs/week9_testing_protocol_draft.md`
- `docs/week10_data_quality_audit.md`
- `meeting_minutes/2026-10-19_week10.md`
- `weekly_journals/ifeanyi/week10.md`
- `tests/week9_testing/preliminary_feasibility_testing_WeChat.md`
- `docs/week10_henry_codec_validation.md`
- `tests/week10_testing/verify_henry_week10.py`
- `tests/week10_testing/validate_production_trials.py`
- `weekly_journals/henry/2026-10-22.md`

## 9. Report Status

**In Progress — Initial Week 10 report prepared.**

This report will be updated before submission to reflect verified production testing, actual team contributions, screenshots, Friday meeting minutes, and any changes to the project schedule.
