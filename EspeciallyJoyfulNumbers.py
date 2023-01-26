"""
Positive integers that are divisible exactly by the sum of their digits are called Harshad numbers.
The first few Harshad numbers are: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, ...
We are interested in Harshad numbers where the product of its digit
sum s and s with the digits reversed, gives the original number n.
"""


def number_joy(n):
    return (s:=sum(int(digit) for digit in str(n))) * int(str(s)[::-1]) == n

assert number_joy(1997) == False
assert number_joy(1998) == False
assert number_joy(1729) == True