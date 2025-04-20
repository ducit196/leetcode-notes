from typing import List


class Solution:
    def lowerBound(self, arr, left, right, target):
        ans = len(arr)
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] >= target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        ans = 0
        nums.sort()
        for i in range(n):
            left = self.lowerBound(nums, i + 1, n - 1, lower - nums[i])
            right = self.lowerBound(nums, i + 1, n - 1, upper - nums[i] + 1)
            ans += right - left
        return ans

nums = [0,1,7,4,4,5]
print(Solution().countFairPairs(nums, 3, 6))