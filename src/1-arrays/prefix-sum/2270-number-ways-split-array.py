from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i + 1] = preSum[i] + nums[i]
        ans = 0
        for i in range(n - 1):
            if preSum[i + 1] - preSum[0] >= preSum[n] - preSum[i + 1]:
                ans += 1
        return ans
nums = [1,1,1,2,3]
print(Solution().waysToSplitArray(nums))
