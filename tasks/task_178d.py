"""Module with task 178d"""

from math import factorial as fac
from tasks.utils import is_natural_number


def task_178d(*arr: tuple) -> int:
    """ Return number that satisfy a following condition:
    2**k< ak < k!
    """
    # assert is_natural_number(num), "The number should be natural"
    count = 0
    for elem in range(len(arr)):
        if arr[elem] > 2**elem and arr[elem] < fac(elem):
            count += 1
    return count
