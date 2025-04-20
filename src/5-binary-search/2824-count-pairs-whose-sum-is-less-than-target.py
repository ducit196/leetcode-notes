from typing import List


class Solution:
    def upperBound(self, nums, left, right, target):
        ans = left - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n):
            ans += self.upperBound(nums, i + 1, n - 1, target - nums[i]) - i
        return ans
nums = [-1,1,2,3,1]
print(Solution().countPairs(nums, 2))