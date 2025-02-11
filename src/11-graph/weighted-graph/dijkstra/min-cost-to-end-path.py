
from heapq import heappush, heappop
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # Dijkstra
        fixed = set()
        heap = []
        heappush(heap, (0, 0, 0))
        m = len(grid)
        n = len(grid[0])
        #2d result
        d = [[float('inf')] * n for _ in range(m)]
        direction = [(0, 1, 1), (0, -1, 2),(1, 0, 3), (-1, 0, 4)]
        #right = 1
        #left = 2
        #down = 3
        # up = 4
        d[0][0] = 0
        while heap:
            dc, r, c = heappop(heap)
            if (r, c) in fixed:
                continue
            fixed.add((r, c))
            for x, y, w in direction:
                neighborR = r + x
                neighborC = c + y
                weight = 0 if grid[r][c] == w else 1 #if current cell equal to direction label --> cost = 0
                if (neighborR, neighborC) not in fixed and 0 <= neighborR < m and 0 <= neighborC < n and d[r][c] + weight < d[neighborR][neighborC]:
                    d[neighborR][neighborC] = d[r][c] + weight
                    heappush(heap, (d[neighborR][neighborC], neighborR, neighborC))
        return d[-1][-1]

grid = [[1,4,1,1], [2,2,2,2],[1,1,1,1],[2,2,2,2]]
print(Solution().minCost(grid))