"""88g. Given a natural number, 
add 1 to the end and start of the number.
"""

from tasks.utils import is_natural_number


def task_88g(number: int) -> int:
    """Return integer with '1' at the start and the end of a number"""
    assert is_natural_number(number), "Wrong argument, must be natural integer"
    number = str(number)

    return int("1" + number + "1")


task_88g.info = __doc__
