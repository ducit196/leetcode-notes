from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()
        def dfs(root, parentVal):
            if root == None:
                return
            root.val = parentVal
            self.seen.add(parentVal)
            dfs(root.left, parentVal * 2 + 1)
            dfs(root.right, parentVal * 2 + 2)
        dfs(root, 0)



    def find(self, target: int) -> bool:
        return target in self.seen
# Your FindElements object will be instantiated and called as such:
root = TreeNode(-1, TreeNode(-1, TreeNode(-1), TreeNode(-1)), TreeNode(-1))
obj = FindElements(root)
# param_1 = obj.find(target)