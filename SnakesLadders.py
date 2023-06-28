"""
This Kata is like the game of Snakes & Ladders
There is an array representing the squares on the game board.
The starting square is at array element 0. The final square is the last array element.
At each "turn" you move forward a number of places (according to the next dice throw)
"""


def snakes_and_ladders(board, dice) -> int:
    ind = 0
    l = len(board)
    for i in dice:
        if (ind + i) < l:
            ind += i
            ind += board[ind]
    return ind