"""88(g) Given natural number, add 1 to the end and start of the number"""


from utils import is_natural_number


def task_88g(number: int) -> int:
    """
    Returns integer with '1' at the start and the end of a number
    """

    assert is_natural_number(number), "Wrong argument, must be natural integer"
    number = str(number)

    return int("1" + number + "1")
