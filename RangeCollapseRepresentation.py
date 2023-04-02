"""
A range-collapse representation of an array of integers looks like this: "1,3-6,8",
where 3-6 denotes the range from 3-6, i.e. [3,4,5,6].
Hence "1,3-6,8" = [1,3,4,5,6,8]. Some other range-collapse representations of [1,3,4,5,6,8]
include "1,3-5,6,8", "1,3,4,5,6,8", etc.
Each range is written in the following format "a-b", where a < b,
and the whole range must belong to the array in an increasing order.
You are given an array arr. Your task is to find the number of different range-collapse
representations of the given array.
"""

def descriptions(arr):
  return 2**len([v for n,v in enumerate(arr) if v==arr[n-1]+1])