"""
The number 23 is special in the sense that all of its digits are prime numbers. Furthermore, it's a prime itself.
There are 4 such numbers between 10 and 100: 23, 37, 53, 73. Let's call these numbers "total primes".

Complete the function that takes a range (a, b) and returns the number of total primes within that range (a <= primes < b). The test ranges go up to 107
"""

from itertools import product

def isPrime(n):
    return n == 2 or n % 2 and all(n % p for p in range(3, int(n **0.5) + 1, 2))

def get_total_primes(a, b):
    low, high = map(len, map(str, (a, b)))
    return sum(a <= n < b and isPrime(n) for d in range(low, high + 1) for n in map(int, map(''.join, product("2357", repeat = d))))