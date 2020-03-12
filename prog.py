""" hello world, prints out the ram """

import base64

BITS = 64
DWORD = 8

LDA=0x01 << (BITS-8)
ADD=0x02 << (BITS-8)
OUT=0x0e << (BITS-8)

PROJ = [
    LDA | 14,  # LDA 14
    ADD | 15,  # ADD 15
    OUT,       # OUT
]

OUTPUT = bytes()

def write_program(proj):
    output = bytes()
    for inst in PROJ:
        output += inst.to_bytes(8, 'little')
    return output

def write_int(mem, idx, num):
    offset = idx * 8
    data = num.to_bytes(DWORD, 'little')
    mem = bytearray(mem)
    for i, val in enumerate(data):
        mem[offset + i] = val
    return mem

def expand_ram(ram, size):
    return ram + bytes([0] * size)

OUTPUT = write_program(PROJ)
OUTPUT = expand_ram(OUTPUT, int((16 - len(OUTPUT)/DWORD) * DWORD))
OUTPUT = write_int(OUTPUT, 14, 28)
OUTPUT = write_int(OUTPUT, 15, 14)

print(base64.b64encode(OUTPUT).decode())
