"""
Your job is to write a function which increments a string, to create a new string.
If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
"""


def increment_string(strng):
    
    number = '' 
    slice_len = 0
    zero_count = 0
    for letter in strng[::-1]:
        
        try:
            int(letter)
            number += letter
            slice_len += 1
            if letter == '0':
                zero_count += 1
            else:
                zero_count = 0
        except ValueError:
            break

    if number:
        new_str = strng[:-slice_len] + f'{zero_count*"0"}{int(number[::-1])+1}'
    else:
        new_str = strng + '1'

    return new_str

    



print(increment_string("foo"), "foo1")
print(increment_string("foobar001"), "foobar002")
print(increment_string("foobar1"), "foobar2")