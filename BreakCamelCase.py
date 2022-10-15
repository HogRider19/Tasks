"""
Complete the solution so that the function will
break up camel casing, using a space between words.
"""

def solution(s):
    split_index = [index for index, letter in enumerate(s) if letter.isupper()]

    words = []
    previous_index = 0
    for index in split_index:
        words.append(s[previous_index:index])
        previous_index = index
    words.append(s[previous_index:len(s)])

    return ' '.join(words)


print(solution('helloWorld') == 'hello World')
print(solution('camelCase') == 'camel Case')
print(solution('breakCamelCase') == 'break Camel Case')
print(solution('') == '')