"""
Your task is to return nth element of this sequence.
Input: n - positive integer (max 268435455)
Output: string - nth expression of sequence - 'a/b' where a and b are integers.
"""


def cantor(n : int) -> str:
    max_in_diagonal = 1
    items_per_diagonal = 1
    is_up = True
    while max_in_diagonal < n:
        items_per_diagonal += 1
        max_in_diagonal += items_per_diagonal
        is_up = not is_up
        
    min_in_diagonal = max_in_diagonal - items_per_diagonal + 1
    
    if is_up:
        numerator = max_in_diagonal - n + 1
        denominator = n - min_in_diagonal + 1
    else:
        numerator = n - min_in_diagonal + 1
        denominator = max_in_diagonal - n + 1
        
    return f'{numerator}/{denominator}'