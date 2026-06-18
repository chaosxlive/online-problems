package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteMiddle(head *ListNode) *ListNode {
	fast := head
	slow := head
	var prev *ListNode

	if head == nil || head.Next == nil {
		return nil
	}

	for {
		fast = fast.Next
		if fast == nil {
			prev.Next = slow.Next
			break
		}
		prev = slow
		slow = slow.Next
		fast = fast.Next

		if fast == nil {
			prev.Next = slow.Next
			break
		}
	}

	return head
}
