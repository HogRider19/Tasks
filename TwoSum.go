// Given an array of integers nums and an integer target,
// return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution,
// and you may not use the same element twice.
// You can return the answer in any order.

package main

func twoSum(nums []int, target int) []int {
	m := make(map[int]int)

	for index, value := range nums {
		if secIndex, exist := m[value]; exist {
			return []int{index, secIndex}
		}
		m[target-value] = index
	}
	return []int{0, 0}
}
