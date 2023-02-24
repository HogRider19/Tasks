"""
Winter is coming, you must prepare your ski holidays. The objective of this kata is
to determine the number of pair of gloves you can constitute from the gloves you have in your drawer.
Given an array describing the color of each glove, return the number of pairs you
can constitute, assuming that only gloves of the same color can form pairs.
"""

def number_of_pairs(gloves):
    color_set = set(gloves)
    pairs = 0
    for i in color_set:
        n = gloves.count(i)
        if n > 1:
            pairs += n // 2
    return pairs