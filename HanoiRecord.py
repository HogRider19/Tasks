"""
Your task, is to calculate the minimal number of moves to win the game
"Towers of Hanoi", with given number of disks.
"""


def hanoi(disks):
    return 2 ** disks - 1