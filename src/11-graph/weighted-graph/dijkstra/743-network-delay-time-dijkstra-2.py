import math
from collections import deque
from heapq import heappush, heappop
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Resolve using dijkstra
        #edge list to adjlist
        adjList = [[] for i in range(n)]
        for u,v,w in times:
            adjList[u - 1].append((w, v - 1))
        #BFS with priority queue

        #Add start node to queue
        q = []
        q.append((0, k - 1))
        visited = set()
        #initiate shortest path
        d = [math.inf] * n
        d[k - 1] = 0
        while q:
            w, u = heappop(q)   #similar to bfs, but using heappop instead of popleft()
            if u in visited:
                continue
            visited.add(u)
            for neiW, nei in adjList[u]:
                if nei not in visited and d[u] + neiW < d[nei]: #optimize nei distance if currentNode to nei lest then d[nei]
                    d[nei] = d[u] + neiW
                    heappush(q, (d[nei], nei))  #similar to bfs but using heappush instead of append
        return -1 if max(d) == math.inf else max(d)




times =  [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(Solution().networkDelayTime(times, n, k))