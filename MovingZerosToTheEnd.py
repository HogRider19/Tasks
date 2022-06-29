"""
Write an algorithm that takes an array and moves all of the zeros to
the end, preserving the order of the other elements.
"""

def move_zeros(array):

    count_zeros = array.count(0)

    for i in range(count_zeros):
        array.remove(0)
        array.append(0)

    return array



a = [2,35,67,4,3,4,6,0,0,1,0]
print(move_zeros(a))