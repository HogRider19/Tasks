// You are given two non-empty linked lists representing two non-negative integers.
// The digits are stored in reverse order, and each of their nodes contains
// a single digit. Add the two numbers and return the sum as a linked list

package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {

	res := &ListNode{}
	pointer := res
	carry := 0

	for l1 != nil || l2 != nil {
		sum := carry

		if l1 != nil {
			sum += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			sum += l2.Val
			l2 = l2.Next
		}

		pointer.Val = sum % 10
		carry = int(sum / 10)

		l := &ListNode{}
		pointer.Next = l

	}

	if carry != 0 {
		l := &ListNode{}
		l.Val = carry
		pointer.Next = l
	}
	return res
}
