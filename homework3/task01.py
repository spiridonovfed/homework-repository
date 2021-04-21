"""In previous homework task 4, you wrote a cache function that remembers other function output value.
Modify it to be a parametrized decorator, so that the following code::

    @cache(times=3)
    def some_function():
        pass


Would give out cached value up to `times` number only.
Example::

    @cache(times=2)
    def f():
        return input('? ')   # careful with input() in python2, use raw_input() instead

    # >>> f()
    # ? 1
    # '1'
    # >>> f()     # will remember previous value
    # '1'
    # >>> f()     # but use it up to two times only
    # '1'
    # >>> f()
    # ? 2
    # '2'
"""


def cache(times):
    def the_real_decorator(function):
        def wrapper(*args):
            nonlocal times
            if args in memory and times:
                times -= 1
                return memory[args]
            result = memory[args] = function(*args)
            return result

        memory = {}
        return wrapper

    return the_real_decorator


@cache(times=2)
def f():
    return input("? ")
