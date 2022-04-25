"""88(g) Given natural number, add 1 to the end and start of the number"""


def task_88g(number: int) -> int:
    """
    Returns integer with '1' at the start and the end of a number
    """

    assert isinstance(number, int), "Wrong parameter type, must be natural int"
    assert number > 0, "Wrong parameter value, must be natural int"
    number = str(number)

    return int("1" + number + "1")
