from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        left = 0
        indexPivot = 0
        for i in range(n):
            if nums[i] == pivot:
                indexPivot = i
                break
        nums[indexPivot], nums[n - 1] = nums[n - 1], nums[indexPivot]
        for i in range(n):
            if nums[i] < nums[n - 1]:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        nums[left], nums[n - 1] = nums[n - 1], nums[left]
        return nums

nums = [9,12,5,10,14,3]
pivot = 10
print(Solution().pivotArray(nums, pivot))