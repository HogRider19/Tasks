"""
The dominoes in a full set come in a couple of types. For each number of pips there is a double domino,
ranging from double blank represented [0, 0] up to double six, sometimes nine, fifteen, or in general [n, n].
Then there are all combinations of different numbers. For instance, a standard set has a single domino with
a blank on one end and six pips on the other, which could be represented either as [0, 6] or equivalently [6, 0]
"""

def make_train(n):
    res = [[0, 1], [1, 1], [1, 0]]
    for m in range(2, n + 1):
        for i in range(m):
            res.append([i, m])
            res.append([m, i + 1])
        res.append([m, 0])
    res.append([0, 0])
    return res

r = make_train(1500)

def domino_train(n):
    if n == 0: return [0, 0]
    res = r[:(n + 1)**2 - 1] + [[0, 0]]
    return [0] + [x[1] for x in res]