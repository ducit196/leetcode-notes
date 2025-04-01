# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder --> root is first element
        # inorder --> index of root is devide left and right
        rootIndex = 0
        def merge(start, end):
            nonlocal rootIndex
            if start > end:
                return None
            rootVal = preorder[rootIndex]
            rootIndex += 1
            root = TreeNode(rootVal)
            mid = inorder.index(rootVal)
            root.left = merge(start, mid - 1)
            root.right = merge(mid + 1, end)
            return root
        return merge(0, len(preorder) - 1)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

print(Solution().buildTree(preorder, inorder))