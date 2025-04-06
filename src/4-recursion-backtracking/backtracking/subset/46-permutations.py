from typing import List

from show_recursion_tree import show_recursion_tree


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def choose(i, currentSolution):
            if i == n:
                ans.append(currentSolution.copy())
                return
            for j in range(n):
                if nums[j] not in currentSolution:
                    currentSolution.append(nums[j])
                    choose(i + 1, currentSolution)
                    currentSolution.pop()

        choose(0, [])
        return ans

print(Solution().permute([1,2,3]))