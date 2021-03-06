"""554. Given a number n.
Return all pythagorean triples where a <= b <= c <= n.
"""

from typing import List


def task_554(number: int) -> List[tuple]:
    """Return list of tuples with all pythagorean triples which satisfy
    following equations: a^2 + b^2 = c^2 and a <= b <= c <= n
    """
    assert isinstance(number, int), "Number can be only int type"

    res = []
    domain = range(1, number+1)
    n_square = number ** 2

    for a in domain:
        for b in domain:
            c = a**2 + b**2
            if c <= n_square:
                if not c**.5 % 1:
                    res.append((a, b, int(c**.5)))

    return res


task_554.info = __doc__
