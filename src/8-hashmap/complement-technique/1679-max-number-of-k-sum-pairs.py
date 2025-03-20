from collections import defaultdict
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seen  = defaultdict(int)
        ans = 0
        for i in range(n):
            complement = k - nums[i]
            if seen[complement] > 0:
                seen[complement] -= 1
                ans += 1
            else:
                seen[nums[i]] += 1
        print(seen)
        return ans
nums = [1,2,3,4]
k = 5
print(Solution().maxOperations(nums, k))