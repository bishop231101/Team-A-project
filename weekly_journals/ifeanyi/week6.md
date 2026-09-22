# Week 6 Weekly Journal - Ifeanyi Emeka

## What I Did
This week, I focused on improving the recovery capability of our zero-width Unicode steganography project. I reviewed the existing encoder and decoder, ran the baseline automated tests, and confirmed that all 19 tests and 108 subtests passed. I also tested the repetition-based recovery method by intentionally corrupting one repeated bit and verifying that the original secret could still be recovered. I documented the results and added screenshot evidence to the Week 6 testing folder.

## What I Learned
I learned how repetition-based error recovery can improve the reliability of zero-width encoded data. By storing repeated copies of each bit, the decoder can use the majority value to recover from a single corrupted symbol.

## Problems Encountered
The main challenge was making sure the recovery test intentionally damaged the encoded payload without making the entire message unrecoverable. After reviewing how the repetition method works, I was able to corrupt one symbol and successfully recover the original secret.

## Next Week's Plan
Next week, I will continue testing the robustness of the recovery method, compare the results with previous testing, and help integrate the team's work into the project.