""" simple clock """

STATE = {
    (0, 0): (0, 1),
    (0, 1): (1, 1),
    (1, 1): (1, 0),
    (1, 0): (0, 0),
}

def lambda_handler(event, _):
    state = event['state']
    halt = event['halt']

    if halt:
        raise Exception('halt')

    return list(STATE[tuple(state)])
