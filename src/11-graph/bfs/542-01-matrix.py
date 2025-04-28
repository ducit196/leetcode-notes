from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #bfs from 0
        #Done when all 0 --> 1
        directions = {(-1, 0), (1, 0), (0 ,1), (0, -1)}
        m = len(mat)
        n = len(mat[0])
        ans = [[0] * n for i in range(m)]

        q = deque()
        totalOne = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                totalOne += 1 if mat[i][j] == 1 else 0
        print(totalOne)
        curDistance = 0
        while q:
            curDistance += 1
            qSize = len(q)
            for _ in range(qSize):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < m and 0 <= ny < n and mat[nx][ny] == 1:
                        q.append((nx, ny))
                        mat[nx][ny] = 0
                        ans[nx][ny] = curDistance
                        totalOne -= 1
                        if totalOne == 0:
                            return ans
        return ans
mat = [[0,0,0],[0,1,0],[1,1,1]]
print(Solution().updateMatrix(mat))