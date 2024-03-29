"""
The number 89 is the first integer with more than one digit that
fulfills the property partially introduced in the title of this kata.
What's the use of saying "Eureka"? Because this sum gives the same number.
In effect: 89 = 8^1 + 9^2
The next number in having this property is 135.
See this property again: 135 = 1^1 + 3^2 + 5^3
We need a function to collect these numbers,
that may receive two integers a, b that defines the range [a, b]
(inclusive) and outputs a list of the sorted numbers in
the range that fulfills the property described above.
"""


def sum_dig_pow(a, b):
    result = []
    for num in range(a, b+1):
        magic_sum = sum([int(letter)**(index+1) for index, letter in enumerate(str(num))])
        if magic_sum == num:
            result.append(num)
    return result


print(sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
print(sum_dig_pow(10, 89),  [89])
print(sum_dig_pow(90, 100), [])