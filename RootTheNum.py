"""
    Find the sum of all positive integer roots up to (and including) the nth term of n, whose products are rational positive integers.
"""

import math


def RootSum(n):
    output = 0
    for i in range(1, n + 1):
        rt = math.pow(n, 1.0 / i)
        if round(rt,10) == round(rt):
            output += rt
        elif round(rt,10) < 2:
            break
  
    return round(output)