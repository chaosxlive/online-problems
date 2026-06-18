from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        node_values = []
        while fast:
            node_values.append(slow.val)
            fast = fast.next.next
            slow = slow.next
        i = len(node_values) - 1
        max_twin_sum = 0
        while i >= 0:
            max_twin_sum = max(max_twin_sum, node_values[i] + slow.val)
            slow = slow.next
            i -= 1
        return max_twin_sum
