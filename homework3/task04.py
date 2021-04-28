"""
Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
https://en.wikipedia.org/wiki/Narcissistic_number

Examples:

- 9 is an Armstrong number, 9 = 9^1 = 9
- 10 is not: 10 != 1^2 + 0^2 = 1
- 153 is : 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153


Write a function that detects if a number is Armstrong number in functionaly style:
 - use map or other utilities from functools library,
 - use anonymous functions (or use function as argument)
 - do not use loops, preferably using list comprehensions

### Example function signature and call
"""


def is_armstrong(number: int) -> bool:
    def number_to_iterable(number_as_int):
        return str(number_as_int)

    def digits_to_power(number_as_iterable):
        result = list(
            map(lambda x: int(x) ** len(number_as_iterable), number_as_iterable)
        )
        return result

    return (number >= 0) and (
        sum(digits_to_power(number_to_iterable(number))) == number
    )


# # Or more simple and cleaner option:
# def is_armstrong(number: int) -> bool:
#     number_as_iterable = str(number)
#     digits_to_the_power = [int(digit)**len(number_as_iterable) for digit in number_as_iterable]
#     if sum(digits_to_the_power) == number:
#         return True
#     else:
#         return False
