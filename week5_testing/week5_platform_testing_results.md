# Week 5 Platform Testing Results

## Objective

The objective of Week 5 testing is to evaluate the zero-width Unicode steganography system across additional platforms and compare how well each platform preserves the hidden zero-width characters and encoded payload.

The platforms tested during Week 5 are:

- Microsoft Outlook
- Telegram Web
- Notepad++

The same test messages and testing methodology used during Week 4 are used where applicable so that the results can be compared consistently.

## Test Messages

The following nine test messages are used for Week 5 platform testing:

1. `Hello`
2. `CS481`
3. `Team A`
4. `Zero Width Test`
5. `1234567890`
6. `This is a longer test message for Week 3.`
7. `Zero width    spacing test`
8. `Hello! @#$% & Test?`
9. `CS481 Test 123!`

## Test Procedure

For each platform, the following procedure is performed:

1. Generate the encoded test message using the zero-width Unicode encoder.
2. Copy the contents of the generated text file.
3. Paste/send the encoded message through the platform being tested.
4. Copy the transferred message back to the clipboard.
5. Compare the original encoded message with the recovered message.
6. Calculate the number of zero-width characters sent, recovered, and lost/corrupted.
7. Calculate the zero-width character survival rate.
8. Attempt to decode the recovered hidden message.
9. Compare the decoded message with the original message.
10. Record the results and take screenshots of the terminal output.

The following information is recorded for each test:

- Original message
- Expected result
- Zero-width characters sent
- Zero-width characters recovered
- Zero-width characters lost/corrupted
- Survival rate
- Decode result
- Error
- Actual result
- Notes

---

# Microsoft Outlook

## Test 1

- Original message: `Hello`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 152
- Zero-width characters recovered: 152
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 152 of 152 zero-width characters survived; decoding succeeded
- Notes: Microsoft Outlook preserved all zero-width characters with no loss or corruption.

## Test 2

- Original message: `CS481`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 152
- Zero-width characters recovered: 152
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 152 of 152 zero-width characters survived; decoding succeeded
- Notes: Microsoft Outlook preserved all zero-width characters with no loss or corruption.

## Test 3

- Original message: `Team A`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 161
- Zero-width characters recovered: 161
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 161 of 161 zero-width characters survived; decoding succeeded
- Notes: Microsoft Outlook preserved all zero-width characters with no loss or corruption.

## Test 4

- Original message: `Zero Width Test`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 242
- Zero-width characters recovered: 242
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 242 of 242 zero-width characters survived; decoding succeeded
- Notes: Microsoft Outlook preserved all zero-width characters with no loss or corruption.

## Test 5

- Original message: `1234567890`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 197
- Zero-width characters recovered: 197
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 197 of 197 zero-width characters survived; decoding succeeded
- Notes: Microsoft Outlook preserved all zero-width characters with no loss or corruption.

## Test 6

- Original message: `This is a longer test message for Week 3.`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 476
- Zero-width characters recovered: 476
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 476 of 476 zero-width characters survived; decoding succeeded
- Notes: Microsoft Outlook preserved all zero-width characters with no loss or corruption.

## Test 7

- Original message: `Zero width    spacing test`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 341
- Zero-width characters recovered: 341
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 341 of 341 zero-width characters survived; decoding succeeded
- Notes: Microsoft Outlook preserved all zero-width characters with no loss or corruption.

## Test 8

- Original message: `Hello! @#$% & Test?`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 278
- Zero-width characters recovered: 278
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 278 of 278 zero-width characters survived; decoding succeeded
- Notes: Microsoft Outlook preserved all zero-width characters with no loss or corruption.

## Test 9

- Original message: `CS481 Test 123!`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 242
- Zero-width characters recovered: 242
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 242 of 242 zero-width characters survived; decoding succeeded
- Notes: Microsoft Outlook preserved all zero-width characters with no loss or corruption.

## Microsoft Outlook Overall Results

| Metric | Result |
|---|---|
| Total Tests | 9 |
| Successful Decodes | 9 |
| Failed Decodes | 0 |
| Average Survival Rate | 100.00% |
| Overall Result | 9/9 tests passed; all zero-width characters survived and all hidden messages decoded successfully. |

---

# Telegram Web

## Test 1

- Original message: `Hello`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 152
- Zero-width characters recovered: 152
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 152 of 152 zero-width characters survived; decoding succeeded.
- Notes: Telegram Web preserved all zero-width characters with no loss or corruption.

## Test 2

- Original message: `CS481`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 152
- Zero-width characters recovered: 152
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 152 of 152 zero-width characters survived; decoding succeeded
- Notes: Telegram Web preserved all zero-width characters with no loss or corruption.

## Test 3

- Original message: `Team A`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 161
- Zero-width characters recovered: 161
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 161 of 161 zero-width characters survived; decoding succeeded
- Notes: Telegram Web preserved all zero-width characters with no loss or corruption.

## Test 4

- Original message: `Zero Width Test`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 242
- Zero-width characters recovered: 242
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 242 of 242 zero-width characters survived; decoding succeeded
- Notes: Telegram Web preserved all zero-width characters with no loss or corruption.

## Test 5

- Original message: `1234567890`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 197
- Zero-width characters recovered: 197
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 197 of 197 zero-width characters survived; decoding succeeded
- Notes: Telegram Web preserved all zero-width characters with no loss or corruption.

## Test 6

- Original message: `This is a longer test message for Week 3.`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 476
- Zero-width characters recovered: 476
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 476 of 476 zero-width characters survived; decoding succeeded
- Notes: Telegram Web preserved all zero-width characters with no loss or corruption.

## Test 7

- Original message: `Zero width    spacing test`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 341
- Zero-width characters recovered: 341
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 341 of 341 zero-width characters survived; decoding succeeded
- Notes: Telegram Web preserved all zero-width characters with no loss or corruption

## Test 8

- Original message: `Hello! @#$% & Test?`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 278
- Zero-width characters recovered: 278
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 278 of 278 zero-width characters survived; decoding succeeded
- Notes: Telegram Web preserved all zero-width characters with no loss or corruption.

## Test 9

- Original message: `CS481 Test 123!`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 242
- Zero-width characters recovered: 242
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 242 of 242 zero-width characters survived; decoding succeeded
- Notes: Telegram Web preserved all zero-width characters with no loss or corruption.

## Telegram Web Overall Results

| Metric | Result |
|---|---|
| Total Tests | 9 |
| Successful Decodes | 9 |
| Failed Decodes | 0 |
| Average Survival Rate | 100.00% |
| Overall Result | 9/9 tests passed; all zero-width characters survived and all hidden messages decoded successfully. |

---

# Notepad++

## Test 1

- Original message: `Hello`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 152
- Zero-width characters recovered: 152
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 152 of 152 zero-width characters survived; decoding succeeded
- Notes: Notepad++ preserved all zero-width characters with no loss or corruption.

## Test 2

- Original message: `CS481`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 152
- Zero-width characters recovered: 152
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 152 of 152 zero-width characters survived; decoding succeeded
- Notes: Notepad++ preserved all zero-width characters with no loss or corruption.

## Test 3

- Original message: `Team A`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 161
- Zero-width characters recovered: 161
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 161 of 161 zero-width characters survived; decoding succeeded
- Notes: Notepad++ preserved all zero-width characters with no loss or corruption.

## Test 4

- Original message: `Zero Width Test`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 242
- Zero-width characters recovered: 242
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 242 of 242 zero-width characters survived; decoding succeeded
- Notes: Notepad++ preserved all zero-width characters with no loss or corruption.

## Test 5

- Original message: `1234567890`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 197
- Zero-width characters recovered: 197
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 197 of 197 zero-width characters survived; decoding succeeded
- Notes: Notepad++ preserved all zero-width characters with no loss or corruption.

## Test 6

- Original message: `This is a longer test message for Week 3.`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 476
- Zero-width characters recovered: 476
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 476 of 476 zero-width characters survived; decoding succeeded
- Notes: Notepad++ preserved all zero-width characters with no loss or corruption.

## Test 7

- Original message: `Zero width    spacing test`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 341
- Zero-width characters recovered: 341
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 341 of 341 zero-width characters survived; decoding succeeded
- Notes: Notepad++ preserved all zero-width characters with no loss or corruption.

## Test 8

- Original message: `Hello! @#$% & Test?`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 278
- Zero-width characters recovered: 278
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 278 of 278 zero-width characters survived; decoding succeeded
- Notes: Notepad++ preserved all zero-width characters with no loss or corruption.

## Test 9

- Original message: `CS481 Test 123!`
- Expected result: Hidden message should decode successfully.
- Zero-width characters sent: 242
- Zero-width characters recovered: 242
- Zero-width characters lost/corrupted: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 242 of 242 zero-width characters survived; decoding succeeded
- Notes: Notepad++ preserved all zero-width characters with no loss or corruption.

## Notepad++ Overall Results

| Metric | Result |
|---|---|
| Total Tests | 9 |
| Successful Decodes | 9 |
| Failed Decodes | 0 |
| Average Survival Rate | 100.00% |
| Overall Result | 9/9 tests passed; all zero-width characters survived and all hidden messages decoded successfully. |

---

# Week 5 Overall Platform Comparison

A total of 27 platform tests were completed across Telegram Web, Microsoft Outlook, and Notepad++, using the same 9 test messages used during previous platform testing.

| Platform | Tests | Successful Decodes | Failed Decodes | Average Survival Rate | Overall Result |
|---|---:|---:|---:|---:|---|
| Microsoft Outlook | 9 | 9 | 0 | 100.00% | PASS |
| Telegram Web | 9 | 9 | 0 | 100.00% | PASS |
| Notepad++ | 9 | 9 | 0 | 100.00% | PASS |

## Comparison Summary

The Week 5 results compare how Microsoft Outlook, Telegram Web, and Notepad++ handle zero-width Unicode characters.

The comparison will focus on:

- Zero-width character survival rate
- Number of successful decodes
- Number of failed decodes
- Whether characters are removed or corrupted
- Differences between platforms
- Whether the hidden message remains recoverable after transfer

All three platforms tested during Week 5 preserved the complete zero-width payload across all nine test messages. Telegram Web, Microsoft Outlook, and Notepad++ each achieved a 100.00% average survival rate and successfully decoded all 9 test messages.

Across the 27 Week 5 tests, all 27 hidden messages were successfully recovered and decoded, with no zero-width characters lost or corrupted during testing. These results show that the current codec remained fully recoverable when transferred or processed through the three Week 5 test platforms.

## Week 5 Conclusion

Week 5 testing evaluated the zero-width steganography codec across Microsoft Outlook, Telegram Web, and Notepad++. Each platform successfully preserved all zero-width characters across all nine test messages. The total results were 27 successful decodes out of 27 tests, with an overall average survival rate of 100.00%.

The Week 5 results provide additional evidence that the current zero-width codec can successfully preserve and recover hidden messages across platforms that maintain the zero-width Unicode characters used by the codec.