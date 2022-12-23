"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!
"""


def find_uniq(arr):
    numbers_map = {}
    for num in arr:
        if num in numbers_map:
            numbers_map[num] += 1
        else:
            numbers_map.update({num: 1})

    for key in numbers_map.keys():
        if numbers_map[key] == 1:
            return key


assert find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
assert find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
assert find_uniq([ 3, 10, 3, 3, 3 ]) == 10