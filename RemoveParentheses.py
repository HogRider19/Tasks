"""
In this kata you are given a string
Your task is to remove everything inside
the parentheses as well as the parentheses themselves.
"""


def remove_parentheses(s: str) -> str:
    result = ''
    bracket_counter = 0
    for letter in s:
        if letter == '(':
            bracket_counter += 1
        elif letter == ')':
            bracket_counter -= 1
        else:
            if not bracket_counter:
                result += letter
    return result


assert remove_parentheses("example (unwanted thing) example") == "example  example"
assert remove_parentheses("a (bc d)e") == "a e"
assert remove_parentheses("a(b(c))") == "a"