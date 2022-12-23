"""
Ваша задача — написать функцию, которая принимает неограниченное количество
списков и возвращает только те элементы, что есть в каждом списке
"""

def get_general_items(*args):
    items_map = {item: True for item in sum(args, [])}
    for item in items_map:
        for lst in args:
            if not item in lst:
                items_map[item] = False
    return [item for item, is_general in items_map.items() if is_general]


assert get_general_items([11, 10, 3], [10, 3, 5, 11], [11, 10]) == [11, 10]
assert get_general_items([8, 4, 7, "hi"], [8, "hi"], [4, "hi"]) == ['hi']
assert get_general_items([1, 4, 3], [6, 2, 8], ["4", "hi"]) == []