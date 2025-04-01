from collections import deque
from typing import List


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m = len(grid)
        n = len(grid[0])

        def bfs(query):
            count = 0
            q = deque()
            if query > grid[0][0]:
                q.append((0,0))
                count += 1
            visited = set()
            while q:
                x,y = q.popleft()
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                for dx, dy in direction:
                    neiX = x + dx
                    neiY = y + dy
                    print(f"{neiX}, {neiY}")
                    if (neiX, neiY) not in visited and neiX >= 0 and neiX < n and neiY >= 0 and neiY < m and query > grid[neiX][neiY]:
                        count += 1
                        q.append((neiX, neiY))
            return len(visited)
        ans = []
        for q in queries:
            ans.append(bfs(q))
        return ans
grid = [[5,2,1],[1,1,2]]
queries = [3]
print(Solution().maxPoints(grid, queries))