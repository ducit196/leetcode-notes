from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]):
        #same as 785, change edge list to adjacent list. Then color solution
        #TC: O(N)
        #SC: O(N)
        adjacents = [[] for i in range(n)]
        for e in dislikes:
            adjacents[e[0] - 1].append(e[1] - 1)
            adjacents[e[1] - 1].append(e[0] - 1)
        print(adjacents)
        WHITE, BLACK, RED = -1, 0, 1
        color = [WHITE] * n
        ans = True
        def dfs(u: int, nextColor: int):
            nonlocal ans
            color[u] = nextColor
            for v in adjacents[u]:
                if color[v] == color[u]:
                    ans = False
                    return
                elif color[v] == WHITE:
                    dfs(v, 1 - nextColor)
                else:
                    pass

        for i in range(n):
            if color[i] == WHITE:
                dfs(i, RED)
        return ans

dislikes =  [[1,2],[1,3],[2,4]]
ans = Solution().possibleBipartition(4, dislikes)
print(ans)