"""
Given a string, return the minimal number of parenthesis
reversals needed to make balanced parenthesis
"""


def solve(s: str) -> int:
    inv = open = 0
    for c in s:
        if c == '(':
            open += 1
        elif open:
            open -= 1
        else:
            open = 1
            inv += 1
    return inv + open // 2


assert solve(")()(") == 2
assert solve("((()") == 1
assert solve("())(((") == 3
assert solve("())()))))()()(") == 4