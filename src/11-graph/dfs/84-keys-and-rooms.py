from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        def dfs(v):
            if v not in visited:
                visited.add(v)
                for u in rooms[v]:
                    if u not in visited:
                        dfs(u)
        dfs(0)
        return len(visited) == n

rooms = [[1],[2],[3],[]]
print(Solution().canVisitAllRooms(rooms))