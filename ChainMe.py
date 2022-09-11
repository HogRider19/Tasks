"""
Write a generic function chainer that takes a starting value
and an array of functions to execute on it.
The input for each function is the output
of the previous function (except the first function, which takes
the starting value as its input). Return the final value after execution is complete.
"""

def chain(init_val, functions):
    value = init_val
    for fun in functions:
        value = fun(value)
    return value

def add10(x):
    return x + 10

def add50(x):
    return x + 50


print(chain(100, [add10, add50]), 160)

