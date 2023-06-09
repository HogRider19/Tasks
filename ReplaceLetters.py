"""
replace the vowel with the nearest left consonant.
replace the consonant with the nearest right vowel.
P.S. To complete this task imagine the alphabet is a circle.
For example, 'a' replace with 'z', 'y' with 'a', etc.
"""

TR = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'zeeediiihooooonuuuuutaaaaa')

def replace_letters(word):
    return word.translate(TR)