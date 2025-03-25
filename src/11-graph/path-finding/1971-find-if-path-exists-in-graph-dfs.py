from collections import deque
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #changee edges list to adjList
        adjList = [[] * n]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        visited = set()
        def dfs(node):
            if node in visited:
                return
            if node == destination:
                return True
            visited.add(node)
            for neighbor in adjList[node]:
                return dfs(neighbor)
            return False
        return dfs(source)
n = 1
edges = []
source = 0
destination = 0
print(Solution().validPath(n, edges, source, destination))