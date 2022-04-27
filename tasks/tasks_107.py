"""Implementation of task 107"""
from math import log


def validate_number(number: int) -> bool:
    """Function for validating number"""

    if isinstance(number, int) and number > 1:
        return True
    else:
        return False


def task_107(number: int) -> int:
    """Find max k, which match the expression 4^k < number"""

    assert validate_number(number), "Wrong argument, must be natural integer"
    print(int(log(number-1, 4)))
    return int(log(number-1, 4))