"""
Your task, is to create N×N multiplication table, of size provided in parameter
"""


def multiplication_table(size: int):
    matrix = [[index]*size for index in range(size)]

    for row in range(size):
        for col in range(size):
            matrix[row][col] = (row + 1)* (col + 1)

    return matrix


assert multiplication_table(3) == [[1,2,3],[2,4,6],[3,6,9]]