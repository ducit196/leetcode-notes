from random import randrange
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        # greater than move to left
        # Less than, move to right
        def greaterThan(num1, num2):
            return str(num1) + str(num2) >  str(num2) + str(num1)

        def quickSort(nums, start, end):

            if start >= end:
                return
            pivot = randrange(start, end + 1)
            pivotVal = nums[pivot]

            left = start
            for i in range(start, end + 1):
                if nums[i] != pivotVal and greaterThan(nums[i], pivotVal):
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
            right = end
            for i in range(end, start - 1, -1):
                if nums[i] != pivotVal and not greaterThan(nums[i], pivotVal):
                    nums[right], nums[i] = nums[i], nums[right]
                    right -= 1
            quickSort(nums, start, left - 1)
            quickSort(nums, right + 1, end)
        quickSort(nums, 0, len(nums) - 1)
        return "".join(nums)

nums = [3,30,34,5,9]
Solution().largestNumber(nums)