"""Module with task 178d"""

from math import factorial as fac


def task178d(n: int, arr: list) -> int:
    """ Return number that satisfy a following condition:
    2**k< ak < k!
    """
    if not isinstance(n, int):
        raise TypeError("Argument should be integer!")
    if n <= 0:
        raise ValueError("Argument is not natural number!")
    c = 0
    for elem in range(n):
        if arr[elem] > 2**elem and arr[elem] < fac(elem):
            c += 1
    return c
