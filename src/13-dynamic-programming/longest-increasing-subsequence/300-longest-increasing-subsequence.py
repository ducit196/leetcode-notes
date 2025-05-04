from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #At every i, find max dp (0 -> i - 1) and nums[j] < nums[i]
        #TC: O(n2)
        #SC: O(n)
        n = len(nums)
        prev = [-1] * n
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        maxLen = max(dp)
        index = dp.index(maxLen)
        ans = []
        while index != -1:
            ans.append(nums[index])
            index = prev[index]
        ans.reverse()
        print(ans)
        return max(dp)
nums = [10,9,2,5,3,7,101,18]
print(Solution().lengthOfLIS(nums))