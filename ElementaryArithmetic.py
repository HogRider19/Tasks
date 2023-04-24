"""
In elementary arithmetic a "carry" is a digit that is transferred from one column of
digits to another column of more significant digits during a calculation algorithm.
This Kata is about determining the number of carries
performed during the addition of multi-digit numbers
"""

def solve(lines):
    result = []
    for line in lines.split('\n'):
        count, c = 0, 0
        for i, j in zip(*line[::-1].split()):
            if c := (int(i) + int(j) + c) // 10:
                count += 1
        result.append(f'{count} carry operations' if count else 'No carry operation')
    return '\n'.join(result)