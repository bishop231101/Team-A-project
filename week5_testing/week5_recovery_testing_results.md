# Week 5 Recovery Testing Results

## Objective

The objective of Week 5 recovery testing is to evaluate whether hidden messages can still be recovered when zero-width Unicode characters are partially removed or altered after encoding.

The recovery tests focus on:
- Partial removal of zero-width characters
- Alteration of zero-width characters
- Zero-width character survival/recovery rate
- Whether the hidden message can still be decoded
- Whether the decoded message matches the original message

## Recovery Testing Method

For each recovery test:

1. Generate an encoded message using the zero-width Unicode encoder.
2. Record the original encoded message and zero-width character count.
3. Intentionally remove or alter a portion of the zero-width characters.
4. Record the modified zero-width character count.
5. Calculate the resulting zero-width character survival rate.
6. Attempt to decode the modified message.
7. Record whether decoding succeeds or fails.
8. If decoding succeeds, compare the recovered message with the original hidden message.
9. Record the results and take a screenshot of the terminal output.

## Terminal Command Descriptions

The terminal commands used during recovery testing automated the creation, corruption, measurement, and decoding of each test message.

- **Generate stego message:** The encoder command created a text file containing the visible cover text and the hidden message encoded using zero-width Unicode characters.
- **Load encoded message:** The encoded text file was loaded into a PowerShell environment variable so it could be processed by subsequent Python commands.
- **Count zero-width characters:** The command counted the zero-width space (U+200B), zero-width non-joiner (U+200C), and zero-width joiner (U+200D) characters in the encoded message.
- **Apply corruption:** The removal tests intentionally deleted a percentage of zero-width characters. The alteration test changed selected zero-width characters to different zero-width characters. The combined test performed both types of corruption.
- **Calculate recovery statistics:** The command compared the original and damaged encoded messages to determine the number of zero-width characters remaining or lost and calculated the resulting survival rate. It also confirmed that the visible cover text remained unchanged.
- **Attempt decoding:** The decoder attempted to extract the hidden message from the damaged encoded text. The recovered message was compared with the original hidden message when decoding succeeded. Decode errors were recorded when the corrupted data could not be recovered.


## Recovery Test Scenarios

### Test 1 — Partial Zero-Width Removal

- Original message: `Hello`
- Zero-width characters before modification: 152
- Zero-width characters after modification: 105
- Zero-width characters removed: 47
- Survival rate: 69.08%
- Decode result: FAILED
- Recovered message: None
- Match with original: No
- Error: `DecodeError: payload contains an incomplete or malformed byte block`
- Notes: Approximately 30% of the zero-width characters were intentionally removed. The visible cover text remained unchanged, but the damaged hidden payload could not be decoded.

### Test 2 — Greater Partial Zero-Width Removal

- Original message: `Zero Width Test`
- Zero-width characters before modification: 242
- Zero-width characters after modification: 121
- Zero-width characters removed: 121
- Survival rate: 50.00%
- Decode result: FAILED
- Recovered message: None
- Match with original: No
- Error: `DecodeError: payload contains an incomplete or malformed byte block`
- Notes: 50% of the zero-width characters were intentionally removed. The visible cover text remained unchanged, but the damaged hidden payload could not be decoded.

### Test 3 — Zero-Width Character Alteration

- Original message: `CS481 Test 123!`
- Zero-width characters before modification: 242
- Zero-width characters after modification: 242
- Zero-width characters altered: 74
- Survival rate: 100.00%
- Decode result: FAILED
- Recovered message: None
- Match with original: No
- Error: `DecodeError: payload contains an incomplete or malformed byte block`
- Notes: Approximately 30% of the zero-width characters were intentionally altered to different zero-width characters. All zero-width characters remained present, resulting in a 100% character survival rate, but the altered encoded data could not be decoded.

### Test 4 — Combined Removal and Alteration

- Original message: `This is a longer test message for Week 3.`
- Zero-width characters before modification: 476
- Zero-width characters after modification: 380
- Zero-width characters removed: 96
- Zero-width characters altered: 76
- Survival rate: 79.83%
- Decode result: FAILED
- Recovered message: None
- Match with original: No
- Error: `DecodeError: payload contains an incomplete or malformed byte block`
- Notes: Approximately 20% of the zero-width characters were removed, followed by alteration of approximately 20% of the remaining zero-width characters. The visible cover text remained unchanged, but the combined corruption prevented the hidden payload from being decoded.

## Recovery Testing Summary

| Test | Scenario | Original Zero-Width Characters | Remaining Zero-Width Characters | Lost Zero-Width Characters | Altered Zero-Width Characters | Survival Rate | Decode Result |
|---|---|---:|---:|---:|---:|---:|---|
| 1 | Approximately 30% removal | 152 | 105 | 47 | 0 | 69.08% | FAILED |
| 2 | 50% removal | 242 | 121 | 121 | 0 | 50.00% | FAILED |
| 3 | Approximately 30% alteration | 242 | 242 | 0 | 74 | 100.00% | FAILED |
| 4 | Approximately 20% removal + approximately 20% alteration | 476 | 380 | 96 | 76 | 79.83% | FAILED |

Across all four recovery scenarios, the visible cover text remained unchanged. Tests 1 and 2 demonstrated that removing zero-width characters caused the encoded payload to become undecodable. Test 3 demonstrated that zero-width characters can all remain present while alteration of approximately 30% of them still prevents successful decoding. Test 4 combined removal and alteration and also resulted in a decode failure.

## Recovery Testing Conclusion

The Week 5 recovery tests evaluated the current zero-width Unicode codec under intentional data corruption. All four tested corruption scenarios resulted in decode failure, including approximately 30% zero-width-character removal, 50% removal, approximately 30% character alteration, and combined removal and alteration.

The results show that the current codec does not successfully recover the tested hidden messages after these levels of zero-width-character corruption. The alteration test is particularly relevant because the zero-width character survival rate remained 100.00%, while changing approximately 30% of the characters still prevented successful decoding. This demonstrates that character presence alone does not guarantee that the encoded payload remains valid.

These results provide a baseline for evaluating the project's planned redundancy and error-correction approach. Future testing can determine whether repetition and Reed-Solomon error correction improve recovery after zero-width characters are removed or altered.