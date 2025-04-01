from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(root, path):
            if root == None:
                return
            reversed()
            path.append(str(root.val))
            if root.left == None and root.right == None:
                ans.append('->'.join(path.copy()))
                # return
            else:
                dfs(root.left, path)
                dfs(root.right, path)
            path.pop()
        dfs(root, [])
        print(ans)
root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
print(Solution().binaryTreePaths(root))