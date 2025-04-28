from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction = {(-1, 0), (1, 0), (0, 1), (0, -1)}
        m = len(grid)
        n = len(grid[0])
        visited = set()
        q = deque()
        totalFresh = 0
        for i in range(m):
            for j in range(n):
                totalFresh += 1 if grid[i][j] == 1 else 0
                if grid[i][j] == 2:
                    q.append((i, j))
        ans = 0
        while q:
            curSize = len(q)
            ans += 1
            for i in range(curSize):
                x, y = q.popleft()
                for dx, dy in direction:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        totalFresh -= 1
                        grid[nx][ny] = 2
                        q.append((nx, ny))
                        if totalFresh == 0:
                            return ans
        return ans if totalFresh == 0 else -1
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(Solution().orangesRotting(grid))