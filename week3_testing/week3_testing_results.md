# Week 3 Testing Results

## Test Environment

- Platform: Local Python environment
- Branch tested: `henry/week3-zero-width-codec`
- Python version: 3.14.5
- Cover text: `Visible cover text.`

## Testing Procedure

1. Select a test message.
2. Encode the message using the zero-width Unicode encoder.
3. Embed the encoded message into the cover text.
4. Decode the embedded message.
5. Compare the decoded message with the original.
6. Verify that the visible cover text remains unchanged.
7. Record the encoded zero-width character count and test result.

## Results

| Test # | Type | Original Message | Encoded ZW Characters | Decoded Message | Cover Unchanged | Result |
|---|---|---|---:|---|---|---|
| 1 | Basic text | `Hello` | 152 | `Hello` | Yes | **PASS** |
| 2 | Course identifier | `CS481` | 152 | `CS481` | Yes | **PASS** |
| 3 | Team identifier | `Team A` | 161 | `Team A` | Yes | **PASS** |
| 4 | Phrase with spaces | `Zero Width Test` | 242 | `Zero Width Test` | Yes | **PASS** |
| 5 | Numbers | `1234567890` | 197 | `1234567890` | Yes | **PASS** |
| 6 | Longer message | `This is a longer test message for Week 3.` | 476 | `This is a longer test message for Week 3` | Yes | **PASS** |
| 7 | Multiple consecutive spaces | `Zero width    spacing test` | 341 | `Zero width    spacing test` | Yes | **PASS** |
| 8 | Special characters | `Hello! @#$% & Test?` | 278 | `Hello! @#$% & Test?` | Yes | **PASS** |
| 9 | Mixed content | `CS481 Test 123!` | 242 | `CS481 Test 123!` | Yes | **PASS** |

## Summary

- Total tests: 9
- Passed: 9
- Failed: 0
- Overall result: **PASS**