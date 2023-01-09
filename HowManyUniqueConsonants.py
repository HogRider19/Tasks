"""
Complete the function that counts the number of unique consonants
in a string (made up of printable ascii characters).
Consonants are letters used in English other than 
"a", "e", "i", "o", "u". We will count "y" as a consonant.
Remember, your function needs to return the number of unique consonants - disregarding
duplicates. For example, if the string passed into the function reads "add",
the function should return 1 rather than 2, since "d" is a duplicate.
Similarly, the function should also disregard duplicate consonants of differing cases.
For example, "Dad" passed into the function should return 1 as "d" and "D" are duplicates.
"""


def count_consonants(text: str) -> int:
    consonants = set('bcdfghjklmnpqrstvwxyz')
    buffer = set()
    for letter in text.lower():
        if letter in consonants and letter not in buffer:
            buffer.add(letter)
    return len(buffer)


assert count_consonants('sillystring') == 7
assert count_consonants('aeiou') == 0
assert count_consonants('abcdefghijklmnopqrstuvwxyz') == 21
assert count_consonants('Count my unique consonants!!') == 7