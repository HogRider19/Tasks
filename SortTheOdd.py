"""
You will be given an array of numbers. You have to sort the odd numbers
in ascending order while leaving the even numbers at their original positions
"""



def sort_array(source_array):
    
    odd_indices = []
    odd_numbers = []
    for index, number in enumerate(source_array):
        if number % 2 != 0:
            odd_indices.append(index)
            odd_numbers.append(number)

    odd_numbers.sort()

    result = source_array
    for index, position in enumerate(odd_indices):
        result[position] = odd_numbers[index]

    return result

    



print(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
print(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
print(sort_array([]),[])