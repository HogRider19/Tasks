"""
Compute the complex logarithm at any given complex number,
accurate to at least 1 in 10^-12. The imaginary part should be inside the interval (−π, π]
(i.e if the imaginary part is exactly π, keep it as is).
Note: You shouldn't try to compute the value of this function at the poles.
"""

import cmath

def log(real, imag):
    c = complex(real, imag)
    try:
        c = cmath.log(c)
    except ValueError:
        return None
    return c.real, c.imag