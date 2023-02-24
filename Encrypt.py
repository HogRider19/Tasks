"""
    Original althabet: abcdefghijklmnopqrstuvwxyz
    New althabet +3:   defghijklmnopqrstuvwxyzabc

    Input: Hello, world!
    Output: ?
"""

from string import ascii_lowercase


def encrypt2(st: str, offset: int):
    result = []
    for letter in st.lower():
        letter_index = ord(letter)
        if 97 <= letter_index <= 122:
            replace_index = letter_index + offset
            if replace_index > 122:
                replace_index -= 25
            elif replace_index < 97:
                replace_index += 25
            letter = chr(replace_index)
        result.append(letter)
    return ''.join(result)

print(encrypt2('Hello, world!', 5))