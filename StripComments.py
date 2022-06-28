"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
Any whitespace at the end of the line should also be stripped out.
"""

def strip_comments(strng, markers):

    str_list = strng.split('\n')

    for index, element in enumerate(str_list):

        index_markers = []
        for marker in markers:
            ind_mar = element.find(marker)
            
            if ind_mar >= 0:

                index_markers.append(ind_mar)
        
        if not index_markers:
            continue

        first_marker = min(index_markers)

        str_list[index] = str_list[index][:first_marker]

    return '\n'.join(map(lambda x: x.rstrip(), str_list))



print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples,', ['#', '!']))