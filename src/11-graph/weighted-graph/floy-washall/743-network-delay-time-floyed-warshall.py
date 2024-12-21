from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Resolve using floyed-warshall

        #Initiate
        d = [[float('inf') for i in range(n)] for j in range(n)]
        for u, v, w in times:
            d[u - 1][v - 1] = w
        for h in range(n):
            for i in range(n):
                for j in range(n):
                    if d[i][j] > d[i][h] + d[h][j]:
                        d[i][j] = d[i][h] + d[h][j]
        ans = 0
        for i in range(n):
            if i != k - 1:
                ans = max(ans, d[k - 1][i])
        if ans == float('inf'):
            return -1
        return ans



times = [[1,2,1],[2,1,3]]
n = 2
k = 2
print(Solution().networkDelayTime(times, n, k))