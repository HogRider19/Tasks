"""
Check if two words are anogram
"""


from collections import Counter


def is_anogram(s1: str, s2: str) -> bool:
    return Counter(s1) == Counter(s2)


assert is_anogram('abs', 'bsa') == True
assert is_anogram('aaabbbccc', 'bbbaaccca') == True
assert is_anogram('aaabbbccc', 'bbbaaccc') == False
assert is_anogram('a', 'ab') == False

