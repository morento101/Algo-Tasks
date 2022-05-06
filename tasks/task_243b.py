"""Implementation of task 243b"""

from tasks.task_243a import _is_prime, find_pairs, check_possibility, validate_number


def check_pair(number: int) -> dict:
    """Function for finding (x,y) for tasks 243a/b where x>y"""

    my_dict = find_pairs(number)
    result_dict = {}
    for i in my_dict.items():
        if int(i[0]) >= int(i[1]):
            result_dict[i[0]] = i[1]
    return result_dict


def task_243b(number: int) -> list:
    """
    Find all pairs(x,y), which match the expression
    x^2 + y^2 = number, where x > y
    """

    assert validate_number(number), "Wrong argument, must be natural integer"
    if _is_prime(number) and check_possibility(number):
        result_lst = []
        for i in check_pair(number).items():
            result_lst.append(i)
        return result_lst
    else:
        return []


task_243b.info = __doc__
