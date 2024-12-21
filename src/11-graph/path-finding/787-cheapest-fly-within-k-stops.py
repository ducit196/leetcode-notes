from collections import deque
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        return 1
        # adjList = [[] for i in range(n)]
        # weight = {}
        # for u, v, w in flights:
        #     weight[(u, v)] = w
        #     adjList[u].append(v)
        # q = deque()
        # q.append(src)
        # while q and k > 0:
        #     current = q.popleft()
        #     for neighbor in adjList[current]:
        #