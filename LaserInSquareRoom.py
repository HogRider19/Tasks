"""
A laser positioned h units from the ground on the left
wall of a unit square (side = 1) will shoot a ray at an angle
a with the x-axis and it will bounce around the walls until the ray has length l.
Calculate the end coordinate of the laser ray to 3 decimal places and return it as a tuple (x, y).
All values are continuous (restrained to the max accuracy of the floating point in the language).
"""

import math

def laser_coord(h, a, l): 
    a_rad = a/360*2*math.pi
    x_r = math.cos(a_rad)*l
    y_r = math.sin(a_rad)*l + h
    x_r -= math.floor(x_r)
    y_r -= math.floor(y_r)

    x = (1 - x_r)**math.floor(x_r) if x_r >= 1 else x_r
    y = (1 - y_r)**math.floor(y_r) if y_r >= 1 else y_r

    return [x, y]


print(laser_coord(0.5, 0, 2.5) == [ 0.5, 0.5])
print(laser_coord(0, 0, 2) == [0, 0])