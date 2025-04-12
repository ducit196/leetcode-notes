from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #Sum[i] - sum[j] == k --> sum[i:j] == k
        n = len(nums)
        seen = defaultdict(int)
        seen[0] = 1
        curSum = 0
        ans = 0
        for i in range(n):
            curSum += nums[i]
            complement = curSum - k
            if complement in seen:
                ans += seen[complement]
            seen[curSum] += 1
        print(seen)
        return ans
nums = [1,2,1,2,1]
print(Solution().subarraySum(nums, 3))