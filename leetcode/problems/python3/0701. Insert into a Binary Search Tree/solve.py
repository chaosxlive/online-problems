from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:

    # Definition for a binary tree node.
    class TreeNode:

        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


class Solution:

    def insertIntoBST(self, root: Optional['TreeNode'], val: int) -> Optional['TreeNode']:
        if root is None:
            return TreeNode(val)

        ptr = root
        while True:
            if val > ptr.val:
                if ptr.right is None:
                    ptr.right = TreeNode(val)
                    break
                ptr = ptr.right
            else:
                if ptr.left is None:
                    ptr.left = TreeNode(val)
                    break
                ptr = ptr.left

        return root
