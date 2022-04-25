"""
332 Given natural number, find four not negative numbers which match
expression: number = x**2 + y**2 + z**2 + t**2
"""


def task_332(number: int) -> tuple:
    """
    Find four numbers which match expression:
    number = x**2 + y**2 + z**2 + t**2
    """

    assert isinstance(number, int), "Wrong parameter type, must be natural int"
    assert number > 0, "Wrong parameter value, must be natural int"
    sqr = int(number ** 0.5) + 1

    for x_val in range(sqr):
        for y_val in range(sqr):
            for z_val in range(sqr):
                for t_val in range(sqr):
                    if x_val*x_val + y_val*y_val + z_val*z_val + t_val*t_val\
                            == number:
                        return x_val, y_val, z_val, t_val
