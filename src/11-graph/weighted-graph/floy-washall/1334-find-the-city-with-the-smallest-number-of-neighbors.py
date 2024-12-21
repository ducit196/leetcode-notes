from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        #Find shortest path between all country that <= threshold
        #Find the city has smallest reachable neighbor
        #Using floyd - warshall
        #Step 1: Initiate a matrix to denote distance between edge
        d = [[float('inf') for j in range(n)] for i in range(n)]
        for u,v,w in edges:
            d[u][v] = w
            d[v][u] = w
        print(d)
        #Step 2: Floyd Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if d[i][j] > d[i][k] + d[k][j]:
                        d[i][j] = d[i][k] + d[k][j]
        #d got minimum distance of 1 city to other city now
        ans = None
        minReachable = float('inf')
        for i in range(n):
            reachCount = 0
            for j in range(n):
                if d[i][j] <= distanceThreshold and i != j:
                    reachCount += 1
            if reachCount <= minReachable:
                minReachable = reachCount
                ans = i
        return ans
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
ans = Solution().findTheCity(n, edges, distanceThreshold)
print(ans)
