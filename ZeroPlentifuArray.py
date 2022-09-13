"""
An array is called zero-plentiful if it contains
multiple zeros, and every sequence of zeros is at least 4 items long.
Your task is to return the number of zero sequences
if the given array is zero-plentiful, oherwise 0.
"""

def zero_plentiful(arr):
    zero = 0
    result = 0
    for letter in arr+[1]:
        if letter == 0:
            zero += 1
        else:
            if zero >= 4:
                result += 1
            else:
                result = 0
                break
            zero = 0     
    return result



print(zero_plentiful([3]),0)
print(zero_plentiful([0,0,0,0,0,0]),1)