"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""


def custom_range(inp, *args):
    """custom range function for any iterable of unique values"""
    # change first two args provided to corresponding indexes of iterable
    converted_args = []
    for num, arg in enumerate(args, 0):
        if num < 2:
            arg = inp.index(arg)
        converted_args.append(arg)
    converted_args = tuple(converted_args)

    # getting result with converted args
    result = [inp[i] for i in range(*converted_args)]
    return result


import string
print(string.ascii_letters)
