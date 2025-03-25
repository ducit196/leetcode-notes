from collections import deque
from typing import List


class Solution:

    #Using topo search algorithm
    # TC: O(m + n) m = number of edge, n = number of vertices
    # SC: O(n)

    #prerequisites = [1, 0]

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        #edge list to adj and cal degree
        degree = [0] * n
        adjList = [[] for i in range(n)]
        for edge in prerequisites:
            degree[edge[0]] = degree[edge[0]] + 1
            adjList[edge[1]].append(edge[0])
        #using BFS, if degree = 0 --> add to the queue
        q = deque()
        for i in range(n):
            if degree[i] == 0:
                q.append(i)
        studied = 0
        while q:
            currentNode = q.popleft()
            studied = studied + 1
            for neighbor in adjList[currentNode]:
                degree[neighbor] = degree[neighbor] - 1
                if degree[neighbor] == 0:
                    q.append(neighbor)
        return studied == n
numCourses = 2
prerequisites = [[1,0],[0,1]]
ans = Solution().canFinish(numCourses, prerequisites)
print(ans)