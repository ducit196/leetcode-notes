from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        visited = set()
        ans = []
        currentPath = [0]
        def dfs(u: int):
            if u == n - 1:
                ans.append(currentPath.copy())
                return
            visited.add(u)
            for v in graph[u]:
                if v not in visited:
                    currentPath.append(v)
                    dfs(v)
                    currentPath.pop()
            visited.remove(u)
        dfs(0)
        return ans

graph = [[1,2], [3], [3], []]
ans = Solution().allPathsSourceTarget(graph)
# print(ans)