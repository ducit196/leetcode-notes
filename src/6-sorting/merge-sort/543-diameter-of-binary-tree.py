from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #max heigh of left and right at any time
        ans = 0
        def dfs(root):
            nonlocal ans
            if root == None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            ans = max(ans, left + right)
            return max(left, right) + 1
        dfs(root)
        return ans
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(Solution().diameterOfBinaryTree(root))