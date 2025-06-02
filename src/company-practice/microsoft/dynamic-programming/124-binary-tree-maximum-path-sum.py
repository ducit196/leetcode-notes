import math
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -math.inf

        def dfs(root):
            nonlocal maxSum
            if root == None:
                return 0
            leftSum = max(dfs(root.left), 0)
            rightSum = max(dfs(root.right), 0)
            maxSum = max(maxSum, leftSum + rightSum + root.val)
            return max(root.val + leftSum, root.val + rightSum, root.val)  #

        dfs(root)
        return maxSum