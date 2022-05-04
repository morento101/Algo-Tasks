"""Module with task 178d"""

from math import factorial as fac
from tasks.utils import has_int_in_list


def task_178d(*arr: tuple) -> int:
    """ Return number that satisfy a following condition:
    2**k< ak < k!
    """
    assert has_int_in_list(arr), "The number should be natural"

    count = 0
    for elem in range(len(arr)):
        if arr[elem] > 2**elem and arr[elem] < fac(elem):
            count += 1
    return count
