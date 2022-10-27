"""
Complete the function that returns an array of length n,
starting with the given number x and the squares of the previous number.
If n is negative or zero, return an empty array/list.
"""


def squares(x, n):
     
    if n <= 0: 
        return []

    result = []
    previous_number = x
    for i in range(x+1, x+n):
        number = previous_number**2
        result.append(number)
        previous_number = number

    return [x] + result


print(squares(2, 5) == [2, 4, 16, 256, 65536])
print(squares(3, 3) == [3, 9, 81])
print(squares(5, 3) ==  [5, 25, 625])
print(squares(2, -4) ==  [])