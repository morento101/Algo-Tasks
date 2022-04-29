""""Task 178b, given sequece of numbers.
Count numbers, which are multiples of three but not multiples of five
"""

from typing import Sequence


def task_178b(numbers: Sequence[int]) -> int:
    """Return amount of numbers from sequence which are 
    multiples of three but not multiples of five
    """
    assert type(numbers) in (tuple, set, list), "Please, sequence must be tuple, set or list"
    count = 0

    for number in numbers:
        if not number % 3 and number % 5:
            count += 1

    return count
