"""
Given two arrays a and b write a function comp(a, b) (orcompSame(a, b))
that checks whether the two arrays have the "same" elements, with the same
multiplicities (the multiplicity of a member is the number of times it appears).
"Same" means, here, that the elements in b are the elements in a squared, regardless of the order
"""

def comp(arr1, arr2):
    arr1.sort()
    arr2.sort()

    if len(arr1) != len(arr2):
    	return False

    for index, letter in enumerate(arr2):

    	if arr1[index]**2 != letter:
    		return False

    return True

print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]) == True)
print(comp([121, 144, 19, 161, 19, 144, 19, 9], [121, 14641, 20736, 361, 25921, 361, 20736, 361]) == False)

