""" clock inverter"""

def lambda_handler(event, _):
    clock = event['clock']

    return {
        'output': [
            0 if clock[0] else 1,
            0 if clock[1] else 1,
        ] 
    }
