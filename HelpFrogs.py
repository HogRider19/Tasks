"""
You will be given an integer N which specifies the number of both types
of frogs i.e. N White and N Black frogs. The board will therefore always be of size 2*N + 1.
You must return a string of the letters w, b, j, which encodes the
moves your algorithm takes to solve the problem for a given value of N.
"""

def white_black_frogs(n):
    return (t := ''.join('wb'[i & 1] + 'j' * (i + 1) for i in range(n))) + t[:-n][::-1]