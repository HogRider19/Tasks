"""
You are given a list of prime numbers (e.g. [5, 7, 11]) and a list of their associated
powers (e.g. [2, 1, 1]). The product of those primes at their specified
power forms a number x (in our case x = 5^2 * 7^1 * 11^1 = 1925).
To do so, you have to multiply each prime number, from its power 0 to its power
p in the power list, to every other prime, from their power 0 to their associated power p.
"""


def get_dividers(values, powers):
    ans = [1]
    for prime, exponent in zip(values, powers):
        multiplier, count_so_far = 1, len(ans)
        for j in range(exponent):
            multiplier *= prime
            ans.extend([multiplier * ans[i] for i in range(count_so_far)])
    return sorted(ans)