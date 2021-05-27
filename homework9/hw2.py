"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

# >>> with supressor(IndexError):
# ...    [][2]

"""
from contextlib import contextmanager


class Suppressor:
    """Context manager as a class to suppress exceptions passed.

    :param *exceptions: a sequence of Exceptions to suppress
    :type *exceptions: list, tuple
    """

    def __init__(self, *exceptions):
        self._exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type is not None and issubclass(exc_type, self._exceptions)


@contextmanager
def suppressor(*exceptions):
    """Context manager as a generator to suppress exceptions passed.

    :param *exceptions: a sequence of Exceptions to suppress
    :type *exceptions: list, tuple
    """
    try:
        yield
    except exceptions:
        pass
