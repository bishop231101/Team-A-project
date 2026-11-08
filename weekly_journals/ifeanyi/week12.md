# Week 12 Individual Journal — Ifeanyi Emeka

**Course:** CS481 — Capstone Project  
**Role:** Team Leader  
**Reporting Period:** November 2–8, 2026

## 1. Work Completed

During Week 12, I focused on coordinating team activities, independently verifying software functionality, reviewing and integrating GitHub contributions, and ensuring that our project documentation accurately reflected the team's progress. This week was particularly important because we completed the Hamming SECDED stabilization work, production testing across three applications, and the full Baseline-versus-Hamming comparative experiment.

### Team Leadership and Coordination

On Monday, November 2, I conducted our Week 12 team meeting with all three members present. We reviewed the previous week's accomplishments, identified outstanding tasks, and established priorities for the current reporting period.

I coordinated Henry's responsibility for stabilizing the Hamming SECDED implementation and supporting verification, while Tristan focused on completing production-platform testing and preparing the comparative recovery experiments.

I documented the meeting discussions, decisions, responsibilities, and action items in `meeting_minutes/2026-11-02_week12.md`.

On Friday, November 6, I conducted our second weekly meeting, with all three members present. We discussed the team's progress, reviewed testing evidence, addressed comparative experiment requirements, and established priorities for completing the remaining deliverables.

I documented the Friday meeting in `meeting_minutes/2026-11-06_week12.md` and pushed the completed minutes to GitHub.

Throughout the week, I maintained communication with both team members, reviewed their progress, provided feedback, and coordinated the completion and integration of their assigned tasks.

### Independent Automated Testing

At the beginning of Week 12, I independently executed the project's automated Python regression suite using:

`python -m pytest -q`

The initial results were:

- 67 tests passed.
- 148 subtests passed.
- Execution time: 5.17 seconds.
- No reported failures.

I captured the terminal results and included the screenshot in our Week 12 report as supporting evidence.

Following Henry's Hamming stabilization changes, I independently tested the updated implementation. The expanded regression suite passed **74 tests and 546 subtests in 4.62 seconds**.

I also executed Henry's dedicated Hamming stability verification script, which confirmed successful protected-mode round trips, supported single-bit recovery, rejection of tested corruption conditions, and encoded-length overhead measurements.

After integrating Henry's and Tristan's initial contributions, I executed the complete regression suite again. The results showed **74 tests and 546 subtests passing in 5.06 seconds**.

Following the final integration of Tristan's comparative experiment PR #29, I ran the complete automated regression suite once more.

**Final integrated regression results:**

- Tests passed: 80
- Subtests passed: 546
- Execution time: 6.06 seconds
- Reported failures: None

These results confirmed that the integrated implementation continued to satisfy the covered regression checks after the Week 12 changes were merged.

### GitHub Review and Integration

I reviewed Henry's Hamming stabilization PR #27 and independently verified the implementation before merging it into the main branch.

I also reviewed Tristan's production-testing PR #28, which included 72 production trial records across Gmail, Notepad++, and Microsoft Word, along with supporting screenshots, reproducibility documentation, and testing results.

During the integration process, I encountered a Git merge conflict involving the Week 12 progress report. I resolved the conflict while preserving the necessary documentation and updates.

I later reviewed Tristan's comparative experiment PR #29, focusing on the approved methodology, corruption conditions, seed configurations, individual trial records, and reported results.

I identified documentation concerns involving the fixed logical bit-corruption targets and the differences between Baseline and Hamming deletion schedules. I communicated these concerns to Tristan and requested clarification before merging.

After the methodology was clarified, I merged PR #29 into `main` and independently reran the project's automated regression suite.

These activities helped maintain repository consistency, preserve project documentation, and ensure that the team's completed contributions were properly integrated.

### Production Testing and Comparative Experiment Coordination

I monitored Tristan's production-testing progress and reviewed the reported findings across the three applications.

The submitted results showed:

- **Notepad++:** 24 successful exact recoveries out of 24 trials, with 100% zero-width character retention.
- **Microsoft Word:** No successful exact recoveries across 24 trials, with 0% zero-width character retention.
- **Gmail:** No successful exact recoveries across 24 trials, with substantial zero-width character loss.

These results demonstrated that application-specific handling of invisible Unicode characters significantly affects the reliability of our steganography technique.

I also coordinated with Henry and Tristan regarding the comparative experiment methodology.

Tristan initially completed an SA01 pilot involving five corruption conditions evaluated under Baseline and Hamming modes, producing 10 trial records. Following the pilot review, I approved the full experiment methodology.

The completed comparative experiment included four approved corpus messages (SA01, SU01, LA01, and LU01), two encoding modes, five corruption conditions, and three deterministic repetitions, producing **120 individual trials**.

I approved the repetition-specific seed pairs and confirmed that the logical bit-corruption targets would remain fixed across repetitions. I also requested that the experiment documentation explain how the deletion conditions were applied fairly across the two encoding modes.

Tristan completed the experiment and reported that an independent audit of the trial records, summary statistics, and experiment report found no discrepancies.

**The final reported comparative results were:**

- Total trials: 120
- Baseline successful recoveries: 12 of 60
- Hamming successful recoveries: 24 of 60
- Total successful recoveries: 36
- Detected failures: 84
- Undetected errors: 0

Hamming successfully recovered all 12 tested single-bit corruption trials, while Baseline recovered none of the corresponding trials. Both modes detected or rejected the tested double-bit corruption and deletion conditions.

The results demonstrated the benefit of Hamming protection against supported single-bit errors while also showing its limitations when encoded symbols are deleted.

I reviewed the submitted methodology and coordinated the integration of the comparative experiment into the main repository.

### Documentation and Weekly Reporting

Throughout Week 12, I maintained and updated the team's progress report to reflect completed milestones, individual contributions, testing results, and remaining project requirements.

I incorporated testing screenshots with explanations, documented the Hamming stabilization results, and updated the comparative experiment section to include the completed 120-trial evaluation.

I also ensured that the report distinguished completed Week 12 objectives from broader production-platform testing that remains part of our future project work.

Both required weekly meeting records were maintained, and I updated my individual journal to accurately reflect my leadership, technical verification, integration, and documentation responsibilities.

## 2. Challenges and Outstanding Work

One of the main challenges this week was coordinating several technical activities while ensuring that testing and documentation remained accurate.

The team needed to stabilize the Hamming implementation, complete outstanding production trials, and execute the comparative experiment within the same reporting period. I had to monitor progress closely and ensure that each contribution was reviewed before integration.

Another challenge involved resolving a Git merge conflict while maintaining the accuracy of the Week 12 report. This required careful attention to prevent important documentation from being lost.

The comparative experiment also required additional methodological clarification. Although the experiment used different deterministic seed pairs across repetitions, the logical bit-corruption targets remained fixed. I worked with Tristan to ensure that this distinction was documented correctly.

We also needed to clarify that Baseline and Hamming used the same deletion percentages and corresponding seeds, but their different encoded layouts could produce different actual deletion counts and physical positions.

These issues were addressed before the final integration.

Although the Week 12 comparative experiment is complete, broader platform testing and additional corruption scenarios remain future project work.

## 3. Lessons Learned

This week reinforced the importance of leadership, communication, independent verification, and disciplined project management.

I learned that completing software development tasks is only one part of a successful project. Every contribution must also be tested, documented, reviewed, and integrated correctly.

Running the regression suite independently helped me confirm that the software continued to function after changes were merged rather than relying entirely on teammates' reported results.

I also gained more experience reviewing pull requests, resolving Git conflicts, coordinating experimental methodologies, and maintaining technical documentation.

The production-testing results showed that successful local encoding and decoding do not guarantee reliable recovery across external applications. Different applications process invisible Unicode characters differently, which can affect message integrity.

The comparative experiment also demonstrated the importance of understanding the limitations of error correction. Hamming protection improved recovery from the tested single-bit corruption but did not restore deleted symbols.

Another important lesson was that reproducible experiments require clearly defined corruption targets, deterministic seeds, accurate trial records, and consistent outcome classifications.

As team leader, I learned the value of reviewing technical details before approving a merge. Identifying and addressing documentation concerns helped ensure that our final results were presented accurately.

## 4. Next Steps

With the Week 12 implementation and comparative experiment completed, my next priorities are to:

1. Complete the final review of the Week 12 progress report and confirm that the testing evidence and screenshots are correctly referenced.
2. Commit and push any remaining report or journal updates to the main GitHub repository.
3. Submit the Week 12 repository link before the course deadline.
4. Coordinate future production testing across the remaining approved applications.
5. Continue evaluating platform compatibility, error-correction limitations, and additional corruption scenarios.
6. Maintain team accountability, regular meetings, GitHub contributions, and documentation standards for the next phase of the project.

## 5. Current Status

Week 12 was a productive period for our team. We completed the Hamming SECDED stabilization, expanded automated testing, production trials across three applications, and the full 120-trial comparative recovery experiment.

I conducted and documented both required team meetings, coordinated responsibilities, independently verified the Hamming implementation, reviewed and merged PRs #27, #28, and #29, resolved a Git merge conflict, and updated the team's documentation.

Following the final integration, the automated regression suite passed **80 tests and 546 subtests in 6.06 seconds**, with no reported failures.

The comparative experiment reported **36 successful recoveries, 84 detected failures, and zero undetected errors** across 120 trials.

The completed work demonstrated improved recovery from supported single-bit corruption through Hamming SECDED while identifying limitations associated with deletion and application-specific character handling.

**Overall Status:** Week 12 leadership, Hamming stabilization, comparative testing, GitHub integration, and regression verification completed. Final documentation submission and broader future platform testing remain.