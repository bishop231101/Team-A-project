# Week 3 Codec Format (Draft v1)

## Character mapping

| Meaning | Unicode character |
| --- | --- |
| Bit `0` | `U+200B` ZERO WIDTH SPACE |
| Bit `1` | `U+200C` ZERO WIDTH NON-JOINER |
| Byte separator | `U+200D` ZERO WIDTH JOINER |

## Frame

The prototype encodes the following binary frame before appending it to the
cover text:

```text
magic (4 bytes: ZWS1) | UTF-8 payload length (4 bytes) | UTF-8 payload | CRC-32 (4 bytes)
```

Each byte is converted to eight bits and mapped to zero-width characters. A
`U+200D` separator appears between adjacent byte blocks. The decoder checks the
magic value, declared length, checksum, and UTF-8 decoding before returning a
secret. Any validation failure must return a clear error, not partial text.

## Week 3 limitations

This is a local baseline, not an error-correction implementation. It appends
the payload to the cover text and assumes the cover text does not already use
the three project zero-width characters. Platform robustness and redundancy are
scheduled for later weeks.
