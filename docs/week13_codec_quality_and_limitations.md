# Week 13 Codec Quality, Diagnostics, and Limitations

**Contributor:** Henry Smith
**Scope:** zero-width Unicode codec and optional Hamming SECDED mode

## Quality checks completed

- Ran the complete automated suite: 83 tests and 546 subtests passed.
- Preserved the existing `DecodeError` exception type and human-readable messages.
- Added stable `DecodeError.category` values so tests and production tools do not need to classify failures by matching message text.
- Added `diagnose_stego_text()` for structured success/failure records. It catches expected decode failures only; type errors and unexpected programming errors remain visible.
- Added package markers so the repository's `tests` modules are not shadowed by an unrelated installed package during pytest collection.
- Added automated coverage for successful Hamming diagnostics, missing-payload diagnostics, stable error categories, and propagation of programming errors.

## Google Chrome Browser Console production results

- Completed all 24 approved trials: eight corpus messages with three repetitions each.
- Each prepared payload was pasted into Chrome DevTools Console, copied back without manual correction, and analyzed with the repository production workflow.
- All 24 trials retained 100% of the encoded zero-width characters and recovered the expected secret exactly.
- Each trial includes its sent text, retrieved text, JSON analysis record, UTC timestamp, and a console screenshot in its evidence directory.
- These results apply specifically to the tested Chrome DevTools Console paste-and-copy-back operation. They do not imply that every Chrome input field or web application preserves zero-width characters.

## Diagnostic interpretation

The structured diagnostic result contains the detected encoding mode, exact recovered secret on success, and a category plus message on failure. A detected failure is a safe result: the codec refuses to return text that failed its structural, length, UTF-8, checksum, or error-correction checks.

Diagnostic categories identify the first condition the decoder can prove. They do not claim to identify the original platform operation that caused the damage. For example, a deletion can shift a frame and surface as a malformed block or length mismatch.

## Algorithm limitations

### Zero-width character survival

The codec cannot force another application to preserve U+200B, U+200C, or U+200D. Platforms may delete, normalize, reorder, or reject invisible characters. Complete removal produces a `missing_payload` failure and cannot be recovered by any current mode.

### Baseline mode

Baseline mode detects corruption through framing and CRC-32 but does not correct it. CRC-32 provides accidental-corruption detection, not cryptographic authentication or protection against deliberate modification.

### Repetition mode

Repetition mode uses majority voting within each repeated bit group. It can recover only while every affected group retains a strict majority. Separator deletion, concentrated damage, reordering, or removal beyond the majority threshold is not recoverable. The repeated representation also increases payload length substantially.

### Hamming SECDED mode

Hamming SECDED corrects one altered bit in a 13-symbol codeword and detects two altered bits in that codeword. It does not recover deleted or inserted symbols because those operations destroy codeword alignment. Three or more alterations in one codeword are outside the SECDED guarantee and may be rejected under a different diagnostic or, for some patterns, miscorrected before the frame checksum rejects the result. Hamming mode also adds approximately 62.5% bit-level redundancy before separator and prefix overhead.

### Security and confidentiality

Zero-width encoding hides data visually but does not encrypt it. Anyone who knows the character mapping can recover the secret. The codec does not provide access control, secrecy, authenticity, or non-repudiation. Sensitive information must be encrypted separately before embedding.

### Format identification

The decoder identifies modes through reserved zero-width prefixes. Unrelated text containing the same project characters can be interpreted as a candidate payload and then rejected. Cover text containing project codec characters is therefore rejected during embedding to prevent ambiguous repeated embedding.

### Resource use

Payload size grows linearly with the UTF-8 secret length, and recovery modes increase it further. The current implementation does not impose an application-level maximum secret length, so callers should enforce limits appropriate to the target platform and available memory.

## Recommended reporting language

Results should say that the codec *recovered*, *detected and rejected damage*, or *could not be tested because the platform blocked the documented operation*. A rejected corrupted payload is not a successful recovery, but it is preferable to an undetected incorrect result.
