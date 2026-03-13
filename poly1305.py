#!/usr/bin/env python3
def poly1305_mac(msg_bytes, key_bytes):
    if len(key_bytes) != 32: raise ValueError("Key must be 32 bytes long")
    r = int.from_bytes(key_bytes[:16], 'little')
    s = int.from_bytes(key_bytes[16:], 'little')
    r &= 0x0ffffffc0ffffffc0ffffffc0fffffff
    a, p = 0, (1 << 130) - 5

    for i in range(0, len(msg_bytes), 16):
        block = msg_bytes[i : i + 16]
        n = int.from_bytes(block + b'\x01', byteorder='little')
        a += n
        buffer = a * r
        low = buffer & ((1 << 130) - 1)
        high = buffer >> 130
        a = low + (high * 5)
        
    while a >= p:
        a -= p

    a += s
    return (a & ((1 << 128) - 1)).to_bytes(16, byteorder='little')
 