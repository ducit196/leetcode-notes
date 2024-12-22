from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        #Build union find function
        parents = [-1 for i in range(n)]

        def union(i: int, j: int):
            parents[i] = j
        def find(i: int):
            root = i
            while parents[root] != -1:
                root = parents[root]
            #Update all parent in the path = root
            while i != root:
                u = parents[i]  #to update parents[i] = root, need to temporary assign u = parents[i]
                parents[i] = root
                i = u
            return root

        #Repesent all point as a graph
        #Build a edge list
        edgeList = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edgeList.append((i, j, dist))
        #Sort by weight
        edgeList.sort(key=lambda x: x[2])

        #Union until has enough vertex or out of edges
        edgeCount = 0
        ans = 0
        for u, v, w in edgeList:
            ru = find(u)
            rv = find(v)
            if ru != rv:
                union(ru, rv)
                ans += w
                edgeCount += 1
                if edgeCount == n - 1:
                    return ans
        return 0
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
ans = Solution().minCostConnectPoints(points)
print(ans)