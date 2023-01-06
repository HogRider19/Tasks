"""
To do this, you must first count the 'mini-wins' on your ticket. Each subarray
has both a string and a number within it. If the character code
of any of the characters in the string matches the
number, you get a mini win. Note you can only have one mini win per sub array.

Once you have counted all of your mini wins, compare that number to the other input 
provided (win). If your total is more than or equal to (win),
return 'Winner!'. Else return 'Loser!'.
"""

def bingo(ticket,win):
    min_wins = 0
    for field in ticket:
        if field[1] in [ord(letter) for letter in field[0]]:
            min_wins += 1
    return 'Loser!' if min_wins < win else 'Winner!'

assert bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 2) == 'Loser!'
assert bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 1) == 'Winner!'
assert bingo([['HGTYRE', 74], ['BE', 66], ['JKTY', 74]], 3) == 'Loser!'