
from typing import List

from show_recursion_tree import show_recursion_tree


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def choose(start, currentPath):
            if sum(currentPath) == target:
                ans.append(currentPath.copy())
                return
            if sum(currentPath) > target:
                return
            for i in range(start, len(candidates)):
                currentPath.append(candidates[i])
                choose(i, currentPath)
                currentPath.pop()
        choose(0, [])
        return ans


print(Solution().combinationSum([2,3,6,7], 7))

