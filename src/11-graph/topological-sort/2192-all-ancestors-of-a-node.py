from collections import deque
from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        #Call cal adj list and degree
        #Topological sort, keep track ancestor
        #TC: O(n)
        #SC: O(n)
        adjList = [[] for i in range(n)]
        degreeList = [0] * n
        ancestors = [set() for _ in range(n)]
        for u, v in edges:
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
        ans = [[] for _ in range(n)]
        for i in range(n):
            ans[i] = list(sorted(ancestors[i]))
        return ans
n = 8
edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
ans = Solution().getAncestors(n, edgeList)
print(ans)

