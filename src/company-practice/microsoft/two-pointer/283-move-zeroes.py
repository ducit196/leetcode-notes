from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = 0
        for i in range(n):
            if nums[i] != 0:
                nums[left] = nums[i]
                left += 1
        for i in range(left, n):
            nums[i] = 0

        print(nums)

nums = [0,1,0,3,12]
Solution().moveZeroes(nums)
