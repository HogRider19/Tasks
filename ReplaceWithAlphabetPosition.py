"""
In this kata you are required to, given a string,
replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"""

import string

def alphabet_position(text):
    
    encoder_alphabet = {letter: str(index + 1) for index, letter
                                    in enumerate(string.ascii_lowercase)}

    result = []
    for letter in text.lower():
        if letter in encoder_alphabet:
            result.append(encoder_alphabet.get(letter))


    return ' '.join(result)



print(alphabet_position("The sunset sets at twelve o' clock.") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
print(alphabet_position("The narwhal bacons at midnight.") == "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")