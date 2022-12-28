"""
You and your friends want to rent a house for the new year, but the problem is that people
can go for a different number of days. It is necessary to calculate the amount that each person must pay,
depending on how many days he is going to live in this house. The amount per person is the rental price divided
by the number of people living in the house on a given day. Rent paid every time someone leaves the house

Write a function that takes an array with the number of days each person will live in the house
(the length of the array is the total number of people) and the rent per apartment per day.
The function should return a dictionary where the key will be the number of days, and the value
will be the amount that the person must deposi
"""

import math


def calculate_cost_per_person(array, rental):
    res = {}
    rent = 0
    before = 0
    for a in sorted(set(list(array))):
        rent += math.ceil((rental/len(list(filter(lambda x: x>=a, array))))*(a-before))
        before = a
        res[a] = rent
    return res

assert calculate_cost_per_person([7, 7, 7, 7, 1, 1, 2, 4, 5, 6], 100) == {
                            1: 10, 2: 23, 4: 52, 5: 69, 6: 89, 7: 114}
assert calculate_cost_per_person([12, 20, 4, 20, 10, 10, 10, 7, 7, 7], 50 ) == {
                            4: 20, 7: 37, 10: 62, 12: 96, 20: 296}