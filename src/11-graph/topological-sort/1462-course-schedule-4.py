from collections import deque
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        adjList = [[] for i in range(n)]
        degreeList = [0] * n
        ancestors = [set() for _ in range(n)]
        for u, v in prerequisites:
            adjList[u].append(v)
            degreeList[v] = degreeList[v] + 1
        #BFS and keep track ancestor list
        q = deque()
        #add all 0 degree node to q
        for i in range(n):
            if degreeList[i] == 0:
                q.append(i)
        while q:
            current = q.popleft()
            for neighbor in adjList[current]:
                # Update the neighbor's ancestor set
                ancestors[neighbor].update(ancestors[current])
                ancestors[neighbor].update([current])  # Add the current node itself
                degreeList[neighbor] -= 1
                if degreeList[neighbor] == 0:
                    q.append(neighbor)
        ans = [False] * len(queries)
        for i in  range(len(queries)):
            u, v = queries[i][0], queries[i][1]
            if u in ancestors[v]:
                ans[i] = True
        return ans