"""Module with task 178d"""

from math import factorial as fac

from tasks.utils import is_natural_number


def task_178d(num: int, arr: list) -> int:
    """ Return number that satisfy a following condition:
    2**k< ak < k!
    """
     assert is_natural_number(num), "The number should be natural"
    count = 0
    for elem in range(num):
        if arr[elem] > 2**elem and arr[elem] < fac(elem):
            count += 1
    return count
