"""
Write a function that accepts a square matrix (N x N 2D array) and returns the determinant of the matrix.
"""

def determinant(matrix):
    len_matr = len(matrix[0])

    if len_matr == 1:
        return matrix[0][0]
    elif len_matr == 2:
        return det_2x2(matrix)
    else:
        det = 0
        for i, column in enumerate([matrix[0]]):
            for j, element in enumerate(column):
                det += (-1)**(j) * element * minor(matrix, [i, j])
        return det


def det_2x2(matrix):
    '''[[a, b], [c, d]] ->  a*d - b*c'''
    return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]


def minor(matrix, element_pos):
    len_matr = len(matrix[0])

    new_matrix = []
    for x in range(len(matrix)):
        new_matrix_row = []
        for y in range(len(matrix)):
            if x != element_pos[0] and y != element_pos[1]:
                new_matrix_row += [matrix[x][y]]
        new_matrix += [new_matrix_row]

    new_matrix = new_matrix[1:]

    if len_matr == 2:
        return new_matrix[0][0]
    elif len_matr == 3:
        return det_2x2(new_matrix)
    elif len_matr >= 4:
        return determinant(new_matrix)


m = [[1,2,3], [4,5,6], [7,8,9]]
print(determinant(m))



