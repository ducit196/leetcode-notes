from collections import deque
from typing import List


class Solution:
    def shortestPpathBinaryMatrix(self, grid: List[List[int]]) -> int:

        # TC: O(n^2 * 8)
        # SC: O(n^2)
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)] # 8 directions
        #Using BFS
        #edge case:
        n = len(grid)
        if grid[0][0] != 0:
            return -1;
        dq = deque()
        dq.append((0,0,1)) #x, y, d
        visited = set()
        visited.add((0,0))
        while dq:
            x, y, d = dq.popleft()
            if x == n - 1 and y == n - 1:
                return d
            for (dx, dy) in directions:
                u, v = x + dx, y + dy
                if (0 <= u < n and 0 <= v < n and (u, v) not in visited and grid[u][v] == 0):
                    dq.append((u,v,d + 1))
                    visited.add((u,v))
        return -1
grid = [[0,0,0], [1,1,0], [1,1,0]]
print(Solution().shortestPpathBinaryMatrix(grid))