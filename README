# Poly1305 Implementation (RFC 8439)
Usage:
  ./poly1305-gen <key_hex> <file>
  ./poly1305-check <key_hex> <file> <tag_hex>

Files:
- poly1305.py: Core logic implementation.
- poly1305-gen: CLI tool to generate an authenticator tag.
- poly1305-check: CLI tool to verify an authenticator tag.
- Makefile: Helper to set executable permissions.

RUnning:
1. Run `make`
2. Generate a tag:
   ./poly1305-gen <64-char-hex-key> <filename>
3. Verify a tag:
   ./poly1305-check <64-char-hex-key> <filename> <32-char-hex-tag>

Testing CASE:
--------------------------------
```bash
make
KEY="85d6be7857556d337f4452fe42d506a80103808afb0db2fd4abff6af4149f51b"
./poly1305-gen $KEY message.txt
TAG="a8061dc1305136c6c22b8baf0c0127a9"
./poly1305-check $KEY message.txt $TAG
```

Key: 85d6be7857556d337f4452fe42d506a80103808afb0db2fd4abff6af4149f51b

Message: "Cryptographic Forum Research Group"

Expected Tag: a8061dc1305136c6c22b8baf0c0127a9