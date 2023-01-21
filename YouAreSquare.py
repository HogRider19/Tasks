"""
You like building blocks. You especially like building blocks that are squares.
And what you even like more, is to arrange them into a square of square building blocks!
However, sometimes, you can't arrange them into a square. Instead,
you end up with an ordinary rectangle! Those blasted things!
If you just had a way to know, whether you're currently working in
vain… Wait! That's it! You just have to check if your number
of building blocks is a perfect square
"""

import math


def is_square(n):    
    return round(sq := math.sqrt(n)) == sq if n >= 0 else False


assert is_square(-1) == False
assert is_square( 0) == True
assert is_square( 3) == False
assert is_square( 4) == True