from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #This is cycle detection
        #Once we meet 2 edge has same root --> cycle --> return
        #Other wise union
        #TC:
        n = len(edges)
        parent = [-1] * n

        def find(i: int) ->int:
            root = i
            while parent[root] != -1:
                root = parent[root]

            while i != root:
                u = parent[i]
                parent[i] = root
                i = u
            return root

        def union(i: int, j: int):
            parent[i] = j

        for u, v in edges:
            x = find(u - 1)
            y = find(v - 1)
            if x != y:
                union(x, y)
            else:
                return [u, v]

edges = [[1,2],[1,3],[2,3]]
ans = Solution().findRedundantConnection(edges)
print(ans)