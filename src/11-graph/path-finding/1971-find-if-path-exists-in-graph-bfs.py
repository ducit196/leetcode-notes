from collections import deque
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = [[] for i in range(n)]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        q = deque()
        q.append(source)
        visited = set()
        while q:
            current = q.popleft()
            if current == source == destination:
                return True
            visited.add(current)
            for neighbor in adjList[current]:
                if neighbor == destination:
                    return True
                if neighbor not in visited:
                    q.append(neighbor)
        return False
n = 1
edges = []
source = 0
destination = 0
print(Solution().validPath(n, edges, source, destination))