"""
Given an array of integers of any length, return an
array that has 1 added to the value represented by the array.
"""

def up_array(arr: list):

    if not arr or min(arr) < 0 or max(arr) > 9:
        return None

    zero_count = 0
    for i in arr:
        if i == 0:
            zero_count += 1
        else:
            break

    val = int(''.join([str(i) for i in arr]))
    val += 1
    
    return [0 for i in range(zero_count)] + [int(i) for i in str(val)]

print(up_array([4, 3, 2, 5]) == [4, 3, 2, 6])
print(up_array([1, 2, 3, 9]) == [1, 2, 4, 0])
print(up_array([9, 9, 9, 9]) == [1, 0, 0, 0, 0])
print(up_array([0, 1, 3, 7]) == [0, 1, 3, 8])
