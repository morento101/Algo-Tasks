"""Module with task 178b."""

from typing import Sequence


def task_178c(numbers: Sequence[int]) -> int:
    """Returns count of numbers from sequence which are
    squares of multiples of two
    """
    count = 0

    for number in numbers:
        assert number >= 0, f"Can't calculate square root from negative number {number}"
        number_root = number ** .5
        if not (number_root % 1) and not (number_root % 2):
            count += 1

    return count
