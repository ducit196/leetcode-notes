from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visisted = set()
        m = len(grid)
        n = len(grid[0])
        ans = 0

        def dfs(i, j):
            visisted.add((i, j))
            val = 1
            for x, y in directions:
                u = x + i
                v = y + j
                if 0 <= u < m and 0 <= v < n and (u, v) not in visisted and grid[u][v] == '1':
                    val += dfs(u, v)
            return val
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visisted:
                    ans = max(ans, dfs(i, j))
        return ans
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(Solution().numIslands(grid))