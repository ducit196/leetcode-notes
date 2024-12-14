from collections import deque
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []
        q = deque()
        q.append([0])
        while q:
            currentPath = q.popleft()
            if currentPath[-1] == n - 1:
                ans.append(currentPath) #add a copy of currentPath
            else:
                for neighbor in graph[currentPath[-1]]:
                    q.append(currentPath + [neighbor])

        return ans
graph = [[4,3,1],[3,2,4],[3],[4],[]]

ans = Solution().allPathsSourceTarget(graph)
print(ans)
