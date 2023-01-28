"""
Yup!! The problem name reflects your task; just add a set of numbers.
But you may feel yourselves condescended, to write a C/C++ program just to add
a set of numbers. Such a problem will simply question your erudition.
So, lets add some flavor of ingenuity to it. Addition operation requires cost now,
and the cost is the summation of those two to be added. So,to add 1 and 10,
you need a cost of 11. If you want to add 1, 2 and 3. There are several ways
"""

def add_all(lst: list) -> int: 
    if len(lst) == 1:
        return 0
    
    lst.sort()
    cost = sum(lst[:2])
    lst[:2] = cost,
    
    return cost + add_all(lst)


assert add_all([1,2,3]) == 9
assert add_all([1,2,3,4]) == 19
assert add_all([1,2,3,4,5]) == 33