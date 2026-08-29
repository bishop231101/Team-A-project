# Platform Testing Requirements

## Candidate Platforms
The team will initially consider the following eight platforms/environments for robustness testing:

1. WeChat
2. Telegram
3. Gmail
4. Microsoft Word
5. Notepad++
6. Browser Console
7. Microsoft Outlook
8. Discord

These platforms may be adjusted if testing limitations or accessibility issues arise.

## Testing Requirements

For each platform, the team will:

- Start with a known plaintext message.
- Encode the message using the project's zero-width Unicode encoder.
- Transfer or copy/paste the encoded message through the platform.
- Retrieve the resulting text.
- Decode the resulting text.
- Compare the recovered message with the original message.
- Record the number of zero-width characters sent.
- Record the number of zero-width characters recovered.
- Record the number of characters lost or corrupted.
- Calculate the zero-width character survival rate.
- Record whether the original message was successfully recovered.

## Data to Record

Each test should record at least:

- Platform
- Test number
- Original message
- Number of encoded characters sent
- Number of encoded characters recovered
- Number of characters lost
- Survival rate
- Decode success/failure
- Notes about platform behavior

## Week 2 scope

For Week 2, the goal is to establish the candidate platform list and define the testing requirements. Actual platform testing and the development of automated testing will occur during later weeks according to the team semester plan.