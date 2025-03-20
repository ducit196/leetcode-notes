from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Mod(preSum(i)) - mod(presum(j) == 0 --> sum[j:i] % k == 0
        n = len(nums)
        preSum = [0] * (n  + 1)
        for i in range(n):
            preSum[i + 1] = preSum[i] + nums[i]
        for i in range(0, n + 1):
            preSum[i] %= k
        seen = {}
        seen[0] = -1
        for i in range(n):
            if preSum[i + 1] in seen:
                if i - seen[preSum[i + 1]] > 1:
                    return True
            else:
                seen[preSum[i + 1]] = i
        return False
nums = [5,0,0,0]
k = 3
print(Solution().checkSubarraySum(nums, k))