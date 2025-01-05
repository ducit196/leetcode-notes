from typing import List
from xml.sax import parse


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def dp(i, sum):
            if i == n:
                return 1 if sum == target else 0
            subtract = dp(i + 1, sum - nums[i])
            add = dp(i + 1, sum + nums[i])
            return subtract + add
        return dp(0, 0)
nums = [1,1,1,1,1]
target = 3
ans = Solution().findTargetSumWays(nums, target)
print(ans)
