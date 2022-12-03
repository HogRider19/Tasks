"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Given a roman numeral, convert it to an integer.
"""


def romanToInt(s: str) -> int:
    roman_numbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    complex_roman_numbers = {
        'IV': 'IIII',
        'IX': 'VIIII',
        'XL': 'XXXX',
        'XC': 'LXXXX',
        'CD': 'CCCC',
        'CM': 'DCCCC',
    }

    transform_st = s
    for rn_key in complex_roman_numbers.keys():
        transform_st = transform_st.replace(rn_key, complex_roman_numbers[rn_key])

    return sum(map(lambda x: roman_numbers.get(x), list(transform_st)))


def tests():
    assert romanToInt("III") == 3
    assert romanToInt("LVIII") == 58
    assert romanToInt("MCMXCIV") == 1994


tests()

