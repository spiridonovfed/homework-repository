"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.

That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...


Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions


# >>> fizzbuzz(5)
# ['1', '2', 'fizz', '4', 'buzz']

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    >>> fizzbuzz(3)
    ['1', '2', 'fizz']
    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    >>> fizzbuzz(10)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz']

    """
    fizzbuzz_numbers = []
    current_number = 1
    while len(fizzbuzz_numbers) != n:
        if current_number % 15 == 0:
            fizzbuzz_numbers.append("fizzbuzz")
        if current_number % 3 == 0:
            fizzbuzz_numbers.append("fizz")
        elif current_number % 5 == 0:
            fizzbuzz_numbers.append("buzz")
        else:
            fizzbuzz_numbers.append(f"{current_number}")
        current_number += 1
    return fizzbuzz_numbers


instruction = """
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <https://github.com/spiridonovfed/homework-repository>
 - Checkout branch <homework4>
 - Open terminal
 - Change directory to root folder of "homework-repository"
    cd homework-repository
 - Run a doctest inside 'task_4_doctest.py' file
    pytest --doctest-modules homework4/task_4_doctest.py
"""
