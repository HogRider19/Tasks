"""
Реализуйте алгоритм для вывода всех корректных
(правильно открытых и закрытых) комбинаций из n пар круглых скобок
"""


def check_bracket(st: str, brackets: dict) -> bool:
    bracket_set = set(sum(list(brackets.items()), ()))
    stack = []

    for letter in st:
        if letter in bracket_set:
            if letter in brackets:
                stack.insert(0, letter)
            elif brackets[stack[0]] == letter:
                stack.pop(0)
            else:
                return False
    return True
