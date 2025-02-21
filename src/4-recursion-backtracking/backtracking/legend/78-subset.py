from typing import List

from show_recursion_tree import show_recursion_tree


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #[1,2,3] [],
        n = len(nums)
        ans = []

        def choose(i, currentSolution):
            ans.append(currentSolution.copy())
            for j in range(i, n):
                currentSolution.append(nums[j])
                print(f'Input {j + 1} : {currentSolution}')
                choose(j + 1, currentSolution)
                currentSolution.pop()
        choose(0, [])
        return ans
print(Solution().subsets([1,2,3]))