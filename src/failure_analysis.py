"""Diagnostic helpers for Week 9 recovered zero-width sequences."""

from __future__ import annotations

from typing import Any

from .zero_width_codec import DecodeError, count_codec_characters, extract_secret


def classify_decoder_error(message: str) -> str:
    """Map a codec error message to a stable production-trial category."""
    if "no zero-width payload" in message:
        return "complete_payload_removal"
    if "invalid repetition prefix" in message:
        return "recovery_prefix_corruption"
    if "unrecognized format marker" in message:
        return "frame_marker_corruption"
    if "frame is too short" in message or "length does not match" in message:
        return "frame_length_corruption"
    if "checksum" in message:
        return "checksum_corruption"
    if "valid UTF-8" in message:
        return "utf8_corruption"
    if "Hamming" in message and "uncorrectable" in message:
        return "error_correction_uncorrectable"
    if "Hamming" in message:
        return "error_correction_structure"
    if any(
        phrase in message
        for phrase in (
            "incomplete or malformed",
            "missing or malformed bit group",
            "no majority bit value",
            "complete bytes",
            "invalid bit value",
        )
    ):
        return "structural_corruption"
    return "decoding_failure"


def analyze_recovered_text(
    sent_text: str,
    retrieved_text: str,
    expected_secret: str,
) -> dict[str, Any]:
    """Measure count retention and classify the decoder outcome.

    Character retention is deliberately count-based. Exact message recovery and
    decoder failure are reported separately because equal counts do not prove
    that the same ordered characters survived.
    """
    if not isinstance(sent_text, str):
        raise TypeError("sent_text must be a string")
    if not isinstance(retrieved_text, str):
        raise TypeError("retrieved_text must be a string")
    if not isinstance(expected_secret, str):
        raise TypeError("expected_secret must be a string")

    sent_counts = count_codec_characters(sent_text)
    retrieved_counts = count_codec_characters(retrieved_text)
    sent_total = sent_counts["total"]
    retrieved_total = retrieved_counts["total"]
    retention_percentage = (
        (retrieved_total / sent_total * 100) if sent_total else None
    )

    result: dict[str, Any] = {
        "sent_counts": sent_counts,
        "retrieved_counts": retrieved_counts,
        "retention_percentage": retention_percentage,
        "retention_above_100_percent": (
            retention_percentage is not None and retention_percentage > 100
        ),
        "decoder_returned": False,
        "exact_match": False,
        "recovered_secret": None,
        "decoder_error": None,
        "failure_category": None,
    }

    try:
        recovered_secret = extract_secret(retrieved_text)
    except DecodeError as error:
        result["decoder_error"] = str(error)
        result["failure_category"] = classify_decoder_error(str(error))
    else:
        exact_match = recovered_secret == expected_secret
        result["decoder_returned"] = True
        result["exact_match"] = exact_match
        result["recovered_secret"] = recovered_secret
        result["failure_category"] = (
            None if exact_match else "undetected_incorrect_recovery"
        )
    return result
