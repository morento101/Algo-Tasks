"""Task 322, requires no input data. 
It finds number with largest sum of divisors within range 1, 10000.
"""

from tasks.utils import is_natural_number


def get_number_with_largest_sum_of_divisors(start: int, end: int) -> int:
    """Returns number with the largest sum of divisors within range (start, end)"""
    assert is_natural_number(start), "start should be natural numbers"
    assert is_natural_number(end), "end should be natural numbers"
    assert end >= start, "End point should be greater than start"
    
    # List of all sums of divisors
    sums = [sum(get_divisors_list(number)) for number in range(start, end)]
    # Get the largest sum in list
    max_sum = max(sums)

    # Get number with the largest sum of divisors
    # Works, while a = 1, b => a
    number_with_max_sum = sums.index(max_sum) + 1

    return number_with_max_sum


def get_divisors_list(number: int) -> list:
    """Returns list of number divisors"""
    assert is_natural_number(number), "The number should be natural"

    return [i for i in range(1, int(number/2) + 1) if number % i == 0] \
                                                            + [number]


def task_322() -> int:
    """Implementation of the task #322.
    Returns number with the largest sum of divisors from 1 to 10000
    """
    # Set boundaries
    start = 1
    end = 10000

    return get_number_with_largest_sum_of_divisors(start, end)


task_322.info = __doc__
