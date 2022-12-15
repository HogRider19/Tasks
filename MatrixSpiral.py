"""
The input is two natural numbers n and m.
Write a program that creates an n x m matrix by filling it in
a spiral with numbers from 1 to n x m. The spiral starts in the left corner and twists clockwise
"""


def get_spiral_matrix(n: int, m: int):
    mx = [[None] * m for _ in range(n)]
    dx, dy = 0, 1
    x, y = 0, 0

    for i in range(1, n * m + 1):
        mx[x][y] = i
        if mx[(x + dx) % n][(y + dy) % m]:
            dx, dy = dy, -dx
        x += dx
        y += dy    
    return mx


print(get_spiral_matrix(3, 3))