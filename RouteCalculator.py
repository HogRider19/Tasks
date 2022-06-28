"""
This calculator takes values that could be written in a browsers route path as a single string.
 It then returns the result as a number (or an error message).
Route paths use the '/' symbol so this can't be in our calculator.
 Instead we are using the '$' symbol as our divide operator.
"""

def calculate(expression):
    
    exp_list = []
    single_exp = ''

    for letter in expression + '$':
        if letter not in '.0123456789+-*$':
            return '400: Bad request'
        else:
            if letter in '+-*$':
                exp_list.append(single_exp)
                exp_list.append(letter)
                single_exp = ''
            else:
                single_exp += letter

    exp_list.pop(-1)

    for index, element in enumerate(exp_list):

        if str(element) in '*$':
            val = ''

            if element == '*':
                val = float(exp_list[index - 1]) * float(exp_list[index + 1])
            elif element == '$':
                val = float(exp_list[index - 1]) / float(exp_list[index + 1])

            exp_list[index] = val
            exp_list[index - 1] = val  
            exp_list[index + 1] = val


    new_exp_list = []
    single_exp = ''
    exp_list.append('+')
    for index, letter in enumerate(exp_list):

        if str(letter) in '+-':
            new_exp_list.append(exp_list[index - 1])
            new_exp_list.append(exp_list[index])

    exp_list = new_exp_list
    exp_list.pop(-1)

    for index, element in enumerate(exp_list):

        if str(element) in '+-':
            val = ''

            if element == '+':
                val = float(exp_list[index - 1]) + float(exp_list[index + 1])
            elif element == '-':
                val = float(exp_list[index - 1]) - float(exp_list[index + 1])

            exp_list[index] = val
            exp_list[index - 1] = val  
            exp_list[index + 1] = val 

    
    return float(exp_list[-1])


print(calculate('1'))