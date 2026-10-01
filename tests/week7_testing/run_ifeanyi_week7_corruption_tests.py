from src.zero_width_codec import embed_secret, extract_secret


def corrupt_group(encoded, changes):
    """
    Corrupt selected zero-width symbols in the encoded payload.
    changes = number of symbols to alter in each five-copy group.
    """
    zero_width = ["\u200b", "\u200c"]

    chars = list(encoded)
    positions = [i for i, c in enumerate(chars) if c in zero_width]

    # Alter the requested number of symbols in each 5-copy group
    for start in range(0, len(positions), 5):
        group = positions[start:start + 5]

        for pos in group[:changes]:
            chars[pos] = "\u200c" if chars[pos] == "\u200b" else "\u200b"

    return "".join(chars)


secret = "Week 7 corruption test"
cover = "This is the Week 7 test message."

print("WEEK 7 FIVE-COPY RECOVERY TESTING")
print("=" * 45)

for corruption_level in [1, 2, 3]:
    encoded = embed_secret(
        cover, secret, recovery_mode=True, repetition_factor=5
    )
    corrupted = corrupt_group(encoded, corruption_level)

    try:
        recovered = extract_secret(corrupted)
        status = "PASS" if recovered == secret else "FAIL"
    except Exception:
        recovered = "Decode failed"
        status = "FAIL"

    print(f"\nCorrupted symbols per group: {corruption_level}/5")
    print(f"Expected: {secret}")
    print(f"Recovered: {recovered}")
    print(f"Result: {status}")