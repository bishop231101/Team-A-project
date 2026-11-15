# Week 13 Individual Journal — Ifeanyi Emeka

**Course:** CS481 Capstone Project  
**Week:** 13 (November 9–15, 2026)  
**Role:** Team Leader  
**Project:** Zero-Width Unicode Steganography

## 1. Weekly Objectives

My main responsibility this week is to coordinate the team's progress toward completing the compatibility matrix, final experimental statistics, reproducibility documentation, and code-quality improvements. I am also responsible for reviewing contributions, verifying results, integrating approved work, and preparing the Week 13 progress report.

## 2. Work Completed

### Monday Team Meeting — November 9

I conducted our Monday team meeting with Henry Smith and Tristan Koch. All three team members were present.

We reviewed our Week 12 accomplishments, discussed outstanding tasks, and established responsibilities for Week 13 based on our semester project plan.

Our main priorities are:

- **Henry:** Review code quality, improve diagnostics, document technical limitations, and complete relevant testing.
- **Tristan:** Finalize experimental statistics, charts, and reproducibility documentation.
- **Ifeanyi:** Prepare and verify the compatibility matrix, review team contributions, coordinate integration, and maintain the weekly report.

We also agreed to continue addressing any outstanding tasks from previous weeks.

### Compatibility Matrix Development

I created `docs/week13_compatibility_matrix.md` to document how the steganography system performed across the tested applications.

Rather than relying only on previously reported results, I used PowerShell to examine the original production-testing JSON records in our repository.

I located and analyzed 72 records, consisting of 24 trials each for Gmail, Microsoft Word, and Notepad++.

The analysis confirmed the following:

| Platform | Trials | Exact Recoveries | Average Retention |
|---|---:|---:|---:|
| Gmail | 24 | 0 | 23.87% |
| Microsoft Word | 24 | 0 | 0% |
| Notepad++ | 24 | 24 | 100% |

All 72 records had a completed analysis status.

These findings showed that Notepad++ preserved the encoded zero-width characters and supported exact recovery in every recorded trial. Gmail retained some characters but did not achieve exact recovery, while Microsoft Word did not retain the encoded characters under the tested conditions.

I documented these findings in the compatibility matrix, including the limitations of the testing procedures.

### Verification Evidence and Report Updates

I captured the PowerShell verification results and saved the screenshot in:

`docs/evidence/week13_compatibility_verification.png`

I also updated `reports/weekly_report_13.md` with the verified statistics, a results table, the screenshot, and an explanation of the findings.

To confirm the evidence was properly included, I opened the report in Markdown Preview and verified that the screenshot displayed correctly.

After reviewing the changes, I committed and pushed the compatibility matrix, verification evidence, and updated report to GitHub. I confirmed that my local `main` branch was synchronized with `origin/main` and that the working tree was clean.

## 3. Testing and Verification

My main testing contribution this week has been independently summarizing the existing production-testing records.

I used PowerShell to extract each record's exact-recovery result, character-retention percentage, and analysis status. I then grouped the records by application to calculate successful recoveries and average retention.

This provided an additional verification of the reported compatibility statistics without modifying or regenerating the original experimental records.

The results are documented in the compatibility matrix and supported by the screenshot embedded in the Week 13 report.

## 4. Challenges and Lessons Learned

One challenge was making sure that the compatibility matrix accurately represented the original testing data rather than relying on assumptions.

I addressed this by inspecting the JSON record structure and using a PowerShell script to summarize the results across all 72 files.

I also learned the importance of verifying that screenshots are correctly linked in Markdown documents. Saving an image in the repository is not enough; it must also display properly in the report so that the evidence can be reviewed.

This week's work reinforced the importance of reproducibility, accurate documentation, and careful verification before presenting technical results.

## 5. Team Leadership and Coordination

As team leader, I continued monitoring progress against our semester plan and maintaining clear responsibilities.

I coordinated the Week 13 assignments, documented our Monday meeting, and prepared the report structure so that completed contributions can be incorporated as they become available.

My focus is to ensure that the team's work is technically supported, properly documented, and integrated without introducing unnecessary changes to previously verified results.

## 6. Progress Against the Semester Plan

Week 13 objectives were completed through the combined efforts of all three team members.

I prepared and independently verified the initial compatibility matrix using 72 production-testing records. Henry completed the remaining Microsoft Outlook testing, added supporting evidence, and contributed code-quality improvements. Tristan finalized the experimental statistics, charts, consolidated datasets, and reproducibility documentation.

The final production-testing results included **168 planned trials, 165 completed trials, 3 blocked trials, and 112 exact recoveries**, representing a 67.88% recovery rate among completed trials.

The comparative experiment contained 120 records, including 36 successful recoveries, 84 detected failures, and no undetected errors.

After the team's contributions were integrated, I ran the regression test suite and confirmed that all 83 tests and 546 subtests passed.

These accomplishments satisfied the main Week 13 objectives and prepared the project for the next phase of development.

## 7. Final Integration and Verification

Following our Friday, November 13 meeting, which all three team members attended, I reviewed the completed Week 13 contributions.

Henry completed the remaining Microsoft Outlook testing, documented the results and supporting evidence, and contributed code-quality improvements. One Outlook trial experienced a delivery failure, which was documented separately from codec failures because the exact cause could not be confirmed.

Tristan completed the final statistics, consolidated CSV files, five charts, and reproducibility documentation. He also updated the compatibility matrix, results documentation, and weekly progress report.

After the team's pull requests were merged, I synchronized the repository and ran the complete regression test suite using `python -m pytest -q`.

**Final regression results:**
- 83 tests passed.
- 546 subtests passed.
- Execution time: 4.70 seconds.
- No test failures reported.

I also prepared Friday's meeting minutes and updated the weekly progress report to reflect the team's completed work.

## 8. Team Leadership and Final Submission Preparation

As team leader, I coordinated responsibilities throughout the week, monitored progress, reviewed team contributions, and ensured the completed work was incorporated into the project documentation.

Both Monday's and Friday's meetings were conducted with all three members present.

Before submission, my final responsibilities included reviewing the Week 13 report, confirming that supporting screenshots and charts were properly referenced, and ensuring the repository reflected the completed contributions.

## 9. Personal Reflection

Week 13 demonstrated how important teamwork, communication, and verification are to a successful software project.

One of my biggest lessons was that completing development work is only part of the responsibility. We also need to verify our results, document failures accurately, and ensure that someone else can understand and reproduce our findings.

I appreciated Henry's effort in completing the remaining Outlook testing and Tristan's work in organizing the final statistics and visualizations.

As team leader, I was responsible for bringing these contributions together and ensuring that our final documentation accurately represented the work completed.

Overall, Week 13 was productive, and I am satisfied with the team's progress toward completing our capstone project.

## 10. Final Week 13 Integration and Verification

Following our Friday, November 13 meeting, which all three team members attended, I reviewed the completed Week 13 contributions.

Henry completed the remaining Microsoft Outlook testing, documented the results with supporting screenshots, and contributed code-quality improvements. One Outlook trial experienced an email delivery failure, which was documented separately from codec failures.

Tristan completed the final statistical analysis, consolidated CSV datasets, five charts, and reproducibility documentation. He also updated the compatibility matrix and Week 13 results documentation.

As team leader, I coordinated the integration of our contributions, reviewed the updated documentation, and ensured that our weekly report reflected the completed work.

After the team's pull requests were merged, I synchronized the repository and ran the complete regression test suite using `python -m pytest -q`. All **83 tests and 546 subtests passed in 4.70 seconds**, with no reported failures.

I also prepared Friday's meeting minutes and finalized the Week 13 progress report.

This week reinforced the importance of teamwork, accurate documentation, and verifying the integrated project before submission.