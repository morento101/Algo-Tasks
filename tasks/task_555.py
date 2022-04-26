"""Module with task 555"""
from math import factorial as fac


def task555(n: int) -> list:
    """
    Build pascal's triangle with n floors
    """
    if not isinstance(n, int):
        raise TypeError("Argument should be integer!")
    if n <= 0:
        raise ValueError("Argument is not natural number!")

    return [[int((fac(n) / (fac(k) * fac(n - k)))) for k in range(0, n + 1)] for n in range(0, n)]


