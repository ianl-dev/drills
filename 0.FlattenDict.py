def flatten_dictionary(dictionary):
    """
    Given a dictionary with nested dictionary, flatten it such that
    final dictionary:
    {
        'key1': value
        'key2.child1': other value
        'key2.child2': other values
    }
    where key2 has a dictionary as its key value
    """
    output = {}
    # Recursive case
    for key in dictionary:
        child = dictionary[key]
        # Only recurse when nested
        if isinstance(child, dict):
            child_output = flatten_dictionary(child)
            for child_key in child_output:
                val = child_output[child_key]
                if key == "":
                    output[child_key] = val
                elif child_key == "":
                    output[key] = val
                else:
                    new_key = str(key) + "." + child_key
                    output[new_key] = val
        # Non-nested (str)
        else:
            output[key] = child
    return output


    # Caveat: empty child key
inp = {
    "Key1": "1",
    "Key2": {
        "a": "2",
        "b": "3",
        "c": {
            "d": "3",
            "e": {
                "": "1"
            }
        }
    }
}

inp2 = {'a': 5, 'b': 10, 'c': None, '': None}
print(flatten_dictionary(inp))
