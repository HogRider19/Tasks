"""
Your task is to write a funtion luck_check(str),
which returns true/True if argument is string decimal
representation of a lucky ticket number, or false/False for all other numbers.
It should throw errors for empty strings or strings which don't represent a decimal number
"""


def luck_check(str):

    try:
        int(str)
    except ValueError:
        raise "Invalid number"

    mean_len_down = int(len(str)/2)
    mean_len_up = mean_len_down

    if len(str) % 2 != 0:
        mean_len_up += 1
    
    left_sum = sum([int(i) for i in str[:mean_len_down]])
    right_sum = sum([int(i) for i in str[mean_len_up:]])

    if left_sum == right_sum:
        return True
    
    return False



print(luck_check('002311'), 'True')
print(luck_check('813372'), 'True')
print(luck_check('71980'), 'Flase')
print(luck_check('403412'), 'True')
