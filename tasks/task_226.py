"""226. Given natural numbers m, n. Get all natural common multiples, smaller m*n."""


def get_natural_common_multiples(first_arg: int, second_arg: int) -> list[int]:
    """
    Returns all natural common multiples of first_arg & second_arg less than first_arg * second_arg
    """
    limit = first_arg * second_arg
    suspect = second_arg
    result = []
    while suspect < limit:
        # Check whether the increment of the second number is divisible by the first
        if suspect % first_arg == 0:
            result.append(suspect)
        suspect += second_arg

    return result


def info() -> str:
    """
    Task & arguments description
    """
    info_string = ("Task 226. Function returns all natural common multiples of n & m less than n*m.\n"
                   "Please enter n, m separated by space (or 'R' to return to main menu): "
                   )

    return info_string


def run(n, m) -> list[int]:
    """
    Implementation of the task #226.
    """

    return get_natural_common_multiples(n, m)
