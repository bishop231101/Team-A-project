# Tristan Week 3-7 Testing Review

## 1. Purpose and Scope

This document consolidates existing Week 3-7 testing evidence for Tristan's Week 8 Midterm Report preparation. It is a personal working analysis for testing methodology, preliminary results, compatibility-matrix updates, potential charts, and evidence organization. It does not replace `docs/week8_midterm_testing.md`.

Scope reviewed:

- `week3_testing/`
- `week4_testing/`
- `week5_testing/`
- `tests/week6_testing/`
- `tests/week7_testing/`

This review only records documented repository facts, direct calculations from documented values, and clearly labeled observations or inferences. It does not invent missing platform or recovery results.

## 2. Platform Testing Summary

### Week 3: Local Python Environment

Source: `week3_testing/week3_testing_results.md`

Week 3 tested the zero-width codec in a local Python environment on branch `henry/week3-zero-width-codec`, using Python 3.14.5 and cover text `Visible cover text.`.

| Platform | Tests | Passed | Failed | Overall outcome | Notes |
|---|---:|---:|---:|---|---|
| Local Python environment | 9 | 9 | 0 | PASS | All decoded messages matched the originals and the cover text remained unchanged. |

The Week 3 test messages covered basic text, course/team identifiers, spaces, numbers, a longer message, multiple consecutive spaces, special characters, and mixed content.

Important observation: Test 6 lists the original message as `This is a longer test message for Week 3.` but the decoded message as `This is a longer test message for Week 3` without the period, while the result is marked PASS. This should be verified before using the row as evidence of exact matching.

### Week 4: Gmail, Discord, Microsoft Word

Sources: `week4_testing/week4_results.md`, `week4_testing/week4_testing_procedure`

Week 4 reused the nine Week 3 messages and transferred encoded payloads through Gmail, Discord, and Microsoft Word. The procedure counted zero-width characters sent and recovered, calculated survival rate, decoded the recovered payload, and compared the decoded result with the original.

| Platform | Tests | Successful decodes | Failed decodes | Average survival rate | Overall result |
|---|---:|---:|---:|---:|---|
| Gmail | 9 | 0 | 9 | 45.08% | FAIL |
| Discord | 9 | 9 | 0 | 100.00% | PASS |
| Microsoft Word | 9 | 0 | 9 | 45.08% | FAIL |

Gmail survival rates ranged from 42.11% to 50.63%. Each Gmail test failed with an incomplete or malformed byte block error.

Discord preserved all zero-width characters in all nine tests. Every Discord payload decoded successfully and matched the original message.

Microsoft Word survival rates ranged from 42.11% to 50.63%. Each Microsoft Word test failed with an incomplete or malformed byte block error after the save, close, reopen, and copy workflow.

Week 4 total: 27 platform tests; 9 successful decodes and 18 failed decodes.

### Week 5: Microsoft Outlook, Telegram Web, Notepad++

Source: `week5_testing/week5_platform_testing_results.md`

Week 5 tested three additional platforms using the same nine messages and comparable methodology.

| Platform | Tests | Successful decodes | Failed decodes | Average survival rate | Overall result |
|---|---:|---:|---:|---:|---|
| Microsoft Outlook | 9 | 9 | 0 | 100.00% | PASS |
| Telegram Web | 9 | 9 | 0 | 100.00% | PASS |
| Notepad++ | 9 | 9 | 0 | 100.00% | PASS |

Week 5 total: 27 platform tests; 27 successful decodes and 0 failed decodes. The document states that no zero-width characters were lost or corrupted during the Week 5 platform tests.

### Platform Coverage Across Weeks 3-5

Documented platforms tested:

- Local Python environment
- Gmail
- Discord
- Microsoft Word
- Microsoft Outlook
- Telegram Web
- Notepad++

Calculated from documented summaries: Weeks 4-5 include 54 cross-platform transfer tests, with 36 successful decodes and 18 failed decodes. Including Week 3 local tests, the documented Week 3-5 platform/local total is 63 tests, with 45 passing and 18 failing. This calculation depends on treating Week 3 local codec tests as platform/local tests rather than transfer-platform tests.

Limitations:

- Week 4 and Week 5 tested different platforms, so platform results are not repeated across weeks.
- Gmail and Microsoft Word had similar documented survival counts and the same 45.08% average survival rate, but the repository does not explain whether the same preservation behavior was independently observed or copied into both result sets.
- The exact platform versions, browser versions, account settings, and document/email formatting settings are not consistently documented.

## 3. Recovery/Corruption Testing Summary

### Week 5 Baseline Recovery Tests

Source: `week5_testing/week5_recovery_testing_results.md`

Week 5 tested the original codec under intentional zero-width removal and alteration. All four scenarios failed to decode.

| Test | Corruption type | Corruption percentage | Message/test identifier | Original ZW count | Remaining/recovered ZW count | Removed count | Altered count | Survival rate | Decode result | Recovered message or error |
|---:|---|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | Removal | Approx. 30% | `Hello` | 152 | 105 | 47 | 0 | 69.08% | FAILED | `DecodeError: payload contains an incomplete or malformed byte block` |
| 2 | Removal | 50% | `Zero Width Test` | 242 | 121 | 121 | 0 | 50.00% | FAILED | `DecodeError: payload contains an incomplete or malformed byte block` |
| 3 | Alteration | Approx. 30% | `CS481 Test 123!` | 242 | 242 | 0 | 74 | 100.00% | FAILED | `DecodeError: payload contains an incomplete or malformed byte block` |
| 4 | Combined removal and alteration | Approx. 20% removal + approx. 20% alteration | `This is a longer test message for Week 3.` | 476 | 380 | 96 | 76 | 79.83% | FAILED | `DecodeError: payload contains an incomplete or malformed byte block` |

Documented observation: visible cover text remained unchanged across all four scenarios, but the hidden payloads could not be decoded.

### Week 6 Recovery Tests

Sources: `tests/week6_testing/week6_tristan_recovery_testing_results.md`, `tests/week6_testing/week6_recovery_testing_results.md`, `tests/week6_testing/henry_week6_recovery_results.md`

Week 6 introduced/use-tested a recovery-enabled codec with five-copy repetition and majority voting. Tristan's six controlled scenarios all passed.

| Test | Corruption type | Corruption percentage | Message/test identifier | Original ZW count | Remaining/recovered ZW count | Removed count | Altered count | Survival rate | Decode result | Recovered message or error |
|---:|---|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | Removal | 10.00% of recoverable data symbols | `Hello` | 820 | 752 | 68 | 0 | 91.71% | PASS | `Hello` |
| 2 | Removal | 20.00% of recoverable data symbols | `Zero Width Test` | 1,300 | 1,084 | 216 | 0 | 83.38% | PASS | `Zero Width Test` |
| 3 | Removal | 30.00% of recoverable data symbols | `CS481 Test 123!` | 1,300 | 976 | 324 | 0 | 75.08% | PASS | `CS481 Test 123!` |
| 4 | Alteration | 10.00% of recoverable data symbols | `This is a longer test message for Week 3.` | 2,548 | 2,548 | 0 | 212 | 100.00% | PASS | `This is a longer test message for Week 3.` |
| 5 | Alteration | 20.00% of recoverable data symbols | `Team A` | 868 | 868 | 0 | 144 | 100.00% | PASS | `Team A` |
| 6 | Mixed removal and alteration | 30.00% of recoverable data symbols | `CS481` | 820 | 718 | 102 | 102 | 87.56% | PASS | `CS481` |

Additional Week 6 evidence:

- `tests/week6_testing/week6_recovery_testing_results.md` records a baseline automated test run with 19 tests passed, 108 subtests passed, no failures, and 0.15 seconds execution time.
- The same file records a repetition recovery test where one zero-width symbol in a repeated bit group was intentionally changed and the secret `Week 6 recovery test` was successfully recovered.
- `tests/week6_testing/henry_week6_recovery_results.md` states that configurable odd repetition factors from 3 through 15 were supported, with Week 6 using five copies. It records PASS results for 10%, 20%, and 30% data-symbol removal; 10%, 20%, and 30% alteration; and 30% mixed removal/alteration.
- Henry's Week 6 document states that the automated suite screenshot shows 25 tests and 118 subtests passed. This differs from the 19-test/108-subtest baseline recorded in `week6_recovery_testing_results.md`.

### Week 7 Expanded and Limit Recovery Tests

Sources: `tests/week7_testing/week7_tristan_expanded_testing_results.md`, `tests/week7_testing/henry_week7_recovery_limit_results.md`, `tests/week7_testing/week7_ifeanyi_testing_results.md`

Week 7 expanded controlled corruption levels for the five-copy recovery method. Tristan's seven scenarios produced four passes and three failures.

| Test | Corruption type | Corruption percentage | Message/test identifier | Original ZW count | Remaining/recovered ZW count | Removed count | Altered count | Survival rate | Decode result | Recovered message or error |
|---:|---|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | Removal | 40.00% of recoverable data symbols | `Hello` | 820 | 548 | 272 | 0 | 66.83% | PASS | `Hello` |
| 2 | Removal | 50.00% of recoverable data symbols | `Zero Width Test` | 1,300 | 760 | 540 | 0 | 58.46% | FAIL | `recovery payload contains a missing or malformed bit group` |
| 3 | Removal | 60.00% of recoverable data symbols | `CS481 Test 123!` | 1,300 | 652 | 648 | 0 | 50.15% | FAIL | `recovery payload contains a missing or malformed bit group` |
| 4 | Alteration | 30.00% of recoverable data symbols | `This is a longer test message for Week 3.` | 2,548 | 2,548 | 0 | 636 | 100.00% | PASS | `This is a longer test message for Week 3.` |
| 5 | Alteration | 40.00% of recoverable data symbols | `Team A` | 868 | 868 | 0 | 288 | 100.00% | PASS | `Team A` |
| 6 | Alteration | 50.00% of recoverable data symbols | `CS481` | 820 | 820 | 0 | 340 | 100.00% | FAIL | `payload has an unrecognized format marker` |
| 7 | Mixed removal and alteration | 40.00% of recoverable data symbols | `CS481` | 820 | 684 | 136 | 136 | 83.41% | PASS | `CS481` |

Henry's Week 7 recovery-limit results record a controlled boundary analysis:

| Corruption type | Damage | Zero-width survival | Expected | Actual | Status |
|---|---:|---:|---|---|---|
| Removal | 35% | 70.90% | Recovered | Recovered | PASS |
| Removal | 40% | 66.74% | Recovered | Recovered | PASS |
| Removal | 45% | 62.58% | Rejected | Rejected | PASS |
| Removal | 50% | 58.42% | Rejected | Rejected | PASS |
| Alteration | 35% | 100.00% | Recovered | Recovered | PASS |
| Alteration | 40% | 100.00% | Recovered | Recovered | PASS |
| Alteration | 45% | 100.00% | Rejected | Rejected | PASS |
| Alteration | 50% | 100.00% | Rejected | Rejected | PASS |
| Mixed | 35% | 85.45% | Recovered | Recovered | PASS |
| Mixed | 40% | 83.37% | Recovered | Recovered | PASS |
| Mixed | 45% | 81.29% | Rejected | Rejected | PASS |
| Mixed | 50% | 79.21% | Rejected | Rejected | PASS |

Ifeanyi's Week 7 corruption testing records the group-level recovery limit:

- 1/5 symbols corrupted per group: PASS; original secret successfully recovered.
- 2/5 symbols corrupted per group: PASS; original secret successfully recovered.
- 3/5 symbols corrupted per group: FAIL; decoder could not recover the original secret.

Week 7 automated-test evidence is inconsistent across documents:

- `tests/week7_testing/week7_ifeanyi_testing_results.md` records 25 tests passed and 118 subtests passed in 0.18 seconds.
- `tests/week7_testing/henry_week7_recovery_limit_results.md` says its screenshot shows 28 tests and 132 subtests passed.

## 4. Week 5-7 Progression

Week 5 baseline behavior: the original codec failed under all four documented recovery/corruption scenarios. It failed after approximately 30% removal, 50% removal, approximately 30% alteration, and combined approximately 20% removal plus approximately 20% alteration. The baseline also showed that a 100.00% zero-width survival rate does not guarantee successful decoding, because the approximately 30% alteration test preserved all zero-width characters but still failed.

Week 6 introduced and tested five-copy repetition/recovery. The Week 6 documents describe five-copy repetition with majority voting, where each bit is repeated five times and the decoder can recover when enough symbols in a repeated group remain correct. Tristan's Week 6 tests preserved structural separator characters and distributed corruption across recoverable data-symbol groups. All six Week 6 scenarios passed: 10%, 20%, and 30% removal; 10% and 20% alteration; and 30% mixed removal/alteration.

Week 7 increased corruption levels. Tristan's Week 7 tests show recovery still succeeding at 40% removal, 30% alteration, 40% alteration, and 40% mixed removal/alteration. Recovery failed at 50% removal, 60% removal, and 50% alteration. Henry's Week 7 boundary analysis records recovery at 35% and 40% distributed damage, and rejection at 45% and 50% distributed damage for removal, alteration, and mixed scenarios.

Point where recovery begins to fail: documented Week 7 evidence places the controlled distributed-damage boundary at 40% recovered/rejected behavior for five-copy majority voting, with 45% and 50% rejected in Henry's boundary tests. Tristan's expanded tests show the first removal failure at 50% and the first alteration failure at 50%, while 40% removal/alteration/mixed scenarios still passed.

Removal vs. alteration vs. mixed corruption:

- Removal reduces the zero-width character count and lowers survival rate.
- Alteration can leave the zero-width character count unchanged, so survival rate can remain 100.00% even when decoding fails.
- Mixed corruption can have a higher survival rate than removal-only tests because only part of the damage removes characters; the rest alters existing characters.
- The documented recovery result depends on data-symbol damage distribution and whether repeated groups exceed the five-copy majority-vote correction capacity.

Observation/inference: the five-copy approach clearly improved controlled recovery compared with Week 5 baseline tests, but the repository evidence supports only the controlled scenarios that preserved structural separators and distributed damage. It does not prove universal robustness against arbitrary platform transformations, separator deletion, prefix damage, concentrated corruption, or complete zero-width stripping.

## 5. Important Statistics

Platform/local testing:

- Week 3 local Python environment: 9 total tests; 9 passed; 0 failed.
- Week 4 platform testing: 27 total tests; 9 successful decodes; 18 failed decodes.
- Week 4 Gmail: 9 tests; 0/9 successful decodes; survival range 42.11%-50.63%; average survival rate 45.08%.
- Week 4 Discord: 9 tests; 9/9 successful decodes; average survival rate 100.00%.
- Week 4 Microsoft Word: 9 tests; 0/9 successful decodes; survival range 42.11%-50.63%; average survival rate 45.08%.
- Week 5 platform testing: 27 total tests; 27 successful decodes; 0 failed decodes.
- Week 5 Microsoft Outlook, Telegram Web, and Notepad++ each had 9/9 successful decodes and 100.00% average survival.
- Calculated from documented Week 4-5 platform summaries: 54 cross-platform transfer tests; 36 successful decodes; 18 failed decodes.

Recovery/corruption testing:

- Week 5 recovery baseline: 4 scenarios; 0 passed; 4 failed.
- Week 5 failed at 69.08% survival for approximately 30% removal of `Hello`.
- Week 5 failed at 50.00% survival for 50% removal of `Zero Width Test`.
- Week 5 failed at 100.00% survival for approximately 30% alteration of `CS481 Test 123!`.
- Week 5 failed at 79.83% survival for combined approximately 20% removal plus approximately 20% alteration of the longer Week 3 message.
- Week 6 Tristan recovery: 6 scenarios; 6 passed; 0 failed.
- Week 6 removal passes: 10% removal at 91.71% survival, 20% removal at 83.38%, 30% removal at 75.08%.
- Week 6 alteration passes: 10% and 20% alteration, both with 100.00% survival.
- Week 6 mixed pass: 30% mixed removal/alteration at 87.56% survival.
- Week 7 Tristan expanded recovery: 7 scenarios; 4 passed; 3 failed.
- Week 7 removal: 40% passed at 66.83% survival; 50% failed at 58.46%; 60% failed at 50.15%.
- Week 7 alteration: 30% passed at 100.00% survival; 40% passed at 100.00%; 50% failed at 100.00%.
- Week 7 mixed: 40% mixed removal/alteration passed at 83.41% survival.
- Week 7 Henry boundary analysis: 12 scenarios; all actual outcomes matched expected outcomes. Recovery at 35% and 40%; rejection at 45% and 50% for removal, alteration, and mixed damage.
- Week 7 Ifeanyi group-level test: 1/5 and 2/5 corrupted symbols per group recovered; 3/5 failed.

Automated-test statistics:

- Week 6 `week6_recovery_testing_results.md`: 19 tests passed, 108 subtests passed, no failures, 0.15 seconds.
- Week 6 Henry document screenshot description: 25 tests and 118 subtests passed.
- Week 7 Ifeanyi document: 25 tests passed, 118 subtests passed, no failures, 0.18 seconds.
- Week 7 Henry document screenshot description: 28 tests and 132 subtests passed.

These automated-test counts should be treated as documented but inconsistent unless the corresponding screenshots or test history are verified.

## 6. Potential Charts and Figures

1. Platform compatibility matrix
   - Shows: platform, total tests, successful decodes, failed decodes, average survival rate, overall result.
   - Supported by: `week4_testing/week4_results.md`, `week5_testing/week5_platform_testing_results.md`, and optionally `week3_testing/week3_testing_results.md` for local baseline.
   - Variables/categories: platform vs. pass/fail counts and survival rate.
   - Usefulness: strong Midterm Report summary of which platforms preserved zero-width payloads.

2. Average survival rate by platform
   - Shows: Gmail, Discord, Microsoft Word, Outlook, Telegram Web, Notepad++ survival averages.
   - Supported by: Week 4 and Week 5 platform summary tables.
   - Variables/categories: platform on x-axis; average survival rate on y-axis.
   - Usefulness: visually separates full-preservation platforms from partial-stripping platforms.

3. Decode success by platform
   - Shows: successful and failed decode counts per platform.
   - Supported by: Week 4 and Week 5 platform summary tables.
   - Variables/categories: platform categories; pass/fail count bars.
   - Usefulness: makes clear that survival percentage and decode success are related but should be reported separately.

4. Week 5 vs. Week 6 vs. Week 7 recovery outcome timeline
   - Shows: progression from all Week 5 recovery failures to all Week 6 Tristan passes to mixed Week 7 pass/fail outcomes.
   - Supported by: Week 5 recovery results, Week 6 Tristan results, Week 7 Tristan results.
   - Variables/categories: week and scenario type; result status.
   - Usefulness: supports the preliminary-results narrative about the improvement introduced by five-copy recovery and the later boundary testing.

5. Recovery success/failure by corruption percentage
   - Shows: pass/fail status across removal, alteration, and mixed scenarios at documented percentages.
   - Supported by: Week 6 Tristan results, Week 7 Tristan results, Henry Week 7 boundary table.
   - Variables/categories: corruption percentage on x-axis; success/failure or recovered/rejected status as marker/color; series for removal/alteration/mixed.
   - Usefulness: helps identify the tested recovery threshold without overstating robustness.

6. Survival rate vs. corruption level
   - Shows: how survival rate changes under removal, alteration, and mixed corruption.
   - Supported by: Week 5 recovery summary, Week 6 Tristan table, Week 7 Tristan table, Henry Week 7 table.
   - Variables/categories: corruption percentage on x-axis; zero-width survival rate on y-axis; corruption type as series.
   - Usefulness: demonstrates that alteration can keep survival at 100.00% while still causing decode failure.

7. Recovery threshold/failure-point figure
   - Shows: five-copy majority voting succeeds when up to two of five symbols per group are corrupted and fails when three of five are corrupted.
   - Supported by: `tests/week7_testing/week7_ifeanyi_testing_results.md` and `tests/week7_testing/henry_week7_recovery_limit_results.md`.
   - Variables/categories: corrupted symbols per five-copy group or distributed damage percentage; recovered/rejected outcome.
   - Usefulness: explains the technical reason for the observed boundary in a concise visual.

8. Evidence map/table
   - Shows: each major result with source Markdown path and screenshot folder.
   - Supported by: all reviewed result files and screenshot paths.
   - Variables/categories: week, evidence type, path, result summary.
   - Usefulness: helps organize report appendix/evidence references.

## 7. Data Quality and Items to Verify

- Week 3 Test 6 marks PASS even though the decoded message omits the final period shown in the original message.
- Week 4 Gmail and Microsoft Word have identical per-test survival counts and averages. This may be accurate, but it should be manually verified because two different platforms showing identical counts is notable.
- Week 4 Gmail Test 5 error text says `payload contains incomplete or malformed byte block`, while most other rows say `payload contains an incomplete or malformed byte block`. This is terminology inconsistency, not necessarily a data issue.
- Week 4 file path `week4_testing/screenshots/gmail/test_02_compose.png.png` has a duplicated `.png` extension.
- Week 5 recovery uses "survival rate" for character count retained, but alteration scenarios can preserve 100.00% of zero-width characters while corrupting payload meaning. The Midterm Report should distinguish survival from decode success.
- Week 6 automated-test counts differ by document: 19 tests/108 subtests in `week6_recovery_testing_results.md` versus 25 tests/118 subtests in Henry's Week 6 document.
- Week 7 automated-test counts differ by document: 25 tests/118 subtests in Ifeanyi's Week 7 document versus 28 tests/132 subtests in Henry's Week 7 document.
- Week 6 Tristan results list six controlled scenarios, while Henry's Week 6 controlled table includes seven scenarios because it includes 30% alteration in addition to Tristan's 10% and 20% alteration scenarios.
- Week 7 Tristan and Henry survival rates for similar 40%/50% scenarios are close but not always identical, likely due to different messages or scenario scripts. Do not merge them without noting source differences.
- Platform versions, browser versions, and exact platform workflows are not consistently documented.
- Recovery tests generally preserve structural separators and use controlled/distributed corruption. The Midterm Report should avoid implying the same results apply to uncontrolled real-world platform transformations.
- Screenshots are referenced as evidence, but this review did not visually inspect each screenshot's contents.

## 8. Midterm Report Evidence Candidates

Testing methodology:

- `week4_testing/week4_testing_procedure`
- `week4_testing/week4_results.md`
- `week5_testing/week5_platform_testing_results.md`
- `week5_testing/week5_recovery_testing_results.md`
- `tests/week6_testing/week6_tristan_recovery_testing_results.md`
- `tests/week7_testing/week7_tristan_expanded_testing_results.md`

Platform testing results:

- `week3_testing/week3_testing_results.md`
- `week4_testing/week4_results.md`
- `week5_testing/week5_platform_testing_results.md`

Recovery/corruption baseline:

- `week5_testing/week5_recovery_testing_results.md`
- `week5_testing/screenshots/recovery/Test1_result.png`
- `week5_testing/screenshots/recovery/Test2_result.png`
- `week5_testing/screenshots/recovery/Test3_result.png`
- `week5_testing/screenshots/recovery/Test4_result.png`

Five-copy recovery evidence:

- `tests/week6_testing/week6_tristan_recovery_testing_results.md`
- `tests/week6_testing/henry_week6_recovery_results.md`
- `tests/week6_testing/week6_recovery_testing_results.md`
- `tests/week6_testing/run_tristan_recovery_tests.py`
- `tests/week6_testing/run_henry_recovery_demo.py`
- `tests/week6_testing/screenshots/tristan/Test1.png` through `tests/week6_testing/screenshots/tristan/Test6.png`
- `tests/week6_testing/screenshots/henry/week6_recovery_scenarios.png`
- `tests/week6_testing/screenshots/week6_recovery_test.png`

Higher-corruption and failure cases:

- `tests/week7_testing/week7_tristan_expanded_testing_results.md`
- `tests/week7_testing/henry_week7_recovery_limit_results.md`
- `tests/week7_testing/week7_ifeanyi_testing_results.md`
- `tests/week7_testing/run_tristan_expanded_recovery_tests.py`
- `tests/week7_testing/run_henry_recovery_limit_tests.py`
- `tests/week7_testing/run_ifeanyi_week7_corruption_tests.py`
- `tests/week7_testing/screenshots/tristan/Week7_Test1.png` through `tests/week7_testing/screenshots/tristan/Week7_Test7.png`
- `tests/week7_testing/screenshots/henry/week7_recovery_limits.png`
- `tests/week7_testing/screenshots/ifeanyi/week7_corruption_tests.png`

Compatibility/survival screenshot evidence:

- `week3_testing/screenshots/`
- `week4_testing/screenshots/gmail/`
- `week4_testing/screenshots/discord/`
- `week4_testing/screenshots/microsoft word/`
- `week5_testing/screenshots/outlook/`
- `week5_testing/screenshots/telegram/`
- `week5_testing/screenshots/notepad++/`

Useful statistics/tables:

- Week 4 Overall Platform Comparison table in `week4_testing/week4_results.md`
- Week 5 Overall Platform Comparison table in `week5_testing/week5_platform_testing_results.md`
- Week 5 Recovery Testing Summary table in `week5_testing/week5_recovery_testing_results.md`
- Week 6 Results table in `tests/week6_testing/week6_tristan_recovery_testing_results.md`
- Week 7 Results table in `tests/week7_testing/week7_tristan_expanded_testing_results.md`
- Week 7 boundary table in `tests/week7_testing/henry_week7_recovery_limit_results.md`

## 9. Key Takeaways for Week 8

- Week 3 establishes a local codec baseline with 9/9 documented passes, but Test 6 should be checked because the decoded text appears to omit punctuation.
- Week 4 shows platform compatibility is uneven: Discord preserved and decoded all payloads, while Gmail and Microsoft Word preserved only about 45.08% on average and failed every decode.
- Week 5 platform testing expands compatibility evidence with Outlook, Telegram Web, and Notepad++ all passing 9/9 tests at 100.00% survival.
- Week 5 recovery testing is the baseline for corruption behavior: the original codec failed every documented recovery scenario.
- Week 6 provides the strongest evidence of improvement from five-copy repetition/recovery: Tristan's six controlled scenarios all recovered successfully.
- Week 7 identifies the controlled recovery boundary more clearly: recovery succeeded through documented 40% distributed damage but failed or was rejected at higher levels such as 45%, 50%, and 60%, depending on the source scenario.
- Survival rate must be reported separately from decode success. Alteration tests can have 100.00% survival while still failing to decode.
- The Midterm Report should describe the recovery results as controlled evidence, not universal robustness. The tests preserve structural separators and distribute corruption; they do not cover all real-world platform damage patterns.
- Before using final numbers, manually verify the punctuation issue, identical Gmail/Word survival values, automated-test count discrepancies, and screenshot evidence for the most important claims.
