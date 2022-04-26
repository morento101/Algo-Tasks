"""
332 Given natural number, find four not negative numbers which match
expression: number = x**2 + y**2 + z**2 + t**2
"""

from utils import is_natural_number


def task_332(number: int) -> tuple:
    """Find four numbers which match expression:
    number = x**2 + y**2 + z**2 + t**2
    """
    assert is_natural_number(number), "Wrong argument, must be natural integer"
    sqr = int(number ** 0.5) + 1

    for x_val in range(sqr):
        for y_val in range(sqr):
            for z_val in range(sqr):
                for t_val in range(sqr):
                    if x_val*x_val + y_val*y_val + z_val*z_val + t_val*t_val\
                            == number:
                        return x_val, y_val, z_val, t_val
