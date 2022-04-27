"""Module with task 178d"""


def task178g(num: int, arr: list) -> int:
    """ Return number that satisfy a following condition:
    l[elem] < (l[elem + 1] + l[elem - 1]) / 2:
    """
    if not isinstance(num, int):
        raise TypeError("Argument should be integer!")
    if num <= 0:
        raise ValueError("Argument is not natural number!")
    count = 0
    for elem in range(1, num - 1):
        if arr[elem] < (arr[elem + 1] + arr[elem - 1]) / 2:
            count += 1
    return count
