""""Task 178b, given sequece of numbers.
Count numbers, which are multiples of three but not multiples of five
"""

from typing import Sequence


def task_178b(numbers: Sequence[int]) -> int:
    """Return amount of numbers from sequence which are 
    multiples of three but not multiples of five
    """
    assert isinstance(numbers, (tuple, set, list), "Sequence must be tuple, set or list"
    count = 0

    for number in numbers:
        assert isinstance(number, int), "Numbers in sequene must be int"
        if not number % 3 and number % 5:
            count += 1

    return count
