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

The compatibility matrix has been prepared and its three-platform results independently verified against the available production-testing records.

The Week 13 report has also been created and updated with supporting evidence.

The remaining work includes final statistics and charts, reproducibility documentation, code-quality review, integration of team contributions, and final report verification.

At this stage, Week 13 is progressing according to the updated timeline, but the week's full deliverables are not yet complete.

## 7. Next Steps

- Review Henry's and Tristan's Week 13 contributions when their PRs are available.
- Verify supporting tests, charts, calculations, and documentation.
- Integrate approved contributions into the main branch.
- Conduct and document Friday's team meeting.
- Update the Week 13 report and individual journal with completed work.
- Complete final verification before the Sunday submission deadline.

## 8. Personal Reflection

This week, I focused on ensuring that our results were accurate and supported by evidence. As team leader, I believe it is important to do more than collect everyone's work. I need to understand what was tested, verify the findings, and make sure our documentation accurately reflects what the project demonstrates.

The compatibility analysis helped me better understand the limitations of our steganography approach across different applications. It also reinforced how important careful testing and clear documentation are to the overall quality of our project.

I will continue coordinating with Henry and Tristan to complete the remaining Week 13 objectives.