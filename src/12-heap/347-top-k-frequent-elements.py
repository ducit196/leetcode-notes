from heapq import heapify, heappop
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Idea: count frequent of all element
        #Put all to max heap, value first
        #While loop k, pop the top
        #TC: O(k*nlog(n))
        #SC: O(n)
        counts = Counter(nums)
        ans = []
        heap = [(-v, k) for k, v in counts.items()]
        heapify(heap)
        while k > 0 and heap:
            l, r = heappop(heap)
            ans.append(r)
            k -= 1
        return ans

        return ans
nums = [1,1,1,2,2,3]
k = 2
ans = Solution().topKFrequent(nums, k)
print(ans)