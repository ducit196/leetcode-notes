from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Backtracking
        # n = len(nums)
        # ans = []
        # currentSolution = []
        # def choose(i, currentSolution: List[int]):
        #     if i == n:
        #         ans.append(currentSolution.copy())
        #         return
        #
        #     currentSolution.append(nums[i])
        #     choose(i + 1, currentSolution)
        #     currentSolution.pop()
        #
        #     choose(i + 1, currentSolution)
        # choose(0, currentSolution)
        # return ans

        #Bit manipulation
        n = len(nums)
        ans = []
        for i in range(1 << n):
            current = []
            for j in range(n):
                if (i >> j) & 1 == 1:
                    current.append(nums[j])
            ans.append(current)
        return ans
















print(Solution().subsets([1,2,3]))

# Bit manipulation
