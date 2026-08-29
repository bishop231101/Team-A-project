# Week 2 Unicode Research

## Project Context

Project 5: Zero-Width Unicode Steganography with Social-Media Robustness Engineering

Course: CS481 Capstone Project

Team: Team A

Researcher: Henry Smith, Team Member A

## Purpose

This document explains the Unicode characters that the project will use to hide information inside ordinary text. It also records the initial design for the encoder, decoder, error handling, and testing work.

## What Is Steganography?

Steganography hides the existence of a secret message. In this project, the visible text is the carrier. A person reading the carrier should see normal text, while the program looks for invisible characters that represent the hidden message.

This is different from encryption. Encryption makes a message unreadable without a key, while steganography attempts to make the existence of the message difficult to notice. The project focuses on the second problem and measures how well the hidden data survives when text is copied through different platforms.

## Zero-Width Unicode Characters

Zero-width characters do not normally occupy visible space on the screen. They may be used by software for text layout, joining behavior, or language processing. Because they are not visible to a person, they can also be used as symbols in a text-steganography experiment.

### Characters Selected For This Project

- `U+200B` - ZERO WIDTH SPACE (ZWSP): project symbol for binary `0`.
- `U+200C` - ZERO WIDTH NON-JOINER (ZWNJ): project symbol for binary `1`.
- `U+200D` - ZERO WIDTH JOINER (ZWJ): project separator between encoded sections.

The project uses these characters according to the required project specification. Their normal Unicode behavior is important because a platform may preserve them, remove them, replace them, or change how they interact with nearby characters.

## Initial Binary Mapping

The encoder will use the following mapping:

```text
Binary 0  -> U+200B
Binary 1  -> U+200C
Separator -> U+200D
```

For example, if a small piece of a message becomes the binary sequence `0101`, the encoded zero-width sequence will be:

```text
U+200B U+200C U+200B U+200C
```

The characters are invisible in the carrier text, but the decoder can identify their code points and convert them back to binary values.

## Proposed Encoding Process

1. Accept a secret message as text.
2. Convert the message into a consistent byte representation, initially UTF-8.
3. Convert each byte into binary bits.
4. Replace each binary `0` with `U+200B`.
5. Replace each binary `1` with `U+200C`.
6. Add `U+200D` separators according to the message-framing design.
7. Insert the zero-width sequence into an ordinary carrier string.
8. Save or display the carrier without exposing the secret message visibly.

## Proposed Decoding Process

1. Receive the carrier text.
2. Extract every occurrence of `U+200B`, `U+200C`, and `U+200D`.
3. Interpret `U+200B` as binary `0` and `U+200C` as binary `1`.
4. Use `U+200D` to identify boundaries between encoded sections.
5. Group the recovered bits into bytes.
6. Convert the bytes back into UTF-8 text.
7. Validate the message length, framing, and error-detection information.
8. Return the original message or a clear decoding-error result.

## Message Framing and Validation

The decoder needs a way to determine where the hidden message starts and ends. The team will evaluate a simple frame containing:

- A format or version indicator.
- The payload length.
- The encoded payload.
- A checksum or other validation value.
- Optional redundancy and error-correction information.

Validation is necessary because a platform may remove some characters without making the visible carrier look different. Without validation, damaged data could be returned as if it were a correct message.

## Platform Robustness Risks

The hidden characters may not survive every transfer. Possible outcomes include:

- The platform preserves all zero-width characters.
- The platform removes some or all zero-width characters.
- The platform changes the order of characters.
- The platform normalizes or replaces characters.
- Copying through a browser, email client, or word processor changes the text.
- The carrier remains visually unchanged even though the hidden payload is damaged.

For this reason, the experiment must record the platform, application or browser, operating system when relevant, transfer method, message sample, characters sent, characters received, and decode result.

## Error-Correction Direction

The project will compare repetition with Reed-Solomon or Hamming error correction. Repetition stores extra copies or repeated information. Error correction adds structured redundancy that may allow the decoder to reconstruct missing or damaged data.

The final evaluation will compare:

- Baseline encoding with no correction.
- Repetition-based redundancy.
- The selected Reed-Solomon or Hamming method.

Each approach will be tested after 10%, 20%, and 30% of the encoded characters are stripped. The important result is not only how many characters survive, but whether the complete original message can still be recovered.

## Initial Testing Plan

### Functional Tests

- Encode and decode short text.
- Encode and decode long text.
- Test letters, numbers, punctuation, spaces, and line breaks.
- Test Unicode input.
- Test empty input and invalid input.
- Test incomplete and malformed zero-width sequences.
- Test each supported redundancy setting.

### Robustness Tests

- Use the same controlled message set across platforms.
- Use at least 30-50 samples for experimental claims.
- Test at least eight platforms or environments.
- Record the number of zero-width characters sent and received.
- Record whether the decoder recovered the exact original message.
- Repeat tests so that individual failures do not determine the conclusion.

## Measurements

- Character survival rate = zero-width characters received / zero-width characters sent x 100.
- Decode success rate = correctly decoded messages / messages attempted x 100.
- Recovery improvement = corrected decode success rate - baseline decode success rate.
- Round-trip accuracy = identical decoded messages / messages tested x 100.

The team should report both survival rate and decode success rate. A platform might preserve many characters but still damage an important part of the message, so character survival alone is not enough.


