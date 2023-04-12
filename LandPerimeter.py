"""
Given an array arr of strings, complete the function by calculating the total
perimeter of all the islands. Each piece of land will be marked with 'X' while the
water fields are represented as 'O'. Consider each tile being a perfect 1 x 1 piece of land.
Some examples for better visualization:
"""

def land_perimeter(arr):
  perimetr=0
  height=len(arr)
  for y in range(height):
    width=len(arr[y])
    for x in range(width):
      if arr[y][x]=='X':
        if x==0 or arr[y][x-1]=='O':perimetr+=1
        if x==width-1 or arr[y][x+1]=='O':perimetr+=1
        if y==0 or arr[y-1][x]=='O':perimetr+=1
        if y==height-1 or arr[y+1][x]=='O':perimetr+=1
  return 'Total land perimeter: '+str(perimetr)