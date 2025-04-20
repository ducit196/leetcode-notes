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
            root = i
            while parent[root] != -1:
                root = parent[root]
            while i != root:
                tmp = parent[i]
                parent[i] = root
                i = tmp
            return root
        for u, v in edges:
            pU = find(u - 1)
            pV = find(v - 1)
            if pU != pV:
                union(pU, pV)
            else:
                return [u, v]

edges = [[1,2],[1,3],[2,3]]
ans = Solution().findRedundantConnection(edges)
print(ans)