""""178b. Given a sequece of numbers,
count those numbers, which are multiples of three, 
but not multiples of five.
"""


def task_178b(*numbers: tuple[int]) -> int:
    """Return amount of numbers from sequence which are 
    multiples of three but not multiples of five
    """
    assert numbers, "Type valid sequence of numbers"

    count = 0

    for number in numbers:
        assert isinstance(number, int), "Numbers in sequene must be int"
        if not number % 3 and number % 5:
            count += 1

    return count


task_178b.info = __doc__
