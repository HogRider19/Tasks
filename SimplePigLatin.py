"""
Move the first letter of each word to the end of it, then add 
"ay" to the end of the word. Leave punctuation marks untouched.
"""

def pig_it(text):
    res = []
    for i in text.split():
        if i.isalpha():
            res.append(i[1:]+i[0]+'ay')
        else:
            res.append(i)      
    return ' '.join(res)


print(pig_it('Pig, latin is cool'),'igPay atinlay siay oolcay')
print(pig_it('This is my string'),'hisTay siay ymay tringsay')