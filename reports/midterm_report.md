# CS481 — Team 1 Midterm Project Report

**Project:** Project 5 — Zero-Width Unicode Steganography with Social-Media Robustness Engineering  
**Period covered:** Project selection and planning through Week 8 (October 9, 2026)  
**Team:** Ifeanyi Emeka (Team Leader), Henry Smith, Tristan Koch  
**Repository:** https://github.com/bishop231101/Team-A-project

## 1. Executive Summary

This report synthesizes the team's work from the start of the semester through Week 8, rather than describing only the most recent week. The team selected Project 5, established its semester plan and GitHub workflow, built a working Python encoder/decoder for hiding UTF-8 messages with zero-width Unicode characters, tested transfers across applications, and developed repetition-based recovery for limited payload damage. By Week 8, the documented automated regression suite passed **28 tests and 132 subtests with no failures**. A local prototype demonstration and platform tests show both the system's capabilities and its limits. In particular, preserving the visible cover text does not guarantee that an application preserves the invisible payload.

## 2. Project Goal, Architecture, and Milestones Achieved

The goal is to embed a hidden message in ordinary visible text, recover it accurately, and measure how well the hidden data survives real-world application workflows. The prototype is written in Python, with its core implementation in `src/zero_width_codec.py`.

The codec maps binary `0` to U+200B (zero-width space), binary `1` to U+200C (zero-width non-joiner), and uses U+200D (zero-width joiner) for structure. A framed message contains the marker `ZWS1`, a four-byte payload length, the UTF-8 payload, and a CRC-32 checksum. The decoder checks framing, length, checksum, and UTF-8 validity before returning a secret; malformed input produces a `DecodeError`. The method conceals text but is **not encryption**. Further implementation details are documented in [`docs/week8_henry_architecture_and_codec.md`](../docs/week8_henry_architecture_and_codec.md) and [`docs/codec_format.md`](../docs/codec_format.md).

| Phase | Milestone achieved | Description and repository evidence |
|---|---|---|
| Initial setup / Week 2 | Project selected and planned | Selected Project 5, reviewed individual plans, adopted the team semester plan, assigned responsibilities, organized the repository, and began journals and meeting minutes. See [`docs/semester_plan.md`](../docs/semester_plan.md) and [`meeting_minutes/2026-08-28.md`](../meeting_minutes/2026-08-28.md). |
| Week 3 | Initial codec and baseline tests | Implemented the encoder/decoder, tested visible-cover preservation, and completed 6 automated tests plus 9 manual message tests. See [`reports/weekly_report_03.md`](weekly_report_03.md). |
| Week 4 | Initial platform robustness evaluation | Ran 27 transfer tests across Gmail, Discord, and Microsoft Word and recorded preservation and decode outcomes. See [`week4_testing/week4_results.md`](../week4_testing/week4_results.md). |
| Week 5 | Broader compatibility and corruption baseline | Ran 27 additional transfer tests across Outlook, Telegram Web, and Notepad++; ran four controlled corruption scenarios; resolved the `code` package naming conflict by using `src`. See [`reports/weekly_report_05.md`](weekly_report_05.md). |
| Week 6 | Repetition-based recovery | Implemented and tested improved repetition protection; six documented controlled recovery scenarios succeeded, contrasting with the Week 5 unprotected failures. See [`reports/weekly_report_06.md`](weekly_report_06.md). |
| Week 7 | Recovery boundary established | Demonstrated successful correction of one or two damaged symbols per five-copy group and failure at three damaged symbols; expanded tests explored higher corruption levels. See [`reports/weekly_report_07.md`](weekly_report_07.md). |
| Week 8 | Midterm validation and demonstration | Consolidated architecture and testing documentation, verified 28 automated tests and 132 subtests, ran five additional application workflows, and documented a reproducible local prototype demonstration. See [`reports/weekly_report_08.md`](weekly_report_08.md). |

## 3. Completed Subtasks and Detailed Testing Evidence

### 3.1 Codec implementation and baseline verification (Week 3)

Henry implemented the initial encoder/decoder and unit tests. Tristan tested nine representative messages (including numbers, spaces, punctuation, and longer content) and compared the decoded secrets with the originals. Ifeanyi reviewed and integrated contributions, resolved a `.gitignore` merge conflict, and reran the automated tests. **Results:** 6 automated tests passed; 9 manual cases passed; visible cover text remained unchanged. Evidence: [`week3_testing/week3_testing_results.md`](../week3_testing/week3_testing_results.md) and the screenshots in `week3_testing/screenshots/`.

### 3.2 Platform-transfer testing (Weeks 4–5)

For each platform test, the team encoded a known secret, moved the encoded text through the application-specific copy/paste or save/reopen workflow, retrieved the result, counted surviving codec characters, attempted decoding, and compared the recovered secret with the original. The Week 4 and Week 5 test sets used **nine messages per platform**.

| Period | Application | Tests | Successful decodes | Recorded result |
|---|---|---:|---:|---|
| Week 4 | Gmail | 9 | 0 | 42.11%–50.63% character survival; decode failed |
| Week 4 | Discord | 9 | 9 | 100% survival; decode succeeded |
| Week 4 | Microsoft Word | 9 | 0 | 42.11%–50.63% survival; decode failed |
| Week 5 | Microsoft Outlook | 9 | 9 | 100% survival; decode succeeded |
| Week 5 | Telegram Web | 9 | 9 | 100% survival; decode succeeded |
| Week 5 | Notepad++ | 9 | 9 | 100% survival; decode succeeded |

These are **workflow-specific observations**, not universal claims about each application. Evidence: [`week4_testing/week4_results.md`](../week4_testing/week4_results.md), [`week5_testing/week5_platform_testing_results.md`](../week5_testing/week5_platform_testing_results.md), and [`docs/tristan_week8_preliminary_results.md`](../docs/tristan_week8_preliminary_results.md). The Week 3 local baseline and the 54 Week 4–5 transfer trials together account for 63 documented manual test cases.

### 3.3 Baseline corruption and recovery development (Weeks 5–6)

Week 5 deliberately removed or altered zero-width characters to test whether the unprotected codec could recover the secret. All **four** documented scenarios failed to decode: approximately 30% removal, 50% removal, 30% alteration, and a mixed removal/alteration case. The alteration case was particularly instructive: a 100% character count did not mean the values were correct. Evidence: [`week5_testing/week5_recovery_testing_results.md`](../week5_testing/week5_recovery_testing_results.md).

In Week 6, Henry developed repetition-based recovery. A five-copy protected bit can be reconstructed by majority vote when no more than two symbols in its group are corrupted. Ifeanyi verified an intentional one-symbol corruption recovery, while Tristan tested six controlled removal, alteration, and mixed scenarios; all six documented scenarios recovered their secrets. The regression suite at this stage was recorded as **19 tests and 108 subtests passing**. Evidence: [`tests/week6_testing/week6_tristan_recovery_testing_results.md`](../tests/week6_testing/week6_tristan_recovery_testing_results.md), [`tests/week6_testing/week6_recovery_testing_results.md`](../tests/week6_testing/week6_recovery_testing_results.md), and Week 6 screenshots.

### 3.4 Recovery limits (Week 7)

The team tested the boundary of five-copy majority recovery. Ifeanyi's group-level tests succeeded with **1/5** and **2/5** symbols damaged, but failed at **3/5** damaged. Henry's controlled distributed-damage trials recovered through 40% and safely rejected 45% and 50% cases. Tristan's seven expanded scenarios had **four successful recoveries and three failures**, depending on corruption level and pattern. This is not a universal 40% recovery guarantee: concentrated damage can defeat one group even when the overall corruption percentage is lower. The Week 7 report recorded **25 tests and 118 subtests passing**. Evidence: [`tests/week7_testing/week7_ifeanyi_testing_results.md`](../tests/week7_testing/week7_ifeanyi_testing_results.md), [`tests/week7_testing/henry_week7_recovery_limit_results.md`](../tests/week7_testing/henry_week7_recovery_limit_results.md), and [`tests/week7_testing/week7_tristan_expanded_testing_results.md`](../tests/week7_testing/week7_tristan_expanded_testing_results.md).

**Figure 1 — Week 7 automated regression evidence.**

![Week 7 automated test screenshot](../tests/week7_testing/screenshots/ifeanyi/week7_baseline_tests.png)

**Figure 2 — Week 7 five-copy recovery boundary.** The test distinguishes recoverable one- and two-symbol group corruption from an unrecoverable three-symbol group.

![Week 7 corruption test screenshot](../tests/week7_testing/screenshots/ifeanyi/week7_corruption_tests.png)

### 3.5 Week 8 regression, platform comparison, and prototype

The team ran `python -m pytest -v` and documented **28 tests passed, 132 subtests passed, 0 failures**. This verifies the local automated test suite; it does **not** establish that all external platforms preserve hidden text.

**Figure 3 — Week 8 automated test results.**

![Week 8 automated tests](../tests/week8_testing/screenshots/henry/week8_automated_tests.png)

Week 8 also used one representative secret (`CS481-WEEK8`) per application, with 206 original codec characters. The results differed from some earlier workflows, including Discord; both results are retained because the procedures and testing periods differ.

| Week 8 application/workflow | Recovered characters | Survival rate | Secret decoded? |
|---|---:|---:|---|
| Windows Notepad | 206/206 | 100% | Yes |
| Browser Console | 206/206 | 100% | Yes |
| Gmail | 25/206 | 12.14% | No |
| Microsoft Word | 0/206 | 0% | No |
| Discord | 0/206 | 0% | No |

Evidence: [`docs/week8_midterm_testing.md`](../docs/week8_midterm_testing.md) and the screenshots in `tests/week8_testing/screenshots/ifeanyi/`.

**Figure 4 — Week 8 Discord decoding failure.** The decoder reported that no zero-width payload was found in the received message; this supports a failure for **this tested workflow**, rather than a universal statement about Discord.

![Discord decoding failure](../tests/week8_testing/screenshots/ifeanyi/discord_failure.png)

Henry also prepared a reproducible offline prototype demonstration with standard encoding/decoding, unchanged visible cover text, five-copy recovery under controlled 40% alteration, and safe rejection at 45% alteration. The documented command from the repository root is `python tests/week8_testing/run_henry_midterm_demo.py`.

**Figure 5 — Week 8 prototype demonstration.**

![Midterm prototype demonstration](../tests/week8_testing/screenshots/henry/week8_midterm_demo.png)

Evidence: [`docs/week8_prototype_demo.md`](../docs/week8_prototype_demo.md), [`tests/week8_testing/henry_midterm_demo_results.md`](../tests/week8_testing/henry_midterm_demo_results.md), and [`docs/week8_henry_architecture_and_codec.md`](../docs/week8_henry_architecture_and_codec.md).

## 4. Lessons Learned and Problems Encountered

1. **Correct local decoding is only the starting point.** Some applications preserve invisible symbols, while others strip or alter them; compatibility must be tested using an explicitly documented workflow.
2. **Survival rate is not equivalent to correct recovery.** A character may remain present but change value, and a decoder must reject invalid messages instead of returning incorrect plaintext.
3. **Redundancy helps within defined limits.** Five-copy majority voting can correct two damaged copies per group, but not three; it cannot recreate a payload that an application removes completely.
4. **Framing and checksums support trustworthy failure detection.** The `ZWS1` marker, length, CRC-32, and UTF-8 checks help reject malformed or damaged messages.
5. **Integration and repository organization matter.** The team resolved a Git merge conflict in Week 3 and a Python package naming conflict in Week 5, then verified the test suite after integration.
6. **Evidence must accompany conclusions.** Screenshots, test scripts, weekly journals, meeting minutes, and meaningful Git commits make each milestone independently reviewable.

## 5. Individual Team Contributions

**Ifeanyi Emeka — Team Leader / Integration and Compatibility Testing.** Organized the repository and semester plan; coordinated weekly responsibilities, meetings, reports, and GitHub pull-request integration; resolved the Week 3 merge conflict and Week 5 Python import/package issue; ran integration/regression checks; performed Week 5–8 compatibility and controlled recovery tests; and documented the Week 8 five-application results. Evidence: [`weekly_journals/ifeanyi/`](../weekly_journals/ifeanyi/), weekly reports, `tests/week7_testing/`, and `tests/week8_testing/screenshots/ifeanyi/`.

**Henry Smith — Codec and Recovery Development.** Developed the encoder/decoder and validation logic, expanded automated tests, implemented repetition-based recovery, investigated higher-corruption limits, documented the system architecture, and prepared the offline Week 8 demonstration. Evidence: [`weekly_journals/henry/`](../weekly_journals/henry/), [`docs/week8_henry_architecture_and_codec.md`](../docs/week8_henry_architecture_and_codec.md), and `tests/week8_testing/`.

**Tristan Koch — Platform Testing, Methodology, and Results Analysis.** Conducted the nine-message baseline and application tests, built controlled recovery-testing scripts, documented survival and decode outcomes, compared results across Weeks 3–8, prepared the compatibility matrix and preliminary findings, and contributed figures and testing evidence. Evidence: [`weekly_journals/tristan/`](../weekly_journals/tristan/), [`docs/tristan_week3-7_testing_review.md`](../docs/tristan_week3-7_testing_review.md), [`docs/tristan_week8_preliminary_results.md`](../docs/tristan_week8_preliminary_results.md), and platform testing folders.

Individual contribution grades should be checked against each person's **GitHub commit and pull-request history**, not this summary alone.

## 6. Progress Against the Semester Plan and Adjustments

The team achieved the main planned progression through the midterm: planning and repository setup; baseline codec development; application transfer testing; corruption baselines; improved recovery; recovery-limit analysis; and midterm documentation and demonstration. The original timeline and assigned work are in [`docs/semester_plan.md`](../docs/semester_plan.md).

The team made technical adjustments in response to evidence: the Python implementation was moved from the conflicting `code` package name to `src`; repetition-based protection was introduced after unprotected corruption failures; and the compatibility assessment was revised to distinguish application/workflow behavior from general platform support. The core semester objectives remained in place. The main remaining work is to improve robustness and coverage without overstating the present recovery capability, continue platform-specific testing, and prepare the later project deliverables.

## 7. Team Coordination and Repository Evidence

Team members maintained individual weekly journals and regular meeting records. Week 8 meetings occurred on **Monday, October 5** and **Friday, October 9**, with all three members recorded as attending. The Monday meeting assigned midterm responsibilities; the Friday meeting reviewed completed Week 8 work, documentation, and test progress. See [`meeting_minutes/2026-10-05_week8.md`](../meeting_minutes/2026-10-05_week8.md) and [`meeting_minutes/2026-10-09_week8.md`](../meeting_minutes/2026-10-09_week8.md).

The repository contains the implementation (`src/`), automated and controlled tests (`tests/` and week-specific testing folders), technical documentation (`docs/`), weekly reports (`reports/`), individual journals (`weekly_journals/`), and meeting records (`meeting_minutes/`). The GitHub commit and PR history provides attribution for the team's work.

## 8. Remaining Work and Conclusion

Following Week 8, the team will continue investigating platform-specific filtering, test additional representative workflows, refine the recovery method and its documentation, and prepare subsequent semester milestones, the final report, and the presentation/demo. The midterm evidence supports a functioning local zero-width steganography prototype with integrity checks and limited repetition-based recovery. It also identifies the central unresolved challenge: reliable transfer through applications that remove or alter invisible Unicode characters.

---

**Evidence note:** All numerical results and technical descriptions above are drawn from the team's repository reports and documentation. Platform findings are tied to their stated test workflows and periods. Image links are relative to this report's location in `reports/` and are intended to render in GitHub's Markdown viewer.
