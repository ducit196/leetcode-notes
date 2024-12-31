from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #At every i, find max dp (0 -> i - 1) and nums[j] < nums[i]
        #TC: O(n2)
        #SC: O(n)
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
        return max(dp)
nums = [10,9,2,5,3,7,101,18]
print(Solution().lengthOfLIS(nums))