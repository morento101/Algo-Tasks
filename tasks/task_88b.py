"""This module contains realisation of task 88b."""

from utils import is_natural_number


def reverse_number(number: int) -> int:
    """Returns reversed number"""
    assert is_natural_number(number), "The number should be natural"

    return int(str(number)[::-1])


def task_88b(number: int) -> int:
    """Implementation of the task #88b.
    Returns reversed number
    """
    return reverse_number(number)
