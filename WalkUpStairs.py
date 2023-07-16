"""
Raj was to move up through a pattern of stairs of a given number (n).
Help him to get to the top using the function stairs. If n<1 then return ' ' .
There are a lot of spaces before the stair starts except for pattern(1)
"""

def stairs(n):
    x = [i%10 for i in range(1, n+1)]
    m = []
    for _ in range(n):
        m += [' '.join(map(str,x + x[::-1]))]
        x = x[:-1]
    f = len(m[0])
    return '\n'.join(' '*(f-len(i))+i for i in m[::-1])