"""Module with task 178d"""


def task178g(n: int, arr: list) -> int:
    """
    Return number that satisfy a following condition:
    l[elem] < (l[elem + 1] + l[elem - 1]) / 2:
    """
    if not isinstance(n, int):
        raise TypeError("Argument should be integer!")
    if n <= 0:
        raise ValueError("Argument is not natural number!")
    c = 0
    for elem in range(1, n - 1):
        if arr[elem] < (arr[elem + 1] + arr[elem - 1]) / 2:
            c += 1
    return c
