# Week 13 Journal — Tristan Koch

## Weekly Focus

This week's focus was completing and reviewing the remaining project testing work, validating experimental results, and preparing for the final results analysis and documentation. I also worked on coordinating the Outlook testing results with the team so that the production-testing dataset could be finalized before generating the Week 13 charts and results documentation.

## Work Completed

- Completed the production-testing trials assigned to me across Gmail, Notepad++, Microsoft Word, Discord, and Telegram Web.
- Reviewed the results from the production-testing platforms and confirmed that the individual trial records and supporting evidence were available for analysis.
- Completed the Baseline-versus-Hamming comparative experiment, including the 120 individual trial records, summary, experiment report, and supporting validation.
- Reviewed the comparative experiment results to confirm that the summary statistics agreed with the individual trial records.
- Reviewed Henry's Outlook testing pull request and examined the submitted results and supporting documentation.
- Coordinated with the team regarding the Outlook results and whether the pull request should be merged before beginning final results consolidation.
- Began preparing the structure and requirements for the final production-testing statistics, chart datasets, and results documentation.
- Consolidated the restored Outlook SU02 records and verified that all three were included exactly once. SU02 R1 and R2 were exact recoveries with 100% retention, while SU02 R3 was a completed failed recovery with complete payload removal.
- Reran the Week 13 consolidation and regenerated the seven chart-ready CSV datasets from the individual production and comparative trial records.
- Verified the final production totals: 168 planned records, 165 completed trials, 3 Discord trials blocked before transfer, 112 exact recoveries, 53 failed recoveries, and a 67.88% completed-trial exact recovery rate.
- Verified the updated Outlook results as 19/24 exact recoveries with 90.27% aggregate character retention. I kept the three blocked Discord trials separate from failed recoveries.
- Revalidated the separate 120-record Baseline-versus-Hamming experiment: 36 successful recoveries, 84 detected failures, 0 undetected errors, 20% Baseline recovery, and 40% Hamming recovery.
- Completed the Week 13 results documentation in `docs/week13_results.md`, including platform analysis, comparative-experiment findings, Hamming overhead, and explanations and takeaways for the five charts.
- Reviewed the chart-ready data and written interpretations to confirm that the percentages, counts, blocked-trial handling, and production/comparative separation were consistent.
- Saved all five chart PNG files alongside the chart-ready CSV datasets in `tests/week13_testing/chart_data/` and inserted them into `docs/week13_results.md`. Reviewed their placement, rendering, labels, and readability.

## What I Learned

- Production-platform behavior can vary significantly. Some platforms preserve zero-width characters and allow exact recovery, while others remove some or all of the encoded payload.
- Character retention and exact message recovery are related but are not interchangeable measurements. Retaining some zero-width characters does not necessarily mean that the hidden message can be successfully decoded.
- Blocked trials must be distinguished from completed trials that result in unsuccessful recovery. This is important when calculating accurate recovery rates.
- The comparative experiment demonstrated the benefits and limitations of Hamming error correction. Hamming successfully corrected the tested single-bit errors, but it did not recover successfully under the tested double-bit corruption or deletion conditions.
- Error correction introduces additional encoded-length overhead, which must be considered when evaluating the trade-offs of the encoding methods.
- Independent review and validation of trial records are important for ensuring that the final statistics and documentation accurately represent the experimental results.

## Problems and Challenges

- Outlook testing produced inconsistent results during my initial testing. Some messages were successfully recovered, while others appeared to lose the entire zero-width payload despite the same testing procedure.
- Henry independently performed Outlook testing and submitted a separate set of results. His results differed from some of my initial observations, so the team's authoritative records needed to be reviewed before final consolidation.
- Coordinating the final Outlook pull request review and merge took additional time while Ifeanyi was attending training.
- The volume of individual trial records, JSON analysis files, screenshots, and supporting documentation made final verification and organization an important part of this week's work.
- Preparing the final charts requires consolidating the production-platform results separately from the Baseline-versus-Hamming comparative experiment to avoid mixing different experimental conditions.

## Next Steps

- Perform a final review of the Week 13 documentation, CSV datasets, chart images, and weekly journal before submission.
- Stage and commit the completed Week 13 results-consolidation and documentation changes.
- Push the updated branch and open or update the pull request for team review.
- Address any feedback or requested corrections from the team before final submission.
