from itertools import count
from typing import List


class Solution:
    #union find
    #for each land, increase count, if traverse 4 direction, any neighbor can union --> decrease count
    #TC: O(m * n * 4) - p = length of position
    #TC: O(m * n)

    def numberOfIslands2(self, m: int, n: int, positions: List[List[int]]) ->List[int]:
        parent = [-1] * (m * n)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ans = []
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

        #traverse through all position
        visited = set()
        count = 0
        for p in positions:
            if (p[0], p[1]) in visited:
                ans.append(count)
                continue
            visited.add((p[0], p[1]))
            mappedIndex = p[0] * n + p[1]
            count += 1                      # new land, increase count
            for (dx, dy) in directions:
                u = p[0] + dx
                v = p[1] + dy
                if (u, v) in visited:
                    neighborMappedIndex = u * n + v
                    x = find(mappedIndex)
                    y = find(neighborMappedIndex)
                    if x != y:
                        union(x, y)             #can union with any neighbor -> same island --> decrease count
                        count = count - 1
            ans.append(count)
        return ans
positions = [[0,0],[0,1],[1,2],[1,2]]
ans = Solution().numberOfIslands2(3, 3, positions)
print(ans)


