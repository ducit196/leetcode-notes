from heapq import heapify, heappop
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Idea: put distance to min heap
        #Loop k and add top element to ans
        #TC: O(k * nlogn)
        #TC: O(n)
        d = [(x * x + y * y, x, y) for x, y in points]
        ans = []
        heapify(d)
        while k > 0 and d:
            dis, x, y = heappop(d)
            ans.append([x, y])
            k -= 1
        return ans
points = [[1,3],[-2,2]]
k = 1
print(Solution().kClosest(points, k))