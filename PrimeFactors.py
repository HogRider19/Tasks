"""
Write a function that generates factors for a given number.
The function takes an integer as parameter and returns a list of integers
(ObjC: array of NSNumbers representing integers). That list contains
the prime factors in numerical sequence
"""

def prime_factors (n):
    a, b = 2, []
    while n > 1:
        while not n % a:
            b += [a]
            n = n // a
        a += 1
    return b