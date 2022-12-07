"""
Given an array in which each number occurs twice,
and only one number occurs once. Find this number
"""


def find_non_repeating(arr: list) -> int:
    return 2*(sum(set(arr))) - sum(arr)


print(find_non_repeating([1, 1, 2, 2, 3]), 3)
print(find_non_repeating([12, -11, 12, -11, 88]), 88)
print(find_non_repeating([0, 0, 100, 100, 200, 200, 111]), 111)