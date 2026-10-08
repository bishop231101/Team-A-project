# Week 8 Midterm Contribution: System Architecture and Codec

**Author:** Henry Smith  
**Purpose:** Report-ready technical sections for integration into the Team A
Midterm Report.

## System architecture

The project uses a small modular Python architecture centered on the codec in
`src/zero_width_codec.py`. The system accepts ordinary cover text and a UTF-8
secret, constructs a self-validating binary frame, converts the frame into
zero-width Unicode characters, and appends the invisible payload to the cover.
The reverse path filters the supported zero-width characters, decodes the
frame, validates its structure and checksum, and returns the secret only when
every integrity check succeeds.

```text
Cover text + UTF-8 secret
           |
           v
  Frame construction
  ZWS1 | length | payload | CRC-32
           |
           v
 Standard bit mapping or optional repetition protection
           |
           v
 Visible cover + zero-width payload
           |
           v
 Character filtering -> mode detection -> bit/byte decoding
           |
           v
 Length, marker, checksum, and UTF-8 validation
           |
           v
     Verified secret or explicit DecodeError
```

### Main components

| Component | Responsibility |
| --- | --- |
| `encode_secret()` | Builds the framed payload and maps its bits to zero-width characters. |
| `embed_secret()` | Validates the cover and appends the encoded payload. |
| `extract_secret()` | Isolates codec characters, detects the format, decodes, and validates the frame. |
| Repetition encoder/decoder | Repeats bits and uses majority voting for limited corruption recovery. |
| `count_codec_characters()` | Measures transmitted and recovered codec symbols for platform testing. |
| Automated tests | Verify round trips, validation failures, Unicode behavior, recovery boundaries, and backward compatibility. |

The implementation uses only Python's standard library. This keeps the local
prototype reproducible and allows the core demonstration to run without a
network connection or third-party package.

## Codec representation

The codec uses three Unicode characters:

| Meaning | Character |
| --- | --- |
| Binary `0` | `U+200B` ZERO WIDTH SPACE |
| Binary `1` | `U+200C` ZERO WIDTH NON-JOINER |
| Structural separator | `U+200D` ZERO WIDTH JOINER |

Visible cover text is not modified. The encoded zero-width payload is appended
to it. Removing these three codec characters reproduces the original visible
cover exactly.

## Binary frame

Before Unicode mapping, the secret is encoded as UTF-8 and placed in this
binary frame:

```text
magic: "ZWS1" (4 bytes)
payload length (4-byte unsigned big-endian integer)
UTF-8 payload (variable length)
CRC-32 checksum (4 bytes)
```

The marker distinguishes valid project data from unrelated invisible text.
The declared length detects truncation or extra data. CRC-32 detects frame
corruption, and UTF-8 validation prevents invalid bytes from being returned as
a recovered secret. These checks provide integrity and reliable failure
detection; they do not provide encryption, authentication, or secrecy against
an observer who understands the encoding.

## Baseline encoding and decoding

In standard mode, every byte is converted into eight bits. A `0` becomes
`U+200B`, a `1` becomes `U+200C`, and `U+200D` separates adjacent byte blocks.
The decoder requires exactly eight symbols in each block before reconstructing
the bytes and validating the frame.

The baseline mode has lower overhead than protected mode but cannot correct a
removed or altered bit. A damaged payload is rejected through block, marker,
length, checksum, or UTF-8 validation.

## Repetition-based recovery mode

Protected mode repeats each encoded bit an odd number of times and decodes the
group by majority vote. The repetition factor is configurable from 3 through
15 and is recorded as a leading run of `U+200D` characters. This permits the
decoder to recognize the format automatically and preserves compatibility with
the Week 5 three-copy format.

The evaluated Week 6 and Week 7 configuration uses five copies per bit. It can
correct at most two removed or altered data symbols in each group:

| Damaged copies in a five-symbol group | Outcome |
| ---: | --- |
| 0, 1, or 2 | Original bit remains the majority and can be recovered. |
| 3, 4, or 5 | Correction capacity is exceeded; decoding is rejected or the frame fails validation. |

Controlled Week 7 tests recovered messages through 40% distributed
data-symbol corruption. Tests at 45% and 50% were safely rejected. This is a
per-group bound: concentrated damage can exceed the limit even when the
overall percentage is lower.

## Error handling and false-success prevention

The decoder raises `DecodeError` instead of returning partial or unverified
text when it encounters:

- no supported zero-width payload;
- malformed byte or repetition groups;
- an invalid repetition prefix;
- incomplete bytes;
- an unrecognized `ZWS1` marker;
- a frame-length mismatch;
- a CRC-32 mismatch; or
- invalid UTF-8 payload bytes.

This fail-closed behavior is important because successful character survival
does not necessarily mean the secret is correct. Altered zero-width characters
remain present and can produce a 100% survival count even when decoding must
fail.

## Development through the midterm

| Phase | Technical result |
| --- | --- |
| Weeks 3-4 | Deterministic encoder/decoder, reusable vectors, UTF-8 round trips, framing, validation, and measurement helpers. |
| Week 5 | Optional three-copy repetition mode with one-symbol correction. |
| Week 6 | Configurable odd repetition factors and five-copy recovery with up to two corrected symbols per group. |
| Week 7 | Higher-corruption tests established a 40% distributed recovery limit and safe failure above it. |
| Week 8 | Midterm technical verification and a reproducible offline prototype demonstration. |

As of the Week 8 technical review, the merged regression suite contains
**28 tests and 132 subtests**, all passing.

## Platform findings and architectural implications

The Week 8 compatibility tests demonstrate that platform handling is the
system's primary external constraint. Windows Notepad and the browser console
preserved the tested payload, while Word and Discord removed it and Gmail
preserved only part of it. Repetition can repair limited, distributed damage;
it cannot recover when a platform removes the complete payload or destroys
structural separators.

The core demo therefore runs locally and uses a prevalidated fallback. Platform
tests are presented as measured compatibility evidence rather than as a claim
that the method works universally.

## Current limitations

- Five-copy mode has approximately five times the data-symbol overhead.
- Group separators and the repetition prefix are not error-corrected.
- Recovery depends on how corruption is distributed among repetition groups.
- Complete removal of the zero-width payload is unrecoverable.
- Zero-width steganography is concealment, not cryptographic confidentiality.
- Compatibility results apply only to the tested applications and workflows.

## Midterm demonstration command

From the repository root, run:

```powershell
python tests/week8_testing/run_henry_midterm_demo.py
```

The demonstration is local, uses synthetic data, and verifies baseline
round-trip behavior, cover preservation, protected recovery within the limit,
and safe rejection beyond the limit.
