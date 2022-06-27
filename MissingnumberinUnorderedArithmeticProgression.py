"""
Note: Don't be afraid that the minimum or the maximum element in the list is missing,
 e.g. [4, 6, 3, 5, 2] is missing 1 or 7, but this case is excluded from the kata.
"""

def find(seq):

    seq_set = sorted(seq)

    element = (seq_set[0] + seq_set[-1])/2 * (len(seq) + 1) - sum(seq_set)

    return element


print(find([4, 6, 3, 5, 2]))



