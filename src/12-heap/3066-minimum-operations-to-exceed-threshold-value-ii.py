from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        heapify(nums)
        while nums[0] < k:
            ans += 1
            first = heappop(nums)
            second = heappop(nums)
            heappush(nums, first * 2 + second)
        return ans