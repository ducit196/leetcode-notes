# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Last element of post order is always root
        # Left of root index in inorder is left subtree
        # Right of root index in inrder os rogjt sub tree

        # Inorder map for fast lookup
        # Look look root index(All value is unique)
        n = len(inorder)
        inorderMap = {}
        for i in range(n):
            inorderMap[inorder[i]] = i

        postOrderIndex = n - 1  # keep track of root index

        def helper(start, end):  # start and end of subtree
            nonlocal postOrderIndex
            if start > end:
                return None

            rootValue = postorder[postOrderIndex]
            root = TreeNode(rootValue)
            postOrderIndex -= 1

            inOrderRootIndex = inorderMap[rootValue]
            root.right = helper(inOrderRootIndex + 1, end)
            root.left = helper(start, inOrderRootIndex - 1)
            return root

        return helper(0, n - 1)

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
print(Solution().buildTree(inorder, postorder))