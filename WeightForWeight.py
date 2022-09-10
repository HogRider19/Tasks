"""
I am the one who establishes the list so I told him:
"Don't worry any more, I will modify the order of the list".
It was decided to attribute a "weight" to numbers.
The weight of a number will be from now on the sum of its digits
"""


def order_weight(strng: str):
    arr_num = strng.split()
    val_map = []
    for letter in arr_num:
        val_map.append([sum(list(map(lambda x: int(x), letter))), letter])
    val_map.sort()
    return ' '.join(list(map(lambda x: x[1], val_map)))


print(order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")
print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"), "11 11 2000 10003 22 123 1234000 44444444 9999")
print(order_weight(""), "")