from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        parent = [-1] * n
        def union(i, j):
            parent[i] = j
        def find(u):
            root = u
            while parent[root] != -1:
                root = parent[root]
            while u != root:
                temp = parent[u]
                parent[u] = root
                u = temp
            return root

        for u, v in edges:
            pu = find(u)
            pv = find(v)
            if pu != pv:
                union(pu, pv)
            else:
                return [u, v]
edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(Solution().findRedundantConnection(edges))
