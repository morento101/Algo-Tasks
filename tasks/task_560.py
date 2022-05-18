"""560. Find all pairs of friendly numbers between 200 and 300.
Two natural numbers are called friendly if each of them is equal 
to the sum of all divisors of the other, except for this number itself.
"""

def task_560() -> list:
    """Return all pairs of friendly numbers between 200 and 300."""
    tmp = 0
    array = []
    for k in range(200, 301):
        if k != tmp:
            sum1 = 0
            for i in range(1, k):
                if k % i == 0:
                    sum1 += i

            sum2 = 0
            for j in range(1, sum1):
                if sum1 % j == 0:
                    sum2 += j

            if sum2 == k != sum1:
                array.append(str(k) + ' ' + str(sum1))
                tmp = sum1

    return array

task_560.info = __doc__
