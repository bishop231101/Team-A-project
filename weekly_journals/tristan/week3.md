# Week 3 Weekly Journal - Tristan Koch

## What I Did

This week, I focused on the testing and validation portion of the team's zero-width Unicode steganography project. I reviewed the team's Week 3 testing plan and prepared an initial procedure for testing the encoder and decoder locally.

After Henry completed the initial zero-width Unicode encoder/decoder implementation, I ran a series of sample-message tests against his Week 3 branch. I tested nine different messages covering basic text, course and team identifiers, numbers, longer messages, multiple spaces, special characters, and mixed content.

For each test, I encoded the message, embedded it into visible cover text, decoded it, and compared the decoded message with the original. I also verified that the visible cover text remained unchanged and recorded the number of zero-width characters produced.

I documented the testing results in a Week 3 testing results file and captured screenshots of the test output as evidence. I organized the screenshots into a dedicated Week 3 testing evidence folder so they can be referenced in the team's final report.

I also continued using Git and GitHub to manage my work, including working on my own Week 3 branch and preparing my testing documentation and evidence for submission.

## What I Learned

This week, I learned more about how zero-width Unicode characters can be used to hide information while keeping the visible text unchanged. I also learned how the encoder and decoder work together to embed and recover a hidden message.

Through testing, I learned the importance of testing more than just a simple example. Using different types of messages, including numbers, spaces, special characters, longer text, and Unicode characters, helps verify that the encoder and decoder can handle different kinds of input.

I also learned more about testing procedures and how to document measurable results. Recording the number of zero-width characters, whether the original message was successfully recovered, and whether the visible cover text changed provides evidence that the implementation is working correctly.

I gained additional experience with Git branches, GitHub, pull requests, and organizing testing evidence within the project repository.

## Problems Encountered

One challenge this week was coordinating my testing with the development of the encoder and decoder. Since Henry was responsible for implementing the codec, I initially had to wait for the implementation to become available before I could perform the actual tests.

I also had to make sure that I was testing the correct branch and using the correct project files. While running the tests, Python-generated `__pycache__` and `.pyc` files appeared in the repository, which required me to address them with the project's `.gitignore` configuration so that generated files would not accidentally be committed.

Another challenge was organizing the testing evidence and determining how the screenshots should be included in the repository. After discussing this with Ifeanyi, I organized the screenshots into a dedicated Week 3 testing screenshots folder.

## Plan for Next Week

Next week, I plan to continue working on the testing portion of the project. I will begin preparing for testing the zero-width encoder and decoder across the candidate platforms identified during Week 2.

I plan to help establish consistent procedures for transferring encoded messages through each platform, retrieving the messages, decoding them, and measuring how much of the hidden data survives.

I will also continue documenting test results and collecting evidence such as screenshots where appropriate. As the project progresses, I will help analyze survival rates and identify which platforms preserve or remove zero-width Unicode characters.

I will continue coordinating with the team and contributing my testing results and documentation through GitHub.