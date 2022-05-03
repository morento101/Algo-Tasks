"""Implementation of task 243a"""
from task_107 import validate_number


def _is_prime(number: int) -> bool:
    """Function for checking is number prime"""

    if number == 2 or number == 3:
        return True
    elif number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def check_possibility(number: int) -> bool:
    """Function for checking possibility solving tasks 243a/b"""

    return number % 4 == 1


def find_pairs(number: int, one_already=False) -> dict:
    """Function for finding (x,y) for tasks 243a/b"""

    result_dict = {}
    for x in range(1, int((number - 1) ** 0.5) + 1):
        for y in range(1, int((number - 1) ** 0.5) + 1):
            if x**2 + y**2 == number:
                result_dict[x] = y
                if one_already:
                    return result_dict
    return result_dict


def task_243a(number: int) -> dict:
    """Find pair(x,y), which match the expression x^2 + y^2 = number"""

    assert validate_number(number), "Wrong argument, must be natural integer"
    if _is_prime(number) and check_possibility(number):
        return find_pairs(number, True)
    else:
        return {}
