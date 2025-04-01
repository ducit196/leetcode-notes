from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        def dfs(root):
            nonlocal ans
            nonlocal k
            if root == None:
                return
            dfs(root.left)
            k -= 1
            if k == 0:
                print(root.val)
                ans = root.val
                return
            dfs(root.right)
        dfs(root)
        return ans
root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print(Solution().kthSmallest(root, 1))