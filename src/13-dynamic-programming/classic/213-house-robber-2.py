from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:


        def findMax(arr):
            n = len(arr)
            if len(arr) == 0:
                return 0
            if n == 1:
                return arr[0]
            if n == 2:
                return max(arr[0], arr[1])
            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
            return dp[-1]
        n  = len(nums)
        if n == 1:
            return nums[0]
        return max(findMax(nums[0:n-1]), findMax(nums[1:]))

nums = [1]
# nums = [200,3,140,20,10]
print(Solution().rob(nums))