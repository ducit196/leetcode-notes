from heapq import heappush, heappop
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        #Idea: find the longest path from source to destination
        #Using dijkstra algorithm, instead of find min path, find max path
        #In using max heap instead of min heap
        #Edge list to adjList
        #TC: O(E + E*Log(V)) - e = number of edge, v = number of vertices.
            # E* Log(V) - Log(V) for heap
        #SC: O(E) - e = number of edge
        adjList = [[] for i in range(n)]
        for i in range(len(edges)):
            adjList[edges[i][0]].append((edges[i][1], succProb[i]))
            adjList[edges[i][1]].append((edges[i][0], succProb[i]))
        print(adjList)

        #Dijkstra algorithm
        d = [-1] * n    #Initiate max profix
        heap = []
        d[start_node] = 1
        fixed = set()
        heappush(heap, (1, start_node))
        while heap:
            du, u = heappop(heap)
            if u in fixed:
                continue
            fixed.add(u)
            for v, w in adjList[u]:    #neighbor list
                if v not in fixed and d[u] * w > d[v]:
                    d[v] = d[u] * w
                    heappush(heap, (-1 * d[v], v))
        if d[end_node] == -1:
            return 0
        return d[end_node]
n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2
ans = Solution().maxProbability(n, edges, succProb, start, end)
print(ans)