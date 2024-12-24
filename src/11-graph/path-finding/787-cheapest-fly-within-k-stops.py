from collections import deque
from heapq import heappush, heappop
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        #Idea: In heap push cost, vertex and stop. At each vertex has stop to continue of exceed number of stop, priority for other vertex with lesser stop
        #TC: O(K * E * log(V))
        #SC: O((k + 1) * E)


        adjList = [[] for i in range(n)]
        weight = {}
        for u, v, w in flights:
            weight[(u, v)] = w
            adjList[u].append(v)
        heap = []
        #cost, vertex, stop
        heappush(heap, (0, src, 0))
        visited = {}
        while heap:
            cost, u, stop = heappop(heap)
            if u == dst:
                return cost
            if stop > k:
                continue
            for v in adjList[u]:
                newCost = cost + weight[(u, v)] #Dijstra
                if (v, stop) not in visited or newCost < visited[(v, stop)]: #Dijstra variant, not only optimize cost, we choose vertex with lesser stop as well
                    visited[(v, stop)] = newCost
                    heappush(heap, (newCost, v, stop + 1))
        return -1
n = 4
flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dst = 3
k = 1
ans = Solution().findCheapestPrice(n, flights, src, dst, k)
print(ans)