"""86a. Given a natural number n, find digits count of the number n."""

from tasks.utils import is_natural_number


def task_86a(number: int) -> int:
    """Get digits length in the number."""
    assert is_natural_number(number), "The number should be natural"
    return len(str(number))


task_86a.info = __doc__

if __name__ == "__main__":
    NUMBER = 13456
    print(task_86a(NUMBER))
