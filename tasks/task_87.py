"""87. Given a natural n, m. Get the sum of m last digits of the number n."""


def get_sum_of_lasts_few(target: int, tail_size: int) -> int:
    """
    Returns sum of m last digits in number n.
    """
    if tail_size == 1:
        # Return last digit
        return target % 10
    else:
        # Return the sum of the right digit and the result of the recursion for the other digits of the number
        tail_size -= 1
        return target % 10 + get_sum_of_lasts_few(target // 10, tail_size)


def info() -> str:
    """
    Task & arguments description.
    """
    info_string = "Task 87. Function returns sum of m last digits in number n.\n" \
                  "Please enter n, m separated by space (or 'R' to return to main menu):"

    return info_string


def task_87(n, m) -> int:
    """
    Implementation of the task #87.
    """

    return get_sum_of_lasts_few(n, m)
