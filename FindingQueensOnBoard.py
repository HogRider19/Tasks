"""
    Your task is to find the maximum number of queens that can
    be put on the board so that there would be one single unbeaten square (ie. threatened by no queen on the board).
    The Queen can move any distance vertically, horizontally and diagonally.
"""

def queens(n):
    number = n - 2
    if number < 0:
        return 0
    return (number ** 2) + number