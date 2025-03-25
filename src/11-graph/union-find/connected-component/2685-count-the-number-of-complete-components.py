from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [-1] * n
        edgeCount = [0] * n
        nodeCount = [1] * n
        def union(i, j):
            parent[j] = i
            nodeCount[i] += nodeCount[j]
            edgeCount[i] += edgeCount[j]
            edgeCount[i] += 1
        def find(i):
            root = i
            while parent[root] != -1:
                root = parent[root]
            #path compress
            while i != root:
                temp = parent[i]
                parent[i] = root
                i = temp
            return root
        for u, v in edges:
            x = find(u)
            y = find(v)
            if x != y:
                union(x, y)
            else:
                edgeCount[x] += 1
        count = 0

        for i in range(n):
            count += 1 if parent[i] == -1 and edgeCount[i] == (nodeCount[i] * (nodeCount[i] - 1)) // 2 else 0
        return count
n = 6
edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
print(Solution().countCompleteComponents(n, edges))