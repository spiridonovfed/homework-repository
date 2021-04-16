from homework2.hw4 import cache


def test_positive_case1():
    """Testing example from the task"""

    def func(a, b):
        return (a ** b) ** 2

    cache_func = cache(func)

    some = 100, 200

    val_1 = cache_func(*some)
    val_2 = cache_func(*some)

    assert val_1 is val_2


def test_negative_case1():
    """Testing example from the task, but without caching"""

    def func(a, b):
        return (a ** b) ** 2

    some = 100, 200

    val_1 = func(*some)
    val_2 = func(*some)

    assert not val_1 is val_2


def test_positive_case2():
    """Testing recursive method of finding 100th Fibonacci number - not possible without caching"""

    def fib(n):
        if n in (0, 1):
            return 1
        return fib(n - 1) + fib(n - 2)

    fib = cache(fib)
    assert fib(100)
