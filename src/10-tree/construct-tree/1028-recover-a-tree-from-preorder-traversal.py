from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        index = 0
        n = len(traversal)
        def buildTree(depth):
            nonlocal index
            if index == n:
                return None
            #Count dash
            dash = 0
            while index + dash < n and traversal[index + dash] == '-':
                dash += 1
            if dash != depth:
                return None
            index += dash
            #Extract number
            val = 0
            while index < n and traversal[index].isdigit():
                val = 10 * val + int(traversal[index])
                index += 1
            node = TreeNode(val)
            node.left = buildTree(depth + 1)
            node.right = buildTree(depth + 1)
            return node
        return buildTree(0)

traversel = '1-2--3--4-5--6--7'
print(Solution().recoverFromPreorder(traversel))
