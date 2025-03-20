from collections import defaultdict
from typing import List


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        #If:   u and v in diff root --> -1
        #else: Can use all edge in the root
        parent = [-1] * n
        componentWeights = [1] * n
        def union(i, j):
            parent[j] = i
            componentWeights[i] &= componentWeights[j]
        def find(i):
            root = i
            while parent[root] != -1:
                root = parent[root]
            while i != root:
                u = parent[i]
                parent[i] = root
                i = u
            return root
        for i, j, k in edges:
            x = find(i)
            y = find(j)
            if x != y:
                union(x, y)
            componentWeights[x] &= k
        ans = []
        for i, j in query:
            x = find(i)
            y = find(j)
            if x != y:
                ans.append(-1)
            else:
                ans.append(componentWeights[x])
        return ans
n = 5
edges = [[0,1,7],[1,3,7],[1,2,1]]

query = [[0,3],[3,4]]
print(Solution().minimumCost(n, edges, query))