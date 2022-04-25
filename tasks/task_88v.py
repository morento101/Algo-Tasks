"""88(v) Given natural number, swap first and last digit of a number"""


def task_88v(number: int) -> int:
    """
    Returns integer with first and last digits swapped
    """

    assert isinstance(number, int), "Wrong parameter type, must be natural int"
    assert number > 0, "Wrong parameter value, must be natural int"
    number = str(number)

    return int(number) if len(number) == 1 else\
        int(number[-1] + number[1:-1] + number[0])
