"""
Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its
position in the alphabet: a = 1, b = 2, c = 3 etc.
For example, the score of abad is 8 (1 + 2 + 1 + 4).
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid.
"""

from string import ascii_lowercase

def high(text: str) -> str:
    score_map = {letter: score+1 for score, letter in enumerate(ascii_lowercase)}
    high_word, high_score = '', 0
    for word in text.lower().split():
        score = sum([score_map.get(letter, 0) for letter in word])
        if score > high_score:
            high_score = score
            high_word = word
    return high_word

assert high('man i need a taxi up to ubud') == 'taxi'
assert high('what time are we climbing up the volcano') == 'volcano'
assert high('take me to semynak') == 'semynak'
assert high('aa b') == 'aa'
assert high('b aa') == 'b'
assert high('bb d') == 'bb'