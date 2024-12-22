from collections import deque
from heapq import heappush, heappop
from itertools import count
from typing import List


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 1000000007
        #Idea: using dijkstra to find the shorest path from last node
        #Use DFS to find the path if d[node(j)] > d[node(j + 1)
        #Use memory to cache number of path
        #TC: O(E* Log(V)
        #SC: O(M + N)
        weight = {}
        adjList = [[] for i in range(n + 1)]
        for u, v, w in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            weight[(u, v)] = w
            weight[(v, u)] = w

        fixed = set()
        d = [float('inf') for i in range(n + 1)]
        heap = []
        heappush(heap, (0, n))
        d[n] = 0
        while heap:
            du, u = heappop(heap)
            if u in fixed:
                continue
            fixed.add(u)
            for v in adjList[u]:
                if v not in fixed and d[u] + weight[(u, v)] < d[v]:
                    d[v] = d[u] + weight[(u, v)]
                    heappush(heap, (d[v], v))
        memo = [None for i in range(n + 1)]
        def dfs(node) -> int:
            if memo[node] != None:
                return memo[node]
            if node == n:
                return 1
            count = 0
            for nei in adjList[node]:
                if d[nei] < d[node]:
                    count += dfs(nei)
                    count %= MOD
            memo[node] = count
            return count
        return dfs(1)



n = 5
edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
ans = Solution().countRestrictedPaths(n, edges)
print(ans)


