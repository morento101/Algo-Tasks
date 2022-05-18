"""178g. Given a sequece of numbers,
count numbers, which satisfy a following condition:
l[elem] < (l[elem + 1] + l[elem - 1]) / 2
"""

from tasks.utils import has_int_in_list


def task_178g(*arr: tuple) -> int:
    """Return number that satisfy a following condition:
    l[elem] < (l[elem + 1] + l[elem - 1]) / 2:
    """
    assert has_int_in_list(arr), "The number should be natural"
    count = 0
    for elem in range(1, len(arr) - 1):
        if arr[elem] < (arr[elem + 1] + arr[elem - 1]) / 2:
            count += 1
    return count


task_178g.info = __doc__
