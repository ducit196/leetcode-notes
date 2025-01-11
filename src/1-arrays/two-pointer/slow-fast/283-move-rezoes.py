from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        insertIndex = 0
        for i in range(n):
            if nums[i] != 0:
                nums[insertIndex] = nums[i] #move all non 0 element to left, remaning filled up with 0
                insertIndex += 1
        for i in range(insertIndex, n):
            nums[i] = 0
        print(nums)
nums = [0,1,0,3,12]
Solution().moveZeroes(nums)