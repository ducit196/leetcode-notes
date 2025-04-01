# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def merge(nums):
            if len(nums) == 0:
                return None
            if len(nums) == 1:
                return TreeNode(nums[0])
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = merge(nums[0:mid])
            root.right = merge(nums[(mid + 1): (len(nums))])
            return root

        return merge(nums)
nums = [-10,-3,0,5,9]
print(Solution().sortedArrayToBST(nums))