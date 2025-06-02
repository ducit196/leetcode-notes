from collections import deque
from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        #Tree 1: Start from each node, and find all node within k distance
        #Tree 2: Start from each ndoe and find max from k - 1 distance
        m = len(edges1) + 1
        n = len(edges2) + 1

        target1 = [0] * m
        target2 = [0] * n

        adjList1 = [[] for i in range(m)]
        for u,v in edges1:
            adjList1[u].append(v)
            adjList1[v].append(u)

        adjList2 = [[] for j in range(n)]
        for u, v in edges2:
            adjList2[u].append(v)
            adjList2[v].append(u)
        def bfs(start, adjList, threshold):
            if threshold < 0:
                return 0
            if threshold == 0:
                return 1
            ans = 1
            visited = set()
            q = deque([start])
            depth = 0
            while q:
                for i in range(len(q)):
                    curNode = q.popleft()
                    visited.add(start)
                    for nei in adjList[curNode]:
                        if nei not in visited:
                            ans += 1
                            q.append(nei)
                depth += 1
                if depth >= threshold:
                    return ans
            return ans

        for i in range(n):
            target2[i] = bfs(i, adjList2, k - 1)
        maxTarget2 = max(target2)
        for i in range(m):
            target1[i] = bfs(i, adjList1, k) + maxTarget2
        return target1
edges1 = [[0,1],[0,2],[2,3],[2,4]]
edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
k = 2
print((Solution().maxTargetNodes(edges1, edges2, k)))



