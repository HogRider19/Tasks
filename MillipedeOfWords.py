"""
The set of words is given. Words are joined if the last letter
of one word and the first letter of another word are the same.
Return true if all words of the set can be combined into one word.
Each word can and must be used only once. Otherwise return false.
"""


def helper(arr, cur):
    if arr == []: return True
    for idx, elem in enumerate(arr):
        if elem[0] == cur:
            print("  help: ", elem)
            temp = arr[:idx] + arr[idx+1:]
            if helper(temp, elem[-1]): return True
    return False

def solution(arr):
    output = []
    for idx, elem in enumerate(arr):
        temp = arr[:idx] + arr[idx+1:]
        output += [helper(temp, elem[-1])]
    return True in output


