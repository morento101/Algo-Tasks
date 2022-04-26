"""
331 Given a natural number, represent it in the sum of three squares.
Return 1 represantation, if possible.
"""

from utils import is_natural_number
from math import sqrt, ceil

def square_sum_equals(x: int, y: int, z: int, number: int) -> bool:
    """Return True if x^2 + y^2 + z^2 == number"""
    return x ** 2 + y ** 2 + z ** 2 == number

def task_108(number: int) -> list[tuple]:
    """Return a represantation of a *num* as a sum of
        three squared numbers, if possible. Or return
        an empty list.
    """
    assert is_natural_number(number), "Wrong argument, must be natural integer"
    square_root_of_num = ceil(sqrt(number))
    result = []
    for x in range(1, square_root_of_num):
        for y in range(1, square_root_of_num):
            for z in range(1, square_root_of_num):
                if square_sum_equals(x, y, z, number):
                    result.append((x, y, z))
                    return result
