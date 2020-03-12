""" counter """

def lambda_handler(event, _):
    clock = event['clock']
    counter_out = event['counter_out']
    reset = event['reset']
    jump = event['jump']
    count_enabled = event['count_enable']
    din = int(event['input'], 0)

    state = int(event['state'], 0)
    output = None

    if jump and rising_clock(clock):
        state = din

    if count_enabled and rising_clock(clock):
        state += 1

    if reset and rising_clock(clock):
        state = 0

    state = hex(state)
    if counter_out:
        output = state

    return {
        'state': state,
        'output': output
    }

def rising_clock(clock):
    return tuple(clock) == (0, 1)
