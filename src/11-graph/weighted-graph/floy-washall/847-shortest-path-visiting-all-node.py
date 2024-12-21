from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        #initate d
        d = [[float('inf')for i in range(n)] for j in range(n)]

        #Cal distance
        for i in range(n):
            for j in graph[i]:
                d[i][j] = 1

        #Floyed warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if d[i][j] > d[i][k] + d[k][j]:
                        d[i][j] = d[i][k] + d[k][j]
        #Call ans
        shortestPath = float('inf')
        #BFS to find shortest path




graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
ans = Solution().shortestPathLength(graph)
print(ans)