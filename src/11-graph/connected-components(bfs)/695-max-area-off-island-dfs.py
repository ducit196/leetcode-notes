from typing import List

class Solution:
    def maxAreaOfIsland(self,grid: List[List[int]]) -> int:
        #grid m x n --> serialize = x * n + y
        directs = [(-1, 0), (0, -1), (1,0), (0, 1)]
        m = len(grid)
        n  = len(grid[0])
        visited = [0] * (m * n)
        def dfs(x: int, y: int) -> int:
            visited[x * n + y] = 1
            area = 1
            for dx, dy in directs:
                xNext = x + dx
                yNext = y + dy
                if 0 <= xNext < m and 0 <= yNext < n and grid[xNext][yNext] == 1 and visited[xNext * n + yNext] == 0:
                    area += dfs(xNext, yNext)
            return area
        ans = 0
        for i in range(m):
            for j in range(n):
                if(visited[i * n + j] == 0 and grid[i][j] == 1):
                    ans = max(ans, dfs(i, j))
        return ans

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
ans = Solution().maxAreaOfIsland(grid)
print(ans)