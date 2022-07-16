"""
Write a program that will calculate the number of
trailing zeros in a factorial of a given number.
"""

def factorial(n):
    return factorial(n-1) * n if n > 1 else 1


def zeros(n):
    
    result = 0
    div_n = n

    while div_n > 0:
        div_n = int(div_n / 5)
        result += div_n

    return result


print(22, zeros(22))

