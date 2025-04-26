from heapq import heapify, heappop
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #using heap
        nums = [nums[i] * -1 for i in range(len(nums))]
        heapify(nums)
        for i in range(k - 1):
            heappop(nums)
        return -nums[0]
nums = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(nums, k))