'''
Given a string of letters a, b, n how many different ways can you make the word "banana"
by crossing out various letters and then reading left-to-right?
'''

def bananas(s):

    search_word = 'banana'
    single_result = []
    search_map = [[] for i in range(6)]

    for i, letter_in_s  in enumerate(search_word):
        
        counter = 0
        for j, letter in enumerate(s):
            
            if letter == letter_in_s and len(s) - j >= len(search_word) - i and j >= i:

                single_result.append('-' * counter + letter)
            
            counter += 1
        
        else:

            counter = 0
            if single_result:
                search_map[i] += single_result
            single_result = []


    result = []

    for i in search_map:
        print(i)

    return search_map

    
def determine_map(map):

    return 



print('bananana', bananas('bananana'))