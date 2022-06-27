'''
Given a string of letters a, b, n how many different ways can you make the word "banana"
by crossing out various letters and then reading left-to-right?
'''

from Amain import timeComplete

@timeComplete
def bananas(s):

    search_word = 'banana'
    single_result = []
    search_map = [[] for i in range(6)]

    for i, letter_in_s  in enumerate(search_word):
        
        counter = 0
        for j, letter in enumerate(s):
            
            if letter == letter_in_s and len(s) - j >= len(search_word) - i and j >= i:

                single_result.append('-' * (counter) + letter)
            
            counter += 1
        
        else:

            counter = 0
            if single_result:
                search_map[i] += single_result
            single_result = []


    result = []

    back_map = search_map[0]
    for i, map in enumerate(search_map[1:]):

        result = determine_map(back_map, map)
        back_map = result


    for i in range(len(result)):
        if len(result[i]) != len(s):
            result[i] += '-' * (len(s) - len(result[i]))


    return list(set(result))

    
def determine_map(map1, map2):
    
    result = []
    for map1_l in map1:
        for map2_l in map2: 
            if len(map1_l) < len(map2_l):
                result.append(map1_l + map2_l[len(map1_l):])

    return result


print(len(bananas("bbaannaannnabbaannaannnabbaannaannnabbaannaannnabbaannaannnabbaannaannnabbaannaannnabbaannaannna")))



