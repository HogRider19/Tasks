package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func detectCycle(head *ListNode) *ListNode {
	m := make(map[*ListNode]bool)
	pointer := head
	for pointer != nil && pointer.Next != nil {
		if _, exist := m[pointer]; exist {
			return pointer
		} else {
			m[pointer] = true
		}
		if pointer.Next == nil {
			return nil
		}
		pointer = pointer.Next
	}
	return nil
}
