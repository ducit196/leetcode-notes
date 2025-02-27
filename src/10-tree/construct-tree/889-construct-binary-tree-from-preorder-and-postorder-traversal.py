# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(postorder)

        #For O(1) lookup
        postorderMap = {}
        for i in range(n):
            postorderMap[postorder[i]] = i
        rootIndex = 0
        def helper(start, end):
            nonlocal rootIndex
            if start > end:
                return None
            if rootIndex >= n:
                return None

            rootVal = preorder[rootIndex]
            root = TreeNode(rootVal)
            rootIndex += 1
            if start == end:
                return root

            #left right recursive
            leftSubTreeIndex = postorderMap[preorder[rootIndex]]
            root.left = helper(start, leftSubTreeIndex)
            root.right = helper(leftSubTreeIndex + 1, end - 1)
            return root