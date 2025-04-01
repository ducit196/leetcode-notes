# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inOrder = sorted(preorder)
        rootIndex = 0
        def merge(left, right):
            nonlocal rootIndex
            if left > right:
                return None
            root = TreeNode(preorder[rootIndex])
            mid = inOrder.index(preorder[rootIndex])
            rootIndex += 1
            root.left = merge(left, mid - 1)
            root.right = merge(mid + 1, right)
            return root
        return merge(0, len(preorder) - 1)