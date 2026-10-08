# Week 8 Midterm Testing

## Full Regression Test

As part of the Week 8 midterm testing requirements, the complete automated regression test suite was executed to verify that the current zero-width Unicode steganography system remained operational before additional Week 8 testing and demonstration activities.

### Test Command

python -m pytest -v

### Results

- 28 tests passed.
- 132 subtests passed.
- No test failures were reported.
- Execution time: 0.24 seconds.

## Initial Assessment

The successful regression test confirms that the current project implementation passes the complete automated test suite at the beginning of Week 8. This provides a stable baseline for the additional midterm testing, platform trials, and prototype demonstration.

## Evidence

A terminal screenshot was captured showing the complete Week 8 regression-test result.

## Microsoft Word Platform Test

The encoded Week 8 test message was copied from the generated test file and pasted into Microsoft Word. The message was then copied from Word and saved as `word_received.txt` for analysis.

### Results

- Visible cover text survived.
- Zero-width payload did not survive.
- Decoder error: `no zero-width payload was found`
- Payload survival rate: 0%

### Assessment

Microsoft Word preserved the visible cover text but removed the zero-width Unicode payload used by the codec during the tested copy-and-paste process. The recovered text therefore could not be decoded. This shows that Microsoft Word is not compatible with the current zero-width encoding method under this test procedure.

### Evidence

A terminal screenshot was captured showing the decoder failure after the message was copied back from Microsoft Word.

## Gmail Platform Test

The encoded Week 8 test message was sent through Gmail and then copied from the received email into `gmail_received.txt`. The recovered text was analyzed using the project codec.

### Results

- Original codec characters: 206
- Recovered codec characters: 25
- U+200B recovered: 0
- U+200C recovered: 18
- U+200D recovered: 7
- Payload survival rate: 12.14%
- Decoder result: Failed
- Decoder error: `payload contains an incomplete or malformed byte block`

### Assessment

Gmail partially preserved the zero-width Unicode payload. Of the 206 original codec characters, 25 remained after transmission, giving a survival rate of approximately 12.14%. However, the recovered payload was incomplete and could not be decoded. This shows that Gmail preserves some zero-width characters but alters or removes enough of the payload to prevent successful recovery with the current encoding method.

### Evidence

A terminal screenshot was captured showing the recovered codec-character count and the decoder failure after the message was sent through Gmail.

## Windows Notepad Platform Test

The encoded Week 8 test message was opened in Windows Notepad, copied, and pasted into `notepad_received.txt`. The recovered text was then analyzed using the project codec.

### Results

- Original codec characters: 206
- Recovered codec characters: 206
- U+200B recovered: 113
- U+200C recovered: 71
- U+200D recovered: 22
- Payload survival rate: 100%
- Decoder result: Successful
- Recovered secret: `CS481-WEEK8`

### Assessment

Windows Notepad successfully preserved the complete zero-width Unicode payload during the copy-and-paste test. All 206 codec characters remained unchanged, resulting in a 100% survival rate. The decoder also successfully recovered the original secret, `CS481-WEEK8`. This demonstrates that Windows Notepad is fully compatible with the current zero-width encoding method under this test procedure.

### Evidence

A terminal screenshot was captured showing all 206 recovered codec characters and the successful decoding of `CS481-WEEK8`.

## Browser Console Platform Test

### Test Procedure

The encoded Week 8 test message was copied into a Google Chrome Developer Tools snippet and then copied back into `browser_received.txt`. The recovered message was analyzed using the project's codec-character counter and decoder.

### Results

- Original codec characters: 206
- Recovered codec characters: 206
- Survival rate: 100%
- Decoder result: Successful
- Recovered secret: `CS481-WEEK8`

### Assessment

Google Chrome Developer Tools preserved the entire zero-width Unicode payload during the copy-and-paste test. All 206 codec characters remained unchanged, resulting in a 100% survival rate. The decoder also successfully recovered the original secret, `CS481-WEEK8`. This shows that the Browser Console is fully compatible with the current zero-width encoding method under this test procedure.

### Evidence

A terminal screenshot was captured showing all 206 recovered codec characters and the successful decoding of `CS481-WEEK8`.

## Discord Platform Test

### Test Procedure

The encoded Week 8 test message was sent through Discord and then copied back into `discord_received.txt`. The recovered message was analyzed using the project's codec-character counter and decoder.

### Results

- Original codec characters: 206
- Recovered codec characters: 0
- Survival rate: 0%
- Decoder result: Failed
- Recovered secret: None

### Assessment

Discord preserved the visible cover text but removed the entire zero-width Unicode payload during the test. None of the original 206 codec characters remained, resulting in a 0% survival rate. The decoder returned `DecodeError: no zero-width payload was found`. This shows that Discord is not compatible with the current zero-width encoding method under this test procedure.

### Evidence

Terminal screenshots were captured showing zero recovered codec characters and the decoder failure after the message was transferred through Discord.

## Week 8 Platform Compatibility Matrix

The following table summarizes the platform compatibility tests completed during Week 8.

| Platform | Codec Characters Recovered | Survival Rate | Secret Decoded | Compatibility |
|---|---:|---:|---|---|
| Microsoft Word | 0 / 206 | 0% | No | Not Compatible |
| Gmail | 25 / 206 | 12.14% | No | Not Compatible |
| Windows Notepad | 206 / 206 | 100% | Yes - `CS481-WEEK8` | Compatible |
| Browser Console | 206 / 206 | 100% | Yes - `CS481-WEEK8` | Compatible |
| Discord | 0 / 206 | 0% | No | Not Compatible |

## Week 8 Testing Summary

Five platforms were tested to determine how well the current zero-width Unicode encoding method survives transfer through different applications. Windows Notepad and the Browser Console preserved all 206 codec characters and successfully recovered the original secret, `CS481-WEEK8`. Microsoft Word and Discord removed the zero-width payload completely. Gmail preserved only 25 of the original 206 codec characters, which was not enough for successful decoding.

These results show that zero-width Unicode steganography is highly dependent on how each platform processes Unicode characters. The tests also identify which platforms can currently preserve the encoded payload and which platforms require additional robustness or recovery techniques.
