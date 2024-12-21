from heapq import heappush, heappop
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Resolve using dijkstra
        #edge list to adjlist
        adjList = [[] for i in range(n)]
        weight = {}
        for u, v, w in times:
            adjList[u - 1].append(v - 1)
            weight[(u - 1, v - 1)] = w

        # Dijkstra
        fixed = set()
        heap = []
        heappush(heap, (0, k - 1))
        d = [float('inf') for _ in range(n)]
        d[k - 1] = 0
        while heap:
            du, u = heappop(heap)
            if u in fixed:
                continue
            fixed.add(u)
            for v in adjList[u]:
                if v not in fixed and d[u] + weight[(u, v)] < d[v]:
                    d[v] = d[u] + weight[(u, v)]
                    heappush(heap, (d[v], v))
        ans = max(d)
        if ans == float('inf'):
            return -1
        return ans

times = [[1,2,1],[2,3,2],[1,3,4]]
n = 3
k = 1
print(Solution().networkDelayTime(times, n, k))