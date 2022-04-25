"""This module provides function to get digits length in the number."""


def is_natural_number(number: int) -> bool:
    """
    Returns True if the number is natural.
    """
    return isinstance(number, int) and number > 0


def task_86a(number: int) -> int:
    """
    Get digits length in the number.
    """
    assert is_natural_number(number), "The number should be natural"
    return len(str(number))


if __name__ == "__main__":
    NUMBER = 13456
    print(task_86a(NUMBER))
