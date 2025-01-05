# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        #idea: if parent is robbed --> skip both left and right
        #If paren is not robbed --> rob or skip, find max
        #This is 0/1 k knapsack problem
        def dp(root, parenRobbed):
            if root == None:
                return 0
            if parenRobbed:
                return dp(root.left, False) + dp(root.right, False)
            take = dp(root.left, True) + dp(root.right, True) + root.val
            skip = dp(root.left, False) + dp(root.right, False)
            return max(take, skip)
        return dp(root, False)
root = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))
print(Solution().rob(root))