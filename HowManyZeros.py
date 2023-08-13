"""
    Define n!! as
    n!! = 1 * 3 * 5 * ... * n if n is odd,
    n!! = 2 * 4 * 6 * ... * n if n is even.
    Hence 8!! = 2 * 4 * 6 * 8 = 384, there is no zero at the end. 30!! has 3 zeros at the end.
    For a positive integer n, please count how many zeros are there at the end of n!!
"""

def count_zeros_n_double_fact(n):
    if n % 2: return 0
    s, n = 0, n // 2
    while n >= 5:
        n //= 5
        s += n
    return s