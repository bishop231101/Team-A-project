# Week 11 Error-Correction Design Comparison

**Prepared by:** Henry Smith

**Date:** October 27, 2026

## Observed Corruption Patterns

Henry reviewed the committed preliminary raw files for Gmail and Microsoft
Word using the Week 10 analyzer.

| Platform | Sent | Retrieved | Retention | Decoder result | Pattern |
|---|---:|---:|---:|---|---|
| Gmail | 152 | 68 | 44.74% | Rejected | All 84 U+200B symbols removed |
| Microsoft Word | 152 | 0 | 0.00% | Rejected | Complete invisible payload removed |

The visible cover remained unchanged in both samples. These are preliminary
results and are not counted as official production trials.

## Reed–Solomon and Hamming Comparison

| Consideration | Hamming SECDED | Reed–Solomon |
|---|---|---|
| Protection unit | Individual bits in a small codeword | Symbols, commonly bytes, in a block |
| Correctable damage | One altered bit per codeword | Multiple symbol errors based on parity count |
| Detectable damage | Two altered bits per codeword | More errors than it can correct, within configured limits |
| Burst-error handling | Limited | Stronger for byte/symbol bursts |
| Complexity | Small, self-contained implementation | More complex Galois-field implementation or dependency |
| Overhead | Fixed 5 parity bits for each 8 data bits | Configurable parity-symbol overhead |
| Fit with current codec | Direct bit mapping and existing CRC | Requires byte block design, sizing, and dependency review |
| Systematic symbol deletion | Not recoverable without preserved positions | Not recoverable when deletions destroy symbol boundaries or locations |
| Complete payload stripping | Not recoverable | Not recoverable |

## Recommendation

Use **Hamming SECDED as an optional experimental codec mode** for Week 11.

Reasons:

- It integrates directly with the project's existing bit-to-zero-width mapping.
- It adds no external dependency.
- It provides deterministic single-bit correction and double-bit detection.
- It preserves the existing frame, CRC-32 validation, and default codec modes.
- Its behavior and limits can be demonstrated clearly with controlled tests.

Reed–Solomon remains the stronger future candidate for byte-oriented burst
damage after the team has enough production evidence to select block sizes and
parity levels. Adding it now would not fix the observed Gmail or Word failures:
Gmail destroyed the zero-symbol positions and Word removed the entire payload.

## Implemented Format

Call the optional mode with:

```python
stego = embed_secret(
    "Visible cover",
    "hidden message",
    error_correction="hamming",
)
```

Each frame byte becomes a 13-bit extended Hamming codeword. A two-separator
prefix distinguishes the mode from standard encoding and the existing
repetition prefixes. The decoder selects the correct format automatically.

The mode cannot be combined with `recovery_mode=True`. This prevents ambiguous
layering and preserves clear, testable behavior.

## Safety and Limitations

- One altered bit in each codeword is corrected.
- Two altered bits in a codeword are rejected.
- Larger corruption is still checked by the frame marker, length, CRC-32, and
  UTF-8 validation, preventing false-success output in the tested cases.
- Deleted symbols and damaged separators are rejected because bit positions are
  no longer known.
- Gmail-style removal of U+200B and Word-style complete stripping remain
  unrecoverable and must not be presented as fixed.
