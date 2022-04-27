"""This module with help functions."""


def is_natural_number(number: int) -> bool:
    """Returns True if the number is natural."""
    return isinstance(number, int) and number >= 0
