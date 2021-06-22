"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""


def after_backspace(text):
    """Imitates backspace"""
    result = []
    for symbol in text:
        if symbol != "#":
            result.append(symbol)
        elif result:
            result.pop()
    return result


def backspace_compare(first: str, second: str):
    return after_backspace(first) == after_backspace(second)
