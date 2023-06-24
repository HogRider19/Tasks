"""
AWrite a function that validates if an input array is a latin square.
It has two parameters, the array and a positive integer m > 1. To help the user with debugging,
it should return an appropriate message, as detailed below. It must not modify the input array
"""


def verify_latin_square(arr, m):
    ver= [i for i in range(1, m + 1)]

    if len(arr) != max( len(r) for r in arr ) or len(arr) != min( len(r) for r in arr ): 
        return "Array not square"
    if len(arr) != m: return "Array is wrong size"

    for i,r in enumerate(arr):
        if ver != sorted(r):
            for j in ver:
                if r.count(j) > 1:
                    return f"{j} occurs more than once in row {i+1}"
        if max(r) > m:
            return f"{max(r)} at {i + 1},{r.index(max(r)) + 1} is not between 1 and {m}"
        if min(r) < 1:
            return f"{min(r)} at {i + 1},{r.index(min(r)) + 1} is not between 1 and {m}"
        
        
    for c in range(len(arr)):
        col = [r[c] for r in arr]
        if ver != sorted(col):
            for j in ver:
                if col.count(j) > 1:
                    return f"{j} occurs more than once in column {c + 1}"
    
    return f"Valid latin square of size {m}"