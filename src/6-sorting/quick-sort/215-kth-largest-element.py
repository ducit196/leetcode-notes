import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #quick select algorithm
        #
        def quickSelect(nums, k):
            left, mid, right = [], [], []
            pivot = random.choice(nums)
            for i in nums:
                if i > pivot:
                    left.append(i)
                elif i < pivot:
                    right.append(i)
                else:
                    mid.append(i)
            if len(left) >= k:
                return quickSelect(left, k)
            elif len(left) + len(mid) < k:
                return quickSelect(right, k - len(left) - len(mid))
            else:
                return pivot
        return quickSelect(nums, k)

nums = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(nums, 2))
