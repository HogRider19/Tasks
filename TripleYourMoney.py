"""
You've found yourself a magic box, which seems to break the laws of physics.
You notice that if you put some money in it, it seems to
spit out more money than was put in.Free money right?
In time you notice the following facts:
If you start with N dollars, using the box twice yields exactly 3*N dollars
You never seem to get any fractional dollar amounts
The box consistently gives the same amount out, if the amount put in is the same
The more money you put in, the more money you get out
Note: "using the box twice" means using it once, and then using it
again with all of the money the box gave you
"""

from math import log

def f(n):
    if n == 0:
        return 0
    k=3**int(log(n)/log(3))
    z= 2 * max(0,n-2*k)
    return n+z+k