"""
I want to count from 1 to n. How many times will I use a '9'?
9, 19, 91.. will contribute one '9' each, 99, 199, 919.. wil contribute two '9's each...etc
Note: n will always be a positive integer
"""

from utils import lead_time


def count_nines(n):
    digits = [int(a) for a in str(n)]
    l = len(digits)
    return sum(
        d * int((l-i-1) * 10 ** (l - i - 2)) + (d==9)*(n%(10**(l-i-1)) + 1)
        for i, d in enumerate(digits))


assert count_nines(100) == 20
assert count_nines(200) == 40
assert count_nines(201) == 40
assert count_nines(278) == 47
assert count_nines(909) == 191
assert count_nines(99999) == 50000
assert count_nines(565754) == 275645