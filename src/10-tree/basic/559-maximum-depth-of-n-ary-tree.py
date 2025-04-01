from typing import Optional, List


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(root):
            if root == None:
                return 0
            if root.children == None or len(root.children) == 0:
                return 1
            curMax = 0
            for child in root.children:
                depthC = dfs(child)
                curMax = max(curMax, depthC)
            return curMax + 1
        return dfs(root)
root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
print(Solution().maxDepth(root))