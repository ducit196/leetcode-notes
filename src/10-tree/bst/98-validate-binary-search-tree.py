# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if root == None:
                return True
            if (root.left == None or root.left.val < root.val) and (root.right == None or root.right.val > root.val):
                return dfs(root.left) and dfs(root.right)
            else:
                return False

        return dfs(root)

root = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
print(Solution().isValidBST(root))