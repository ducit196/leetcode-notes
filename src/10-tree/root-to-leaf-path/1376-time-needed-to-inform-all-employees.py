from collections import deque
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        #build tree from the array
        #find max root to leaf

        #build adj list
        adjList = [[] for i in range(n)]
        for i in range(n):
            if manager[i] != -1:
                adjList[manager[i]].append(i)
        q = deque()
        q.append((headID, 0))
        ans = 0
        while q:
            curNode, curTime = q.popleft()
            ans = max(ans, curTime)
            for c in adjList[curNode]:
                q.append((c, curTime + informTime[curNode]))
        return ans