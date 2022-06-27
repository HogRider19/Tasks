"""
Create a function that takes a positive integer and returns the next bigger
 number that can be formed by rearranging its digits. For example:
"""


def next_bigger(n):

    number = [int(i) for i in str(n)]
   
    len_n = len(number)
     
    k = len_n - 2
    while k >= 0:
        if number[k] < number[k + 1]:
            break
        k -= 1

    if k < 0:
        number = number[::-1]
    else:
       
        for l in range(len_n - 1, k, -1):
            if number[l] > number[k]:
                break
     
        number[l], number[k] = number[k], number[l]
         
        number[k + 1:] = reversed(number[k + 1:])

    result = int(''.join(map(str,number)))

    if result > n:
        return int(''.join(map(str,number)))
    else:
        return -1


print(next_bigger(86))