"""Module with task 555"""

from math import factorial as fac


def task555(num: int) -> list:
    """ Build pascal's triangle
    with n floors
    """
    if not isinstance(num, int):
        raise TypeError("Argument should be integer!")
    if num <= 0:
        raise ValueError("Argument is not natural number!")
    return [[int((fac(num) / (fac(k) * fac(num - k)))) for k in range(0, num + 1)] for num in range(0, num)]


