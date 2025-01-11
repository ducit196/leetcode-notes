from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n - 1] = True
        for i in range(n - 1, -1, -1):
            if nums[i - 1] > 0:
                nums[i] == 1
        return dp[n - 2]
nums = [2,0]
print(Solution().canJump(nums))