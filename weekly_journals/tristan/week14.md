# Week 14 Journal — Tristan Koch

## Weekly Focus

Focus on final testing, validating the project's experimental results, completing and improving the charts, and preparing the Results and Evaluation sections for the final academic report.

## Work Completed

- Conducted a Codex-assisted, read-only audit of the existing project branch to identify areas requiring updates, corrections, or improvements in clarity and readability based on my assigned Week 14 responsibilities.
- Used the audit findings to make targeted updates to the existing Week 13 documentation so that completed production trial counts, blocked trials, and final results are accurately represented.
- Updated the Week 13 compatibility matrix and results consolidation documentation to remove outdated trial counts and reflect the finalized experimental results.
- Improved the charts in `docs/week13_results.md` to make the experimental data easier to read, interpret, and compare. This included redesigning the existing charts and separating information into two panels for:
  - Chart 3: Production Platform Comparison
  - Chart 4: Baseline vs. Hamming Recovery by Corruption Condition
  - Chart 5: Hamming Encoding Overhead
- Replaced the previous chart exports with the updated PNG files and revised the accompanying descriptions so that each chart and its individual panels accurately explain the information being presented.
- Used Codex to visually inspect the updated chart exports, verify the Markdown image references, and compare the documented results against the existing CSV data.
- Used Codex to verify the automated testing suites:
  - Full regression suite: 87 tests passed and 549 subtests passed in 11.38 seconds.
  - Relevant targeted Hamming suite: 65 tests passed and 546 subtests passed in 0.87 seconds.
- Used Codex to assist with drafting the Results and Evaluation documents for the final academic report, drawing on the production testing records, comparative experiment results, charts, CSV files, and supporting project documentation collected throughout the project.
- Personally reviewed both documents section by section to ensure that the descriptions, interpretations, and conclusions accurately reflected the work completed and the results actually recorded. I then used Codex to perform final audits against the original JSON trial records, consolidated CSV files, charts, and supporting documentation to double-check the reported figures, percentages, and consistency of the information before submitting the documents for team review.

## What I Learned

I learned the importance of separating large or complex datasets across multiple charts and panels rather than attempting to display every measurement in a single chart. Dividing the information makes the results easier to navigate, read, and understand without sacrificing the amount of information being communicated.

I also gained a better understanding of the importance of checking visualizations against their underlying CSV data and written results. A chart must not only be readable but also accurately represent the experimental measurements and conclusions.

Preparing the Results and Evaluation sections also reinforced the importance of consolidating evidence from different stages of a project. Experimental conclusions need to be supported by the original testing records and documented methodology rather than relying only on summarized statistics or assumptions.

## Problems and Challenges

One of the main challenges was improving the readability of the charts while ensuring that the data remained consistent with the existing CSV files and finalized experimental results. I also needed to make sure that the descriptions and explanations accurately reflected what each chart and panel displayed, particularly after separating several figures into multiple panels.

Another consideration was preserving the distinction between completed and blocked trials so that the final recovery statistics and comparisons remained accurate.

Preparing the Results and Evaluation documentation presented an additional challenge because it required consolidating findings from the production testing and comparative experiments conducted throughout the project. This involved ensuring that the reported figures, interpretations, and conclusions were supported by the original JSON trial records, consolidated CSV files, charts, and documented testing procedures. The documents also needed to present the results clearly without making claims that went beyond what the experiments actually demonstrated.

I also experienced illness during this week, which affected the amount of time I could spend working and required me to limit extended screen time. This made it more difficult to complete tasks that involved prolonged reading, reviewing documentation, and working at the computer. I had to work around these limitations while prioritizing the accuracy of the documentation and completing the work as my health allowed.

## Next Steps

- The completed Results and Evaluation documents have been committed and submitted through a pull request for team review.
- Address any requested corrections or feedback identified during the team review before the documentation is incorporated into the final academic report.
- Continue coordinating with the team on the remaining final report and presentation work as health permits.
