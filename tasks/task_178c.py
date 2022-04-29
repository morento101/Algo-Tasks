"""Task 178c, given sequence of numbers. 
Count numbers which are squares of multiples of two.
"""

from typing import Sequence


def task_178c(numbers: Sequence[int]) -> int:
    """Returns count of numbers from sequence which are
    squares of multiples of two
    """
    assert type(numbers) in (tuple, set, list), "Please, sequence must be tuple, set or list"
    count = 0

    for number in numbers:
        assert isinstance(number, int), "Numbers in sequene must be int or float"
        assert number >= 0, f"Can't calculate square root from negative number {number}"
        number_root = number ** .5
        if not (number_root % 1) and not (number_root % 2):
            count += 1

    return count
