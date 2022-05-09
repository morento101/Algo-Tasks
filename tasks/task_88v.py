"""88v. Given a natural number, 
swap first and last digits of a number.
"""

from tasks.utils import is_natural_number


def task_88v(number: int) -> int:
    """Return integer with first and last digits swapped"""
    assert is_natural_number(number), "Wrong argument, must be natural integer"
    number = str(number)

    return int(number) if len(number) == 1 else\
        int(number[-1] + number[1:-1] + number[0])


task_88v.info = __doc__
