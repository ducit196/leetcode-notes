from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #This is cycle detection
        #Once we meet 2 edge has same root --> cycle --> return
        #Other wise union
        #TC:
        n = len(edges)
        parent = [-1] * n
        def union(i, j):
            parent[i] = j
        def find(i):
            if parent[i] == -1:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        for u, v in edges:
            pU = find(u - 1)
            pV = find(v - 1)
            if pU != pV:
                union(pU, pV)
            else:
                return [u, v]

edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
ans = Solution().findRedundantConnection(edges)
print(ans)