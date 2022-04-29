"""Module with task 178d"""

from tasks.utils import is_natural_number


def task178g(num: int, arr: list) -> int:
    """ Return number that satisfy a following condition:
    l[elem] < (l[elem + 1] + l[elem - 1]) / 2:
    """
    assert is_natural_number(num), "The number should be natural"
    count = 0
    for elem in range(1, num - 1):
        if arr[elem] < (arr[elem + 1] + arr[elem - 1]) / 2:
            count += 1
    return count
