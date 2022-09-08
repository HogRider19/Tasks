"""
You need count how many valleys you will pass.
Start is always from zero level.
Every time you go down below 0 level counts as an entry of a valley,
and as you go up to 0 level from valley counts as an exit of a valley.
One passed valley is equal one entry and one exit of a valley.
"""

def counting_valleys(s):
    level = 0
    count_valleys = 0
    for c in s:
        if c == "D":
            level -= 1
        elif c == "U":
            level += 1
            if level == 0:
                count_valleys += 1
    return count_valleys