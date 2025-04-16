from typing import List


class Solution:
    def dfs(self, u, isConnected, visited):
        visited.add(u)
        for v in range(len(isConnected)):
            if isConnected[u][v] == 1 and v not in visited:
                self.dfs(v, isConnected, visited)


    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #1: DFS: each node traverse, increase number if province
        n = len(isConnected)
        visited = set()
        ans = 0
        for i in range(n):
            if i not in visited:
                ans += 1
                self.dfs(i, isConnected, visited)
        return ans

isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
print(Solution().findCircleNum(isConnected))
