"""
 1. The input string will always be lower case but maybe empty.
 2. If the character in the string is whitespace then pass over it as if it was an empty seat
"""


def wave(st: str) -> list:
    result = []
    for index, letter in enumerate(st):
        if letter.isalpha():
            result.append(f"{st[:index]}{st[index].upper()}{st[index+1:]}")
    return result


assert wave("") ==  []
assert wave("hello") ==  ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
assert wave("codewars") ==  ["Codewars", "cOdewars", "coDewars", "codEwars",
                    "codeWars", "codewArs", "codewaRs", "codewarS"]
assert wave("two words") == ["Two words", "tWo words", "twO words", "two Words",
                    "two wOrds", "two woRds", "two worDs", "two wordS"]