# Week 9 Production Testing Protocol

Status: DRAFT — pending team confirmation
Proposed version: 1.0
Owner: Ifeanyi Emeka

## 1. Purpose

Measure preservation of the project's zero-width Unicode characters
and exact recovery of hidden messages after platform processing.

Earlier testing remains pilot evidence. Production results will be
recorded separately using this fixed procedure.

## 2. Fixed Codec Configuration

Codec: src/zero_width_codec.py

Baseline configuration:
- recovery_mode=False
- Fixed cover text: "Team 1 compatibility test."
- Encoding: embed_secret(cover_text, secret, recovery_mode=False)
- Decoding: extract_secret(retrieved_text)
- Character counts: count_codec_characters(text)

Henry must confirm the codec commit before production testing begins.
Record that commit in every trial.

Henry technical confirmation (October 15, 2026):
- Codec implementation commit: `4134cec1d23be3ae7069440a3718e09069922bdc`
- Verification checkout: `aa37928f2f026a4d6aa2e48d1c16cb25db40d40e`
- Pre-change main baseline: 28 tests and 132 subtests passed.
- Week 9 validation branch: 33 tests and 132 subtests passed.
- All eight approved corpus messages passed exact local baseline round trips.
- Detailed evidence: `docs/week9_henry_codec_confirmation.md`

Recovery-mode experiments are separate from this baseline dataset.
They must record recovery_mode and repetition_factor explicitly.

## 3. Proposed Balanced Test Corpus

Use eight messages: two messages in each of four groups.

Short ASCII:
- SA01: "Hello"
- SA02: "Test 123!"

Short Unicode:
- SU01: "Café"
- SU02: "你好"

Long ASCII:
- LA01: "The quick brown fox jumps over the lazy dog. "
  repeated exactly four times.
- LA02: "Team 1 checks message recovery, punctuation, and numbers 12345. "
  repeated exactly four times.

Long Unicode:
- LU01: "Café déjà vu — résumé. "
  repeated exactly four times.
- LU02: "你好，世界！こんにちは。 "
  repeated exactly four times.

Generate repeated messages programmatically.
Preserve all spaces and punctuation, including trailing spaces.
Save the exact messages in a UTF-8 corpus file before testing.
Do not retype or normalize messages during trials.

Balance means equal numbers of short/long and ASCII/Unicode cases.
It does not mean equal UTF-8 byte lengths.

## 4. Platform and Operation Matrix

Before testing, Tristan must document the exact workflow for each
platform-operation combination.

Candidate platforms:
- Gmail
- Discord
- Microsoft Word
- Microsoft Outlook
- Telegram Web
- Notepad++
- Browser Console
- WeChat

Distinguish operations such as:
- Paste into an editor and copy back.
- Send a message and retrieve its delivered text.
- Save a document, reopen it, and retrieve its text.

These operations are separate combinations, not interchangeable trials.

Record application/browser version, operating system, formatting mode,
and retrieval method. Specify the exact Browser Console procedure.

WeChat remains unverified. Confirm access or document an agreed scope
change before freezing the matrix. Do not report eight-platform coverage
unless all eight platforms have actually been tested.

## 5. Proposed Trial Count

Run each of the eight messages three times for every approved
platform-operation combination.

Trials per combination: 8 × 3 = 24.

Total planned production trials:
24 × number of approved platform-operation combinations.

Examples:
- Seven combinations: 168 trials.
- Eight combinations: 192 trials.

These counts are proposed workload targets, not a statistical
sample-size guarantee.

Week 9 target:
Complete all 24 trials for at least half of the approved combinations,
rounding the number of combinations upward.

Record the final matrix and total before starting production collection.

## 6. Procedure for Each Trial

1. Assign a unique trial ID.
2. Load the exact message by corpus ID.
3. Encode it with the fixed cover text and baseline configuration.
4. Confirm locally that decoding returns the exact original message.
5. Count sent codec characters.
6. Perform the documented platform operation using a fresh transfer.
7. Save the retrieved text exactly as obtained.
8. Count retrieved codec characters.
9. Attempt decoding and preserve any DecodeError message.
10. Compare the decoded result with the original using exact equality.
11. Save the trial record and supporting evidence.

A failed local round trip is a setup defect; resolve it before
collecting that production trial.

Do not manually repair retrieved text before measurement.
Retain platform failures as results. Log diagnostic reruns separately.

## 7. Required Trial Fields

- Trial ID and UTC timestamp
- Tester
- Corpus ID
- Platform and operation ID
- Application/browser version and operating system
- Codec commit and protocol/corpus version
- Recovery mode and repetition factor
- Sent and retrieved counts for U+200B, U+200C, and U+200D
- Sent and retrieved total codec-character counts
- Character-retention percentage
- Decoder returned successfully: yes/no
- Exact original-message match: yes/no
- Decoder error, if any
- Paths to sent text, retrieved text, and supporting evidence
- Notes and deviations

## 8. Metrics

Character retention percentage:
retrieved total / sent total × 100.

This is a count-based retention measurement, not a sequence-match metric. It
cannot independently identify substitutions, insertions, reordering, or which
original symbols survived.
Flag values above 100% for investigation; do not silently cap them.

Exact recovery:
The decoder returns text that equals the original message exactly.

Report decoding errors separately from successful decoding that
returns a different message.

Summarize results by platform-operation combination and corpus group.
Include trial counts alongside percentages.

## 9. Confirmation Before Freezing

- Ifeanyi confirms the protocol, corpus, matrix, and audit fields.
- Tristan confirms workflows, platform access, and trial workload.
- Henry confirms the codec commit and local corpus round trips.

Record actual confirmations and dates in the repository.
Then mark version 1.0 frozen and link it from the Week 9 audit.

Until confirmation, the audit remains pending.
Changes after freezing require a new version and an explanation.

## 10. Team Leader Decision and Protocol Authorization

**Date:** October 17, 2026
**Authorized by:** Ifeanyi Emeka, Team Leader
**Protocol Version:** 1.0

Following the Week 9 team meeting and review of the
proposed testing methodology, the team leader has
authorized the production testing plan to move forward.

The following decisions are established:

- Eight platform-operation combinations are approved
  as the production testing scope.
- Each combination requires eight corpus messages,
  repeated three times, for 24 trials.
- Total planned production trials: 192.
- Week 9 milestone: Complete at least four approved
  combinations, representing 96 trials (50%).
- Browser Console testing will use paste-and-copy-back
  only.
- The fixed baseline codec and eight-message corpus
  will remain unchanged.
- Production results must be recorded separately
  from preliminary testing.
- All trial records must include measurements,
  decoding results, and supporting evidence.

Henry's codec verification is complete.

Tristan's workflow verification and production trial
results will be documented as they become available.

This authorization represents a team-leader decision
following the team meeting. It does not imply that
all team members individually approved every detail.

Any subsequent changes to the approved testing
scope or procedure must be documented with a
version update and explanation.

**Status:** Version 1.0 authorized for production
testing, subject to recording the exact eight
platform-operation assignments before trials begin.