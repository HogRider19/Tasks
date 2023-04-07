"""
Your task is to write a function that accept a single parameter - a whole number N and
generates an array with following properties.
There are exactly 2 * N + 1 elements in this array
There is only one 0 (zero) in array
Other elements are pairs of natural numbers from 1 to N
Number of elements between a pair of numbers is equal to the number itself
For example, the number of elements between pair of 2s should be exactly 2, for 3s - three and so on.
"""

def generate(n):
    r1, r2 = range(1,n,2), range(2,n,2)
    return [*reversed(r1), n, *r1, *reversed(r2), 0, n, *r2] if n else [0]