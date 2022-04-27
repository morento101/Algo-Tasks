"""Module with task 555"""

from math import factorial as fac

from tasks.utils import is_natural_number


def task555(num: int) -> list:
    """ Build pascal's triangle
    with n floors
    """
    assert is_natural_number(num), "The number should be natural"
    return [[int((fac(num) / (fac(k) * fac(num - k)))) for k in range(0, num + 1)] for num in range(0, num)]
