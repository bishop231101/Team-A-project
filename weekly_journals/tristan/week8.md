# Week 8 Weekly Journal - Tristan Koch

## Project

Zero-Width Unicode Steganography with Social-Media Robustness Engineering

## Week 8 Focus

Documenting testing methodology and preliminary results for the Midterm Report, reviewing previous testing results, updating platform compatibility information, and creating reproducible figures from the collected testing data

## Work Completed

During Week 8, I focused on organizing and documenting the testing work completed during the earlier weeks of the project for inclusion in the team's Midterm Report. My assigned work was to write the testing methodology and preliminary-results sections, update the testing results and platform compatibility information, create baseline figures from the collected testing data, organize testing evidence, and document my individual contributions.

I reviewed the platform compatibility and recovery testing completed during Weeks 3 through 7 and consolidated the results into a testing review document. The review included the Week 3 local encoder/decoder testing, Week 4 platform testing, Week 5 platform and baseline recovery testing, Week 6 improved recovery testing, and Week 7 expanded recovery testing. I also reviewed the recovery results and supporting evidence to identify important trends, limitations, and areas that needed to be clarified in the Midterm Report.

I created a testing methodology document describing the purpose and procedures used for both platform compatibility testing and controlled recovery/corruption testing. The methodology documents the testing process, measurements collected, survival-rate calculation, decode-success criteria, evidence collection process, and limitations of the testing performed so far.

I also created a preliminary-results document summarizing the platform compatibility results and recovery/corruption results through Week 8. The document includes the Week 5 baseline results, Week 6 improved recovery results, Week 7 expanded recovery results, Week 8 platform testing results, preliminary findings, supporting figures, limitations, and a summary.

As part of the Week 8 platform testing and results review, I incorporated the additional platform results for Microsoft Word, Gmail, Windows Notepad, Browser Console, and Discord. These results expanded the platform coverage and provided additional evidence that different applications handle zero-width Unicode characters differently.

I created two report-ready figures from the collected testing data. The first figure shows decode success and failure across the six platforms tested during Weeks 4–5. The second figure shows recovery outcomes across the controlled corruption scenarios tested during Week 7. I saved the figures as PNG files in the repository's Week 8 figures folder so they can be referenced directly from the Markdown documentation.

I also created and included a platform compatibility matrix in the preliminary-results documentation. The matrix summarizes the testing period, platform, number of tests, survival results, decode results, and overall compatibility classification.

## Testing and Results

The Week 8 documentation work incorporated the results from the platform compatibility and recovery testing performed throughout the semester so far.

The platform compatibility review showed significant differences between applications in their handling of zero-width Unicode characters. During Weeks 3–5, Gmail and Microsoft Word did not successfully preserve enough of the hidden payload for decoding, while Discord, Microsoft Outlook, Telegram Web, and Notepad++ successfully preserved and decoded the tested messages.

The additional Week 8 platform tests expanded this comparison. Microsoft Word and Discord did not preserve the hidden payload in the tested representative message. Gmail recovered only 25 of the original 206 zero-width characters, resulting in a 12.14% survival rate and unsuccessful decoding. Windows Notepad and the Browser Console preserved all 206 zero-width characters and successfully recovered the hidden message.

The recovery testing results showed the progression from the original recovery system to the improved five-copy recovery method. The Week 5 baseline recovery tests failed under all four tested corruption scenarios. The improved five-copy method successfully recovered all six controlled scenarios tested during Week 6.

The expanded Week 7 testing showed that recovery remained successful under several higher corruption levels but failed under more severe conditions. The 40% removal scenario successfully recovered its message, while the 50% and 60% removal scenarios failed. The 30% and 40% alteration scenarios successfully recovered their messages, while the 50% alteration scenario failed despite retaining 100.00% of the zero-width characters. The 40% mixed corruption scenario successfully recovered its message.

The results were then used to create the preliminary-results figures and compatibility matrix included in the Week 8 documentation.

## Evidence and Documentation

* I organized the previously collected results and evidence into documentation suitable for use in the midterm report.

* I used Codex to help consolidate my Weeks 3-7 testing results into `tristan_week3-7_testing_review.md`
    - it includes the results, statistics, possible figures, and limitations I identified while reviewing the tests

* created `tristan_week8_testing_methodology_section.md` to document the procedures used for platform compatibility testing and controlled recovery/corruption testing.
    - also defines the survival-rate and decode-success measurements used throughout the testing.

* created `tristan_week8_preliminary_results.md` to document the preliminary results through week 8.
    - includes platform compatibility results, recovery and corruption results, survival rate results, and decode-success measurements used throughout testing.

* using relevant data from weeks 3-7 I created png figures for the preliminary-results documentation
    - the figures were added under the repository's `week8_figures` folder and referenced in the markdown file

* also included platform compatibility matrix in the preliminary-results documentation to provide a direct comparison of the tested platforms and their decode outcomes.

## What I Learned

While preparing the midterm report material, I learned that explaining how a test was performed is different from presenting its results or explaining what those results mean.

One thing that stood out during my review was how differently the applications handled the hidden text. Some kept the zero-width characters intact, while others removed or changed them. I learned that I cannot assume a message will work across applications just because it worked in one of them.

Reviewing the recovery results also reinforced the difference between survival rate and successful message recovery. A high survival rate does not necessarily mean that the hidden message can be decoded successfully. The 50% alteration test from Week 7 retained 100.00% of the zero-width characters but still failed to decode, demonstrating that altered characters can prevent successful recovery even when no characters are removed.

The comparison of the Week 5, Week 6, and Week 7 recovery results also showed the improvement provided by the five-copy recovery method while demonstrating that recovery performance still has limitations under higher levels of controlled corruption.

Creating the figures and compatibility matrix also showed how collected testing data can be converted into a more understandable format for a technical report. Visualizing the results makes it easier to identify successful and failed recovery scenarios and compare platform compatibility.

## Problems and Challenges

My biggest challenge this week was  bringing together results from several weeks of testing. Since the tests were not all performed the same way, I had to keep the different procedures and results clear instead of treating them as one identical set of tests.

Another challenge was interpreting survival-rate results correctly. Survival rate measures how much of the zero-width payload remains after corruption, but it does not directly indicate whether the decoder can successfully reconstruct the hidden message. This distinction needed to be clearly explained in the preliminary-results documentation.

Another challenge was determining how to present the platform results because the earlier platform tests in Weeks 4–5 used nine messages per platform, while the Week 8 platform testing used one representative message per platform. I kept these results distinguishable rather than combining them into a single statistic that could make the testing appear more uniform than it actually was.

I also needed to make sure that the figures accurately represented the collected testing results and that the image paths were correctly referenced from the Markdown documentation.

## Next Steps

Before submitting my work, I still need to check the results, make sure the figure links work, and verify the formatting. Once everything looks correct, I'll commit and push my changes on my Week 8 branch and open a pull request for the team to review.

I will also continue supporting the team with testing, documentation, and analysis as the project moves into the remaining weeks of the semester.
