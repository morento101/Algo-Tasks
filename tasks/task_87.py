"""87. Given natural numbers n and m, 
get the sum of last m digits of the number n.
"""

from tasks.utils import is_natural_number


def task_87(target: int, tail_size: int) -> int:
    """Return sum of m last digits in number n."""
    assert is_natural_number(target), "The number should be natural"
    assert is_natural_number(tail_size), "The number should be natural"

    if tail_size == 1:
        return target % 10
    else:
        tail_size -= 1
        return target % 10 + task_87(target // 10, tail_size)


task_87.info = __doc__
