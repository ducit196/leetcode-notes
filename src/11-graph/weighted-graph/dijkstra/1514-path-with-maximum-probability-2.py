from heapq import heappush, heappop
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        #dijitstra but find maximum --> min heap with negative value
        d = [0] * n
        adjList = [[] for i in range(n)]

        for i, (u, v) in enumerate(edges):
            adjList[u].append((succProb[i], v))
            adjList[v].append((succProb[i], u))
        print(adjList)

        q = [(1, start_node)]
        d[start_node] = 1
        visited = set()
        while q:
            wu, u = heappop(q)
            if u in visited:
                continue
            for wNei, nei in adjList[u]:
                if nei not in visited and d[u] * wNei > d[nei]:
                    d[nei] = d[u] * wNei
                    heappush(q, (-d[nei], nei))
        return d[end_node]
n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2
ans = Solution().maxProbability(n, edges, succProb, start, end)
print(ans)