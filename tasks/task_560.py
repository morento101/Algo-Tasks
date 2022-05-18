"""560. Find all pairs of friendly numbers between 200 and 300.
Two natural numbers are called friendly if each of them is equal 
to the sum of all divisors of the other, except for this number itself.
"""


def task_560() -> list:
    """Return all pairs of friendly numbers between 200 and 300."""
    tmp = 0
    pairs_of_friendly_nums = []
    for k in range(200, 301):
        if k != tmp:
            sum_of_divisor_1num = 0
            for i in range(1, k):
                if k % i == 0:
                    sum_of_divisor_1num += i

            sum_of_divisor_2num = 0
            for j in range(1, sum_of_divisor_1num):
                if sum_of_divisor_1num % j == 0:
                    sum_of_divisor_2num += j

            if sum_of_divisor_2num == k != sum_of_divisor_1num:
                pairs_of_friendly_nums.append(
                    str(k) + ' ' + str(sum_of_divisor_1num))
                tmp = sum_of_divisor_1num

    return pairs_of_friendly_nums


task_560.info = __doc__
