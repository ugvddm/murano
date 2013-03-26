import types

def transform_json(json, mappings):
    if isinstance(json, types.ListType):
        return [transform_json(t, mappings) for t in json]

    if isinstance(json, types.DictionaryType):
        result = {}
        for key, value in json.items():
            result[transform_json(key, mappings)] = \
                transform_json(value, mappings)
        return result

    if isinstance(json, types.StringTypes) and json.startswith('$'):
        value = mappings.get(json[1:])
        if value is not None:
            return value

    return json


def merge_dicts(dict1, dict2, max_levels=0):
    result = {}
    for key, value in dict1.items():
        result[key] = value
        if key in dict2:
            other_value = dict2[key]
            if max_levels == 1 or not isinstance(
                    other_value, types.DictionaryType):
                result[key] = other_value
            else:
                result[key] = merge_dicts(
                    value, other_value,
                    0 if max_levels == 0 else max_levels - 1)
    for key, value in dict2.items():
        if key not in result:
            result[key] = value
    return result


def find(f, seq):
    """Return first item in sequence where f(item) == True."""
    index = 0
    for item in seq:
        if f(item):
            return item, index
        index += 1
    return None, -1


def generate(length):
    return ''.join(choice(chars) for _ in range(length))
