"""This module contains realisation of task 88a."""

from .utils import is_natural_number


def is_3_in_square_of_number(number: int) -> bool:
    """Returns True if 3 is in square of number"""
    assert is_natural_number(number), "The number should be natural"

    return '3' in str(number*number)


def task_88a(number: int) -> bool:
    """Implementation of the task #88a.
    Returns true if square of number contains 3
    """
    return is_3_in_square_of_number(number)
