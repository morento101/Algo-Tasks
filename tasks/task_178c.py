"""178c. Given a sequence of numbers, 
count those numbers, which are squares of multiples of two.
"""


def task_178c(*numbers: tuple[int]) -> int:
    """Return count of numbers from sequence which are
    squares of multiples of two
    """
    assert numbers, "Type valid sequence of numbers"

    count = 0

    for number in numbers:
        assert isinstance(number, int), "Numbers in sequene must be int"
        assert number >= 0, f"Can't calculate square root from negative number {number}"
        number_root = number ** .5
        if not (number_root % 1) and not (number_root % 2):
            count += 1

    return count

task_178c.info = __doc__
