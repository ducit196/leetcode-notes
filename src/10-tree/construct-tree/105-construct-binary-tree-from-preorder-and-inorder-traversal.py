from shutil import posix
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #find the root
        #from root, lookup left and right in inorder
        n = len(inorder)
        inOrderMap = {}

        #O(1) lookup
        for i in range(n):
            inOrderMap[inorder[i]] = i
        preOrderIndex = 0
        def helper(left, right):    #start and end of whole subtree
            nonlocal preOrderIndex
            if left > right:
                return None
            rootValue = preorder[preOrderIndex]
            preOrderIndex += 1
            root = TreeNode(rootValue)
            inOrderIndex = inOrderMap[rootValue] #find subleft and sub right tree from inorder traversal
            root.left = helper(left, inOrderIndex - 1)
            root.right = helper(inOrderIndex + 1, right)
            return root
        return helper(0, n - 1)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
print(Solution().buildTree(preorder, inorder))