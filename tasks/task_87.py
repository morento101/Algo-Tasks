"""87. Given a natural n, m. Get the sum of m last digits of the number n."""


def task_87(target: int, tail_size: int) -> int:
    """Return sum of m last digits in number n."""
    if tail_size == 1:
        # Return last digit
        return target % 10
    else:
        # Return the sum of the right digit and the result of the recursion for the other digits of the number
        tail_size -= 1
        return target % 10 + task_87(target // 10, tail_size)
