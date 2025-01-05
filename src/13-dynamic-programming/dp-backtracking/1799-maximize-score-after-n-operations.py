from functools import cache
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        #Idea: each step backtracking all possible pair of i, j. Use bit mask to mark used number
        #Find max at each step
        #TC: O(n ^ 3)
        #SC: O(n)
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        n = len(nums)
        maxOpr = n // 2
        @cache
        def dp(i, usedNumber):
            if i == maxOpr + 1:
                return 0
            ans = 0
            for j in range(n - 1):
                if usedNumber >> j & 1 == 1:
                    continue
                for k in range(j + 1, n):
                    if usedNumber >> k & 1 == 1:
                        continue
                    newUsedNumber = usedNumber | (1 << j) | (1 << k)
                    ans = max(ans, dp(i + 1, newUsedNumber) + i * gcd(nums[j], nums[k]))
            return ans
        return dp(1, 0)
        return dp(1, 0)
nums = [370435,481435,953948,282360,691237,574616,638525,764832]
ans = Solution().maxScore(nums)
print(ans)