"""108. Given a natural number,
find the smallest possible number which matches 
pattern 2**r and is bigger than the given number.
"""

from tasks.utils import is_natural_number


def task_108(number: int) -> int:
    """Return the smallest possible number that matches
    pattern 2**r and is bigger than number
    """
    assert is_natural_number(number), "Wrong argument, must be natural integer"
    r = 1
    while True:
        if 2**r > number:
            return 2**r
        r += 1

task_108.info = __doc__
