import struct


def dump_str(s: str) -> bytes:
    b = s.encode('utf-8')
    r = b''
    l = len(b)
    while True:
        if l < 128:
            r += struct.pack('<B', l)
            break
        else:
            r += struct.pack('<B', l % 128 + 128)
            l //= 128
    return r + b


def read_str(file) -> str:
    l = 0
    for i in range(9):
        n, = struct.unpack('<B', file.read(1))
        l += n % 128 * 128 ** i
        if n < 128:
            return file.read(l).decode('utf-8')
