"""
The block letters should consist of corresponding capital letters.
It's irrelevant whether input consists of lower or upper case letters.
Any leading and/or trailing spaces in input should be ignored.
Empty strings or such containing only spaces should return an empty string.
The remaining spaces (between letters and/or words) are to be treated as any other character.
This means that there will be six spaces in output for a space in input, or a multiple of six,
if there were more spaces - plus the one from preceding character!
Trailing spaces should be removed in the resulting string.
The string should be formatted in a way that when passed to Pythons' print()
function shows the desired output (see below for example).
"""

def get_face(face):
    faces = { ':D':0, ':)':1, ':|':2, ':(':3, 'T_T':4 }
    return faces[face]

def sort_emotions(arr, order):
    return sorted(arr, key=get_face, reverse= not order)