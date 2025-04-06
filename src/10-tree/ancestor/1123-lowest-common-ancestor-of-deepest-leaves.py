from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root, depth):
            if root == None:
                return (root, depth)
            leftRoot, leftDepth = dfs(root.left, depth + 1)
            rightRoot, rightDepth = dfs(root.right, depth + 1)
            if leftDepth > rightDepth:
                return (leftRoot, leftDepth)
            elif leftDepth < rightDepth:
                return (rightRoot, rightDepth)
            else:
                return (root, leftDepth)

        lcaRoot, depth = dfs(root, 0)
        return lcaRoot

root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
print(Solution().lcaDeepestLeaves(root))