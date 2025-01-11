import math
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        currentSum = 0
        ans = math.inf
        for right in range(n):
            currentSum += nums[right]
            while currentSum >= target and left <= right:
                ans = min(ans, right - left + 1)
                currentSum -= nums[left]
                left += 1
        return 0 if ans == math.inf else ans

target = 7
nums = [2,3,1,2,4,3]
print(Solution().minSubArrayLen(target, nums))