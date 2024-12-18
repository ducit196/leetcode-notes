from typing import List


class Solution:
    #complete component: number of edge = n * (n - 1)/2
    #maintain a list if node count and edges count
    #at the end check if a node is root and edgeCound = nodeCount * (nodeCount - 1) / 2
    #TC: O(n)
    #SC: O(n)
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [-1] * n
        edgeCount = [0] * n
        nodeCount = [1] * n

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
            u = find(i)
            v = find(j)
            edgeCount[u] = edgeCount[u] + 1
            if u != v:
                parent[v] = u
                edgeCount[u] = edgeCount[u] + edgeCount[v]  #acc edge/node count to new root
                nodeCount[u] = nodeCount[u] + nodeCount[v]

        for edge in edges:
            union(edge[0], edge[1])
        count = 0
        for i in range(n):
            edge = edgeCount[i]
            node = nodeCount[i]
            if parent[i] == -1 and edge == node * (node - 1) / 2:   #check if th node is root and satisfy completed component
                count = count + 1
        return count
n = 6
edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
ans = Solution().countCompleteComponents(n, edges)
print(ans)