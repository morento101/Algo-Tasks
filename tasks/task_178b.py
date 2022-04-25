""""Module with task 178b"""
from typing import Sequence


def task_178b(numbers: Sequence[int]) -> int:
    """
    Return amount of numbers from sequence which are 
    multiples of three but not multiples of five
    """
    count = 0

    for number in numbers:
        if not number % 3 and number % 5:
            count += 1

    return count
    