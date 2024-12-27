from heapq import heappush, heappop
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []
        for i in range(n - 1):
            if heights[i] >= heights[i + 1]:
                continue
            delta = heights[i + 1] - heights[i]
            heappush(heap, -1 * delta)
            if bricks >= delta:
                bricks -= delta
                continue
            elif ladders > 0:
                ladders -= 1
                bricks += -1 * heappop(heap) - delta
                continue
            else:
                return i
        return n - 1
heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1
ans = Solution().furthestBuilding(heights, bricks, ladders)
print(ans)