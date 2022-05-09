"""88b. Given a natural number n,
print the given number in reverse.
"""

from tasks.utils import is_natural_number


def reverse_number(number: int) -> int:
    """Return reversed number"""
    assert is_natural_number(number), "The number should be natural"

    return int(str(number)[::-1])


def task_88b(number: int) -> int:
    """Implementation of the task No. 88b.
    Return reversed number
    """
    return reverse_number(number)


task_88b.info = __doc__
