"""323. Given a natural number n, 
get all natural numbers less than n and relatively prime to it.
"""

from tasks.utils import is_natural_number


def task_323(number: int) -> list:
    """Return all natural numbers less than n and coprime with it."""
    assert is_natural_number(number), "The number should be natural"

    tmp = number - 1
    array = []
    while tmp != 0:
        for i in range(tmp, 0, -1):
            tmp1 = tmp
            tmp2 = i
            while tmp2 != 0 and tmp1 != 0:
                if tmp2 > tmp1:
                    tmp2 = tmp2 % tmp1
                else:
                    tmp1 = tmp1 % tmp2

            if tmp2 + tmp1 == 1:
                array.append(str(tmp) + ' & ' + str(i))
        tmp -= 1

    return array

task_323.info = __doc__
