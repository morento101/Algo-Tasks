"""This module contains realisation of task 182."""

from tasks.utils import (is_natural_number,
                    has_int_in_list)


def task_182(*args: list) -> tuple:
    """Returns amount and sum of elements
    which are divisible by 5 and not divisible by 7.
    """
    assert has_int_in_list(args), "The list should have integer elements"

    amount = 0
    sum_res = 0

    for i in range(0, len(args)):
        if args[i] % 5 == 0 and args[i] % 7 != 0:
            amount += 1
            sum_res += args[i]

    return amount, sum_res
