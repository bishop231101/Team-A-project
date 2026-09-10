# Week 4 Platform Testing Results

## Objective

Test the zero-width Unicode steganography codec across Gmail,
Discord, and Microsoft Word using the Week 3 test cases.

## Test Messages

1. Hello
2. CS481
3. Team A
4. Zero Width Test
5. 1234567890
6. This is a longer test message for Week 3.
7. Zero width    spacing test
8. Hello! @#$% & Test?
9. CS481 Test 123!

## Test Procedure

For each platform, each Week 3 test message was encoded using the team's
zero-width Unicode codec. The encoded text was transferred through the
platform and then retrieved. The recovered text was analyzed to determine
how many zero-width characters survived. The recovered payload was then
passed to the decoder and compared with the original message.

For each test, the following information was recorded:
- Original message
- Expected result
- Zero-width characters sent
- Zero-width characters recovered
- Characters lost
- Survival rate
- Decode result
- Error, if applicable
- Actual result 
- Notes

## Gmail

### Test 1
- Original: Hello
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 152
- Zero-width characters recovered: 68
- Lost: 84
- Survival rate: 44.74%
- Decode result: FAIL
- Error: payload contains an incomplete or malformed byte block
- Actual result: 68 of 152 zero-width characters survived the transfer, resulting in a 44.74% survival rate. The recovered payload could not be decoded because it contained an incomplete or malformed byte block.
- Notes: Gmail preserved some zero-width characters, but enough were removed or altered that the remaining payload could not be decoded.

### Test 2
- Original: CS481
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 152
- Zero-width characters recovered: 64
- Lost: 88
- Survival rate: 42.11%
- Decode result: FAIL
- Error: payload contains an incomplete or malformed byte block
- Actual result: 64 of 152 zero-width characters survived the transfer, resulting in a 42.11% survival rate. The recovered payload could not be decoded because it contained an incomplete or malformed byte block.
- Notes: Similar to Test 1 Gmail is preserving some of the zero-width characters but enough were removed or altered that it could not be properly decoded.

### Test 3
- Original: Team A
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 161
- Zero-width characters recovered: 68 
- Lost: 93
- Survival rate: 42.24%
- Decode result: FAIL
- Error: payload contains an incomplete or malformed byte block
- Actual result: 68 of 161 zero-width characters survived the transfer, resulting in a 42.24% survival rate. The recovered payload could not be decoded because it contained an incomplete or malformed byte block.
- Notes: Gmail stripped a significant portion of the zero-width characters, resulting in an incomplete payload and decode failure.

### Test 4
- Original: Zero Width Test
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 242
- Zero-width characters recovered: 113 
- Lost: 129
- Survival rate: 46.69%
- Decode result: FAIL
- Error: payload contains an incomplete or malformed byte block
- Actual result: 113 of 242 zero-width characters survived the transfer, resulting in a 46.69% survival rate. The recovered payload could not be decoded because it contained an incomplete or malformed byte block.
- Notes: Gmail continues to strip significant portions of the zero-wdith characters, resulting in incomplete payload and a decode failure.

### Test 5
- Original: 1234567890
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 197
- Zero-width characters recovered: 86 
- Lost: 111
- Survival rate: 43.65% 
- Decode result: FAIL
- Error: payload contains incomplete or malformed byte block
- Actual result: 86 of 197 zero-width characters survived the transfer, resulting in a 43.65% survival rate. The recovered payload could not be decoded because it contained an incomplete or malformed byte block.
- Notes: Gmail continues to strip significant portions of the zero-width characters, resulting in incomplete payload and decode failure.

### Test 6
- Original: This is a longer test message for Week 3.
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 476
- Zero-width characters recovered: 241
- Lost: 235
- Survival rate: 50.63%
- Decode result: FAIL
- Error: payload contains an incomplete or malformed byte block
- Actual result: 241 of 476 zero-width characters survived the transfer, resulting in a 50.63% survival rate. The recovered payload could not be decoded because it contained an incomplete or malformed byte block.
- Notes: Gmail continues to strip significant portions of the zero-width characters, resulting in incomplete payload and decode failure.

### Test 7
- Original: Zero width    spacing test
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 341
- Zero-width characters recovered: 161
- Lost: 180
- Survival rate: 47.21%
- Decode result: FAIL
- Error: payload contains an incomplete or malformed byte block
- Actual result: 161 of 341 zero-width characters survived the transfer, resulting in a 47.21% survival rate. The recovered payload could not be decoded because it contained an incomplete or malformed byte block.
- Notes: Gmail continues to strip significant portions of the zero-width characters, resulting in incomplete payload and decode failure.

### Test 8
- Original: Hello! @#$% & Test?
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 278
- Zero-width characters recovered: 123
- Lost: 155
- Survival rate: 44.24%
- Decode result: FAIL
- Error: payload contains an incomplete or malformed byte block
- Actual result: 123 of 278 zero-width characters survived the transfer, resulting in a 44.24% survival rate. The recovered payload could not be decoded because it contained an incomplete or malformed byte block.
- Notes: Gmail continues to strip significant portions of the zero-width characters, resulting in incomplete payload and decode failure.

### Test 9
- Original: CS481 Test 123!
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 242
- Zero-width characters recovered: 107
- Lost: 135
- Survival rate: 44.21% 
- Decode result: FAIL
- Error: payload contains an incomplete or malformed byte block
- Actual result: 107 of 242 zero-width characters survived the transfer, resulting in a 44.21% survival rate. The recovered payload could not be decoded because it contained an incomplete or malformed byte block.
- Notes: Gmail continues to strip significant portions of the zero-width characters, resulting in incomplete payload and decode failure.

### Gmail Overall Results

All 9 test cases were successfully transferred through Gmail for testing. Gmail consistently removed a substantial portion of the zero-width Unicode characters, with survival rates ranging from 42.11% to 50.63%. None of the 9 recovered payloads could be decoded successfully; each resulted in an incomplete or malformed byte block error. These results indicate that Gmail does not reliably preserve the zero-width characters required by the current steganography codec.

## Discord

### Test 1
- Original: Hello
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 152
- Zero-width characters recovered: 152
- Lost: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 152 of 152 zero-width characters survived; decoding succeeded.
- Notes: Discord preserved the complete zero-width payload, allowing the original message to be successfully recovered.

### Test 2
- Original: CS481
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 152
- Zero-width characters recovered: 152
- Lost: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 152 of 152 zero-width characters survived; decoding succeeded.
- Notes: Discord preserved the payload, allowing it to be decoded successfully, matching the original message.

### Test 3
- Original: Team A
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 161
- Zero-width characters recovered: 161
- Lost: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 161 of 161 zero-width characters survived; decoding succeeded.
- Notes: Discord preserved the zero-width payload, allowing the original message to be successfully recovered.

### Test 4
- Original: Zero Width Test
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 242
- Zero-width characters recovered: 242
- Lost: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 242 of 242 zero-width characters survived; decoding succeeded.
- Notes: Discord preserved the zero-width payload, allowing the original message to be successfully recovered.

### Test 5
- Original: 1234567890
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 197
- Zero-width characters recovered: 197
- Lost: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 197 of 197 zero-width characters survived; decoding succeeded.
- Notes: Discord preserved the zero-width payload, allowing the original message to be successfully recovered.

### Test 6
- Original: This is a longer test message for Week 3.
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 476
- Zero-width characters recovered: 476
- Lost: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 476 of 476 zero-width characters survived; decoding succeeded
- Notes: Discord preserved the zero-width payload, allowing the original message to be successfully recovered.

### Test 7
- Original: Zero width    spacing test
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 341
- Zero-width characters recovered: 341
- Lost: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 341 of 341 zero-width characters survived; decoding succeeded.
- Notes: Discord preserved the zero-width payload, allowing the original message to be successfully recovered.

### Test 8
- Original: Hello! @#$% & Test?
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 278
- Zero-width characters recovered: 278
- Lost: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 278 of 278 zero-width characters survived; decoding succeeded.
- Notes: Discord preserved the zero-width payload, allowing the original message to be successfully recovered.

### Test 9
- Original: CS481 Test 123!
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 242
- Zero-width characters recovered: 242
- Lost: 0
- Survival rate: 100.00%
- Decode result: PASS
- Error: None
- Actual result: 242 of 242 zero-width characters survived; decoding succeeded.
- Notes: Discord preserved the zero-width payload, allowing the original message to be successfully recovered.

### Discord Overall Results

All 9 test cases were successfully transferred through Discord and decoded correctly. Discord preserved 100% of the zero-width characters for every test, with survival rates of 100.00% across all 9 test cases. All recovered payloads decoded successfully and exactly matched their original messages. These results indicate that Discord reliably preserved the complete zero-width payload used by the current steganography codec.

## Microsoft Word

### Test 1
- Original: Hello
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 152
- Zero-width characters recovered: 68
- Lost: 84
- Survival rate: 44.74%
- Decode result: FAIL
- Error: payload contains an incomplete or malformed byte block
- Actual result: 68 of 152 zero-width characters survived; decoding failed.
- Notes: Microsoft Word removed a substantial portion of the zero-width characters during the save and reopen process, preventing the original payload from being successfully decoded.

### Test 2
- Original: CS481
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 152
- Zero-width characters recovered: 64
- Lost: 88
- Survival rate: 42.11%
- Decode result: FAIL
- Error: payload contains an incomplete or malformed byte block
- Actual result: 64 of 152 zero-width characters survived; decoding failed.
- Notes: Microsoft Word removed a substantial portion of the zero-width characters during the save and reopen process, preventing the original payload from being successfully decoded.

### Test 3
- Original: Team A
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 161
- Zero-width characters recovered: 68
- Lost: 93
- Survival rate: 42.24%
- Decode result: FAIL
- Error: payload contains an incomplete or malformed byte block
- Actual result: 68 of 161 zero-width characters survived; decoding failed.
- Notes: Microsoft Word removed a substantial portion of the zero-width characters during the save and reopen process, preventing the original payload from being successfully decoded.

### Test 4
- Original: Zero Width Test
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 242
- Zero-width characters recovered: 113
- Lost: 129
- Survival rate: 46.69%
- Decode result: FAIL
- Error: payload contains an incomplete or malformed byte block
- Actual result: 113 of 242 zero-width characters survived; decoding failed.
- Notes: Microsoft Word removed a substantial portion of the zero-width characters during the save and reopen process, preventing the original payload from being successfully decoded.

### Test 5
- Original: 1234567890
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 197
- Zero-width characters recovered: 86
- Lost: 111
- Survival rate: 43.65%
- Decode result: FAIL
- Error: payload contains an incomplete or malformed byte block
- Actual result: 86 of 197 zero-width characters survived; decoding failed.
- Notes: Microsoft Word removed a substantial portion of the zero-width characters during the save and reopen process, preventing the original payload from being successfully decoded.

### Test 6
- Original: This is a longer test message for Week 3.
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 476
- Zero-width characters recovered: 241
- Lost: 235
- Survival rate: 50.63%
- Decode result: FAIL
- Error: payload contains incomplete or malformed byte block
- Actual result: 241 of 476 zero-width characters survived; decoding failed.
- Notes: Microsoft Word removed a substantial portion of the zero-width characters during the save and reopen process, preventing the original payload from being successfully decoded.

### Test 7
- Original: Zero width    spacing test
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 341
- Zero-width characters recovered: 161
- Lost: 180
- Survival rate: 47.21%
- Decode result: FAIL
- Error: payload contains an incomplete or malformed byte block
- Actual result: 161 of 341 zero-width characters survived; decoding failed.
- Notes: Microsoft Word removed a substantial portion of the zero-width characters during the save and reopen process, preventing the original payload from being successfully decoded.

### Test 8
- Original: Hello! @#$% & Test?
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 278
- Zero-width characters recovered: 123
- Lost: 155
- Survival rate: 44.24%
- Decode result: FAIL
- Error: payload contains an incomplete or malformed byte block
- Actual result: 123 of 278 zero-width characters survived; decoding failed.
- Notes: Microsoft Word removed a substantial portion of the zero-width characters during the save and reopen process, preventing the original payload from being successfully decoded.

### Test 9
- Original: CS481 Test 123!
- Expected result: The recovered message should decode successfully and exactly match the original message.
- Zero-width characters sent: 242
- Zero-width characters recovered: 107
- Lost: 135
- Survival rate: 44.21%
- Decode result: FAIL
- Error: payload contains an incomplete or malformed byte block
- Actual result: 107 of 242 zero-width characters survived; decoding failed
- Notes: Microsoft Word removed a substantial portion of the zero-width characters during the save and reopen process, preventing the original payload from being successfully decoded.

## Microsoft Word Overall Results

All 9 test cases were successfully transferred through Microsoft Word and evaluated after saving, closing, reopening, and copying the document contents. Microsoft Word consistently removed a substantial portion of the zero-width Unicode characters. Survival rates ranged from 42.11% to 50.63%, with an average survival rate of approximately 45.08% across all 9 tests. None of the 9 recovered payloads could be decoded successfully; each resulted in an incomplete or malformed byte block error. These results indicate that Microsoft Word does not reliably preserve the zero-width characters required by the current steganography codec during the save and reopen process.

## Week 4 Overall Platform Comparison

A total of 27 platform tests were completed across Gmail, Discord, and Microsoft Word, using the same 9 test messages developed during Week 3.

| Platform       | Tests | Successful Decodes | Failed Decodes | Average Survival Rate | Overall Result |
| -------------- | ----: | -----------------: | -------------: | --------------------: | -------------- |
| Gmail          |     9 |                0/9 |            9/9 |                45.08% | FAIL           |
| Discord        |     9 |                9/9 |            0/9 |               100.00% | PASS           |
| Microsoft Word |     9 |                0/9 |            9/9 |                45.08% | FAIL           |

### Comparison Summary

Discord produced the strongest results during Week 4. All 9 test cases successfully preserved 100% of the zero-width characters, and every recovered payload decoded successfully and exactly matched its original message. No zero-width characters were lost during the Discord tests.

Gmail and Microsoft Word produced significantly weaker results. Both platforms preserved less than half of the zero-width characters on average, with an average survival rate of 45.08% across their 9 tests. All 18 Gmail and Microsoft Word tests resulted in decoding failures because the recovered payloads contained incomplete or malformed byte blocks.

These results demonstrate that platform behavior has a major effect on the reliability of zero-width Unicode steganography. Although the codec successfully passed the Week 3 local round-trip tests, transferring the encoded payload through different platforms can cause zero-width characters to be removed or altered. Discord preserved the complete payload in all tests, while Gmail and Microsoft Word removed enough characters to make the current payload undecodable.

### Week 4 Conclusion

The Week 4 testing established a clear difference in zero-width Unicode preservation between the three tested platforms. Discord appears to be compatible with the current codec, while Gmail and Microsoft Word are not reliable for preserving the encoded payload in their tested workflows. These findings provide a measurable baseline for future testing and will help determine which additional platforms and robustness techniques should be investigated in later weeks.
