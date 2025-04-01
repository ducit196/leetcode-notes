from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def dfs(root, level):
            if root == None:
                return
            if level >= len(ans):
                ans.append([root.val])
            else:
                ans[level].append(root.val)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        dfs(root, 0)
        return ans
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(Solution().levelOrder(root))