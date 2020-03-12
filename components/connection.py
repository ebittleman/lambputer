""" connections components """

def lambda_handler(event, _):
    passthrough = event['pass']
    value = event['input']
    if value is None:
        return passthrough

    din = int(value, 0)
    connections = event['connections']
    result = {}
    for hex_mask, addr in connections.items():
        mask = int(hex_mask, 0)
        dout = din & mask
        result = set_addr(result, addr, hex(dout))

    return _merge_dictionaries(passthrough, result)

def set_addr(result, addr, value):
    path = addr.split('.')
    cursor = result
    for i in path[:-1]:
        cursor = cursor.setdefault(i, {})

    cursor[path[-1:][0]] = value
    return result

def _merge_dictionaries(dict1, dict2):
    """
    Recursive merge dictionaries.

    :param dict1: Base dictionary to merge.
    :param dict2: Dictionary to merge on top of base dictionary.
    :return: Merged dictionary
    """
    for key, val in dict1.items():
        if isinstance(val, dict):
            dict2_node = dict2.setdefault(key, {})
            _merge_dictionaries(val, dict2_node)
        else:
            if key not in dict2:
                dict2[key] = val

    return dict2
