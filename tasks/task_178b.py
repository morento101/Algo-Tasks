""""Task 178b, given sequece of numbers.
Count numbers, which are multiples of three but not multiples of five
"""

from typing import Sequence
from utils import is_natural_number


def task_178b(numbers: Sequence[int]) -> int:
    """Return amount of numbers from sequence which are 
    multiples of three but not multiples of five
    """

    count = 0

    for number in numbers:
        assert is_natural_number(number)
        if not number % 3 and number % 5:
            count += 1

    return count
