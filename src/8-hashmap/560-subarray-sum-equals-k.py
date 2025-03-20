from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #sum[j] - sum[i] == k --> sum[i:j] == k
        ans = 0
        seen = defaultdict(int)
        seen[0] = 1
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            complement = sum - k
            ans += seen[complement]
            seen[sum] += 1
        return ans
k = 3
nums = [1,2,3]
print(Solution().subarraySum(nums, k))