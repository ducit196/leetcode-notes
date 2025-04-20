from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # dfs to find all cell of first island
        # bfs by layer until reach the other island
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        m = len(grid)
        n = len(grid[0])
        visited = set()
        found = False

        q = deque()
        for i in range(m):
            for j in range(n):
                if found == False and grid[i][j] == 1:
                    self.dfs(i, j, m, n, q, grid, visited)
                    found = True
        ans = 1
        while q:
            curSize = len(q)
            for i in range(0, curSize):
                curX, curY = q.popleft()
                for x, y in directions:
                    neiX = curX + x
                    neiY = curY + y
                    if grid[neiX][neiY] == 1:
                        return ans
                    q.append((neiX, neiY))
            ans += 1
        return -1


    def dfs(self, i, j, m, n, q, grid, visited):
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited.add((i, j))
        q.append((i, j))
        for x, y in directions:
            u = i + x
            v = j + y
            if 0 <= u < m and 0 <= v < n and grid[u][v] == 1 and (u, v) not in visited:
                self.dfs(u, v, m, n, q, grid, visited)
grid = [[0,1,0],[0,0,0],[0,0,1]]
print(Solution().shortestBridge(grid))