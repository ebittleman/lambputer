""" simple alu """

def lambda_handler(event, _):
    enable = event['enable']
    subtract = event['subtract']

    a_state = int(event['a_state'], 0)
    b_state = int(event['b_state'], 0)

    result = a_state - b_state if subtract else a_state + b_state
    carry_out = result > 255 or result < 0
    result = hex(result)

    output = None
    if enable:
        output = result

    return {
        'result': result,
        'carry_out': carry_out,
        'output': output
    }
