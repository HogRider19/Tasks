"""
    Your task is to find the last non-zero digit of n! (factorial)
"""

def last_digit(n):
    if n < 10:
        return [1, 1, 2, 6, 4, 2, 2, 4, 2, 8][n]
    else:
        return (4 if int(str(n)[-2]) % 2 else 6) * last_digit(n // 5) * last_digit(n % 10) % 10