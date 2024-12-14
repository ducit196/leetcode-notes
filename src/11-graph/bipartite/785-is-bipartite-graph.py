from typing import List

#Assign one color to current vertex
#Assign opposite color to all its neighbor
#Check if conflict, if any neighbor same color as current vertex --> not bipartite
#TC: O(v + e) - v = number of vertex, e = number of edge
#SC: O(2v) - 1 for color array and 1 for recursive stack

class Solution:
    def isBipartiteGraph(self,graph: List[List[int]]) -> bool:
        n = len(graph)
        WHITE, BLACK, RED = -1, 0 ,1
        color = [WHITE] * n #Initiate all vertex yet to color
        ans = True
        def dfs(u: int, colored: int):
            nonlocal ans
            color[u] = colored
            for v in graph[u]:
                if color[v] == color[u]:
                    ans = False # 2 adjacent vertex have same color --> not bipartite graph
                    return
                elif color[v] == WHITE:
                    dfs(v, 1 - colored) #colored different color for this vertex
                else:
                    pass                #different color --> Pass
        for u in range(n):
            if color[u] == WHITE:
                dfs(u, RED)
        return ans
graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
print(Solution().isBipartiteGraph(graph))