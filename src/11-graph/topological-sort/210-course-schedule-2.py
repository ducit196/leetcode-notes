from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        degree = [0] * numCourses
        adjList = [[] for i in range(n)]

        #Calculate
        for edge in prerequisites:
            adjList[edge[1]].append(edge[0])
            degree[edge[0]] = degree[edge[0]] + 1
        q = deque()
        ans = []
        for i in range(n):
            if degree[i] == 0:
                q.append(i)
        while q:
            currentNode = q.popleft()
            ans.append(currentNode)
            for neighbor in adjList[currentNode]:
                degree[neighbor] = degree[neighbor] - 1
                if degree[neighbor] == 0:
                    q.append(neighbor)
        if len(ans) != n:
            return []
        return ans
numCourses = 2
prerequisites = [[1,0]]
ans = Solution().findOrder(numCourses, prerequisites)
print(ans)

