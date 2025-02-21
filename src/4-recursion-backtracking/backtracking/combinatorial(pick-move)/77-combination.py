from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def choose(start, currentPath):
            if len(currentPath) == k:
                ans.append(currentPath.copy())
            for i in range(start, n):
                currentPath.append(i + 1)
                choose(i + 1, currentPath)
                currentPath.pop()
        choose(0, [])
        return ans
print(Solution().combine(4,2))