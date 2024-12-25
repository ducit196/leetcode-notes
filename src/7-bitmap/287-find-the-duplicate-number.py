from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start = nums[0]
        for i in range(1, len(nums)):
            new = start & nums[i]
            if new == start and start != 1 and nums[i] != 1:
                return nums[i]
        return 1
nums = [1,3,4,2,2]
print(Solution().findDuplicate(nums))
