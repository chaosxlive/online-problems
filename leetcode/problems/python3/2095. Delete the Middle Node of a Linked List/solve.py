from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        prev = None

        if head is None or head.next is None:
            return None

        while True:
            fast = fast.next
            if fast is None:
                prev.next = slow.next
                break
            prev = slow
            slow = slow.next
            fast = fast.next
            if fast is None:
                prev.next = slow.next
                break

        return head
