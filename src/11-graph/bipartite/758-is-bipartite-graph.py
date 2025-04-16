from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #color algorithm
        #Color for current node, neighbor node is differen, if there is any conflict -> false. Else return true
        n = len(graph)
        colored = [0] * n   #0, 1 , 2
        def dfs(v, color):
            if colored[v] != 0:
                return color == colored[v]
            colored[v] = color
            nextColor = 2 if color == 1 else 1
            for nei in graph[v]:
                #if colored[neigh] == 0
                return dfs(nei, nextColor)
        for i in range(n):
            if colored[i] == 0:
                if dfs(i, 1) == False:
                    return False
        return True
nums = [[1,2,3],[0,2],[0,1,3],[0,2]]
print(Solution().isBipartite(nums))