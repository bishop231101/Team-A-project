# CS481 – Team 1 Week 11 Error-Correction Design Review

**Week:** October 26 – November 1, 2026  
**Reviewer:** Ifeanyi Emeka – Team Leader  
**Status:** Initial design review; implementation pending verification

## 1. Purpose

This document reviews the planned error-correction feature for our zero-width Unicode steganography project. It establishes design requirements, identifies risks, and defines the tests needed before the team can consider the implementation complete.

Week 11 also includes unfinished Week 10 baseline production testing. Both workstreams must be tracked separately to avoid confusing preliminary findings with verified production results.

## 2. Current Project Status

Week 10 preliminary testing identified differences in how platforms preserve zero-width Unicode characters. Some tested workflows preserved the encoded characters, while Gmail and Microsoft Word showed substantial character loss.

These observations provide useful examples of possible corruption but do not replace the planned 168 official production trials.

As of this review, Henry's Week 11 implementation and Tristan's outstanding production testing have not been verified through submitted pull requests.

## 3. Error-Correction Approaches

### Hamming Codes

Hamming codes provide a relatively simple approach for correcting limited bit errors.

**Advantages:**
- Lower implementation complexity.
- Useful for demonstrating correction of isolated bit errors.
- Relatively small overhead for certain configurations.

**Limitations:**
- Standard Hamming codes have limited correction capability.
- They may be unsuitable for substantial character deletion or burst corruption.

### Reed–Solomon Codes

Reed–Solomon codes operate on symbols and can correct a defined number of symbol errors or erasures depending on the code configuration.

**Advantages:**
- Suitable for certain multi-symbol corruption patterns.
- Configurable redundancy and recovery capacity.
- Potentially stronger protection against grouped errors.

**Limitations:**
- Higher implementation complexity.
- Increased encoded payload length.
- Recovery is not guaranteed when corruption exceeds the selected code's capability.

**Design consideration:** Platform removal of zero-width characters may cause deletions rather than ordinary symbol substitutions. The team must evaluate whether either method can recover such damage without additional framing, synchronization, or erasure-location information.

## 4. Design Requirements

Henry's proposed implementation should:

1. Preserve the existing baseline codec behavior by default.
2. Provide an optional error-correction mode.
3. Document the selected algorithm and its configuration.
4. Record the added payload length and redundancy overhead.
5. Recover payloads within the demonstrated correction capability.
6. Reject unrecoverable or invalid payloads without reporting false success.
7. Maintain compatibility with existing baseline-encoded messages.
8. Include clear installation instructions if additional dependencies are required.

## 5. Required Validation Tests

The implementation should be tested against:

- No-error encoding and decoding.
- Correctable corruption within the selected method's limits.
- Uncorrectable corruption beyond those limits.
- Boundary conditions and empty payloads.
- Unicode payloads.
- Deterministic repeated tests.
- Incorrect or altered error-correction metadata.
- Baseline-mode backward compatibility.
- Encoded-length overhead.

Every claimed result must be supported by executable tests, actual output, and screenshots or other reproducible evidence.

## 6. Week 10 Carryover Requirements

Before closing the baseline testing milestone, Tristan must provide:

- Production trial records following the approved testing protocol.
- Original sent and retrieved text evidence.
- Platform and workflow identifiers.
- Trial-level retention and decoding results.
- A reproducible summary of the results.
- Documentation of missing or incomplete trials.

The team must distinguish completed production trials from preliminary feasibility tests.

## 7. Responsibilities

**Henry Smith:** Compare candidate error-correction methods, document the design decision, implement the selected optional mode, and provide automated tests.

**Tristan Koch:** Complete outstanding baseline testing, document observed corruption patterns, and create reproducible corruption fixtures for error-correction testing.

**Ifeanyi Emeka:** Review design tradeoffs, evaluate backward compatibility and overhead, audit evidence, coordinate outstanding work, and update the project schedule and weekly report.

## 8. Review Findings and Risks

The principal technical risk is that error correction may not recover payloads when platforms remove the invisible characters entirely.

Additional risks include increased payload size, incompatible decoding behavior, insufficient test coverage, and unsupported claims about recovery performance.

The team should not claim that the new mode solves Gmail or Microsoft Word failures without verified experiments demonstrating successful recovery.

## 9. Acceptance Criteria

The design will be ready for approval when:

- Henry submits a documented design decision and implementation.
- Automated tests demonstrate the stated correction capability.
- Baseline compatibility is verified.
- Encoded-length overhead is measured.
- Failure cases are reported accurately.
- Supporting evidence is available in GitHub.
- Outstanding Week 10 testing is reported separately and accurately.

## 10. Review Conclusion

The proposed error-correction feature is an appropriate Week 11 development objective, but its effectiveness remains unverified.

Final approval is pending Henry's implementation, Tristan's testing evidence, and review of the actual results.

**Review Status:** Open – Awaiting implementation and test evidence.