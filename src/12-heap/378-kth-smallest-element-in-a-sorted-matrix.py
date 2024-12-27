from heapq import heappush, heapreplace, heappop
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        for i in range(n):
            for j in range(n):
                if len(heap) < k:
                    heappush(heap, -matrix[i][j])
                elif matrix[i][j] < -heap[0]:
                    heapreplace(heap, -matrix[i][j])
        return -heappop(heap)
matrix = [[1,4],[2,5]]
k = 2
ans = Solution().kthSmallest(matrix, k)
print(ans)