"""
    Create a function that takes a list of integers and a group length as parameters.
    Your task is to determine if it's possible to split all the numbers from the list
    into groups of the specified length, while ensuring that
    consecutive numbers are present within each group.
"""

from collections import Counter

def consecutive_nums(lst, group_len):
    lst = Counter(lst)
    while lst:
        x = min(lst)
        for i in range(group_len):
            if x + i not in lst:
                return False
            lst[x + i] -= 1
            if lst[x + i] == 0:
                lst.pop(x + i)
    return True