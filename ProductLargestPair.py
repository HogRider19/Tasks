"""
Rick wants a faster way to get the product of the largest pair in an array.
Your task is to create a performant solution to find 
the product of the largest two integers in a unique array of positive numbers.
"""

def max_product(a):    
    first_max = 0
    second_max = 0
    for x in a:
        if x > first_max:
            second_max = first_max
            first_max = x
        elif x > second_max:
            second_max = x
    return first_max*second_max