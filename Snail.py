"""
Given an n x n array, return the array elements arranged 
from outermost elements to the middle element, traveling clockwise.
"""


def snail(snail_map):

    if len(snail_map) == 1:
        return snail_map

    result = []
    new_matrix = snail_map
    for i in range(round(len(snail_map[0])/2)):

        result += get_square_element(new_matrix)

        new_matrix = get_matrix_down(new_matrix)

        if new_matrix is None:
            break
        elif type(new_matrix) == int:
            result += [new_matrix]
            break

    
    return result


def get_square_element(matrix):

    len_map = len(matrix[0])

    if len_map == 1:
        return [matrix[0][0]]

    result = matrix[0].copy()

    result += [matrix[i][-1] for i in range(1, len_map)]

    result += [i for i in matrix[-1][0:-1][::-1]]

    result += [matrix[i][0] for i in range(len_map - 2, 0, -1)]

    return result


def get_matrix_down(matrix):

    len_matrix_down = len(matrix[0]) - 1

    if len(matrix[0]) == 3:
        return matrix[1][1]
    elif len_matrix_down == 2:
        return None

    down_matrix = matrix[1:len_matrix_down]

    for i in range(len_matrix_down-1):
        
        down_matrix[i].pop(0)
        down_matrix[i].pop(-1)
        

    return down_matrix



array = [[1,2,3],
         [4,5,6],
         [7,8,9]]


print(snail([1]), [1,2,3,6,9,8,7,4,5])
