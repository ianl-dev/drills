def flatten(*args):
    """
    # list
    # range -> list
    # other types (string / numbers)
    
    # logic
    # inputs is an args tuple
    """
    result = []
    
    # Prevent overflow
    elements = args[0] if len(args) == 1 else args
        
    for elem in elements:
        try:
            n = len(elem)
            # Tuple, list, iterable, range
            if n != 0 and not isinstance(elem, str):
                next_input = list(elem)
                result.extend(flatten(next_input))
            else:
                result.append(elem)
        # Primitive type
        except:
            result.append(elem)
    return result

#  My test cases
print(flatten('Hello', range(3), [5,6,7]))
print(flatten('Hello', 2, [[3, 4, 5], [6, 7, [8,2]]], 9))


# yield -> primitive 
# yield from (python 3) -> nested list
# list(flatten())

# queue: first element will be at the end of my queue (append), out of order
# stack: first element will be in order (processed in the same way we wanted)

# def flatten(*args):
#     # Please Implement function
#     # list
#     # range -> list
#     # other types (string / numbers)
    
#     # logic
#     # inputs is an args tuple
    
#     result = []
    
#     # Prevent overflow
#     elements = args[0] if len(args) == 1 else args
        
#     for elem in elements: # int
#         if isinstance(elem, list) or isinstance(elem, tuple):
#             # Only recurse on non-empty list
#             if elem:
#                 result.extend(flatten(elem))
#         elif isinstance(elem, range):
#             result.extend(list(elem))
#         # String or int or other primitive types
#         else:
#             result.append(elem)
#     return result

# My test cases


# def test_flatten():
#     truth = ['Hello', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     result = list(flatten('Hello', range(3), [(3, 4, 5), [6, 7, 8]], 9))
#     assert truth == result
 
# test_flatten()