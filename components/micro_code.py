""" rom that contains micro-code """

ROM_SIZE=4096

OPS = {
    # LDA
    0x12: 0x4800,
    0x13: 0x1200,

    # ADD
    0x22: 0x4800,
    0x23: 0x1020,
    0x24: 0x0280,

    # SUB
    0x32: 0x4800,
    0x33: 0x1020,
    0x34: 0x02c0,

    # STA
    0x42: 0x4800,
    0x43: 0x2100,

    # JMP
    0x52: 0x4800,
    0x53: 0x1002,

    # OUT
    0xe2: 0x0110,
    0xe3: 0x8000,
}

def program_rom(data, size):

    rom = list([0] * size)
    for i in range(0, size, 16):
        rom[i] = 0x4004
        rom[i+1] = 0x1408
        rom[i+2] = 0x8000

    for i, val in data.items():
        rom[i] = val

    return rom

ROM = program_rom(OPS, ROM_SIZE)

def lambda_handler(event, _):
    op = int(event['op'], 0)
    ic_count = int(event['ic_count'], 0)

    upper_word = op >> 64 - 12
    index = upper_word | ic_count
    return {
        'op': event['op'],
        'ic_count': event['ic_count'],
        'upper_word': hex(upper_word),
        'index': hex(index),
        'control': to_control_state(ROM[index]),
    }


def to_control_state(inst):
    word = inst.to_bytes(2, 'big')
    return {
        "halt": bool(word[0] & 0x80),
        "addrin": bool(word[0] & 0x40),
        "min": bool(word[0] & 0x20),
        "mout": bool(word[0] & 0x10),
        "irout": bool(word[0] & 0x08),
        "irin": bool(word[0] & 0x04),
        "ain": bool(word[0] & 0x02),
        "aout": bool(word[0] & 0x01),
        "eo": bool(word[1] & 0x80),
        "subtract": bool(word[1] & 0x40),
        "bin": bool(word[1] & 0x20),
        "outin": bool(word[1] & 0x10),
        "count_enable": bool(word[1] & 0x08),
        "counter_out": bool(word[1] & 0x04),
        "jump": bool(word[1] & 0x02)
    }
