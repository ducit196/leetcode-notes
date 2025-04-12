from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n
        maxIndex = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > dp[maxIndex]:
                maxIndex = i
        path = []
        while maxIndex != -1:
            path.append(nums[maxIndex])
            maxIndex = prev[maxIndex]
        path.reverse()
        return path
nums = [1,2,4,8]
print(Solution().largestDivisibleSubset(nums))
