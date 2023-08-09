"""
    In this kata, you should calculate the type of triangle
    with three given sides a, b and c (given in any order).
    If each angle is less than 90°, this triangle
    is acute and the function should return 1.
    If one angle is strictly 90°, this triangle
    is right and the function should return 2.
    If one angle is more than 90°, this triangle
    is obtuse and the function should return 3.
    If three sides cannot form a triangle, or one angle is 180°
    (which turns the triangle into a segment) - the function should return 0.
"""

def triangle_type(a, b, c):
  a,b,c = sorted((a,b,c))
  if a+b <= c: return 0
  t = a**2+b**2 - c**2
  if t > 0: return 1
  if t == 0: return 2
  else: return 3