import math
from collections import deque
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        d1 = [math.inf] * n
        d2 = [math.inf] * n

        def bfs(start, d):
            q = deque([start])
            d[start] = 0
            visited = set()
            while q:
                curNode = q.popleft()
                visited.add(curNode)
                nei = edges[curNode]
                if nei != -1 and nei not in visited:
                    d[nei] = d[curNode] + 1
                    q.append(nei)


        bfs(node1, d1)
        bfs(node2, d2)
        print(d1)
        print(d2)
        minD = math.inf
        ans = -1
        for i in range(n):
            if minD > max(d1[i], d2[i]):
                ans = i
                minD = max(d1[i], d2[i])
        return ans
edges = [2,2,3,-1]
node1 = 0
node2 = 1
print(Solution().closestMeetingNode(edges, node1, node2))