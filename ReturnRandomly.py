"""
You have to create a function namedone_two (oneTwo for Java or Preloaded.OneTwo for C#)
that returns 1 or 2 with equal probabilities. one_two is already defined in a global scope and can be called everywhere.
Your goal is to create a function named one_two_three (oneTwoThree for Java or OneTwoThree for C#)
that returns 1, 2 or 3 with equal probabilities using only the one_two function.
"""

def one_two():
    """For test"""
    import random
    return 1 if random.random() < 0.5 else 2

def one_two_three():
    value1 = one_two()
    value2 = one_two()
    while value1 == 1 and value2 == 2:
        value1 = one_two()
        value2 = one_two()

    if value1 == value2 == 1:
        return 1
    elif value1 == value2 == 2:
        return 2 
    else:
        return 3



values = []
for i in range(1000):
    values.append(one_two_three())
print(f"Count one: {round(values.count(1)/len(values)*100)}")
print(f"Count two: {round(values.count(2)/len(values)*100)}")
print(f"Count three: {round(values.count(3)/len(values)*100)}")
    