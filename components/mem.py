""" memory chip """

import base64

DWORD = 8

def lambda_handler(event, _):
    clock = event["clock"]
    load = event["load"]
    enable = event["enable"]
    addr = int(event["addr"], 0)
    din = int(event['input'], 0).to_bytes(DWORD, 'little')
    state = base64.b64decode(event["state"].encode())

    dout = None
    start = addr * DWORD
    if enable:
        dout = hex(int.from_bytes(state[start:start+DWORD], 'little'))

    if load and rising_clock(clock):
        state = bytearray(state)
        for i, val in enumerate(din):
            state[start+i] = val

    return {
        'state': base64.b64encode(state).decode(),
        'output': dout
    }

def rising_clock(clock):
    return tuple(clock) == (0, 1)
