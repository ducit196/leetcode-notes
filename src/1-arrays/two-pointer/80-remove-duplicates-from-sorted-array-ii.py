from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        left = 2
        for i in range(2, n):
            if nums[i] != nums[left - 2]:
                nums[left]  = nums[i]
                left += 1
        return left

nums = [1,1,1,2,2,3]
print(Solution().removeDuplicates(nums))