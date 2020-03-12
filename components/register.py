""" simple register """

def lambda_handler(event, _):
    state = int(event['state'], 0)

    clock = event['clock'] 
    load = event['load'] 
    enable = event['enable'] 
    din = int(event['input'], 0)

    if load and rising_clock(clock):
        state = din

    state = hex(state)
    output = None
    if enable:
        output = state

    return {
        'state': state,
        'output': output,
    }


def rising_clock(clock):
    return tuple(clock) == (0, 1)
