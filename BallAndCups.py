"""
Ronny the robot is watching someone perform the Cups and Balls magic trick.
The magician has one ball and three cups, he shows Ronny which cup he hides the ball under (b),
\he then mixes all the cups around by performing multiple two-cup switches (arr).
Ronny can record the switches but can't work out where the ball is. Write a programme to help him do this
"""


def cup_and_balls(b, arr):
    for flip in arr:
        if b in flip:
            b = sum(flip) - b
    return b


assert cup_and_balls(2,[[1,2]]) == 1
assert cup_and_balls(1,[[2,3],[1,2],[1,2]]) == 1
assert cup_and_balls(2,[[1,3],[1,2],[2,1],[2,3]]) == 3