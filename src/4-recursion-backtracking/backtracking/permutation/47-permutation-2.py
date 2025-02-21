from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        used = [0] * n
        ans = []

        def choose(start, currentPath):
            if start == n:
                ans.append(currentPath.copy())
                return
            for i in range(n):
                if used[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == 0:
                    continue
                used[i] = 1
                currentPath.append(nums[i])
                choose(start + 1, currentPath)
                used[i] = 0
                currentPath.pop()

        choose(0, [])
        return ans
print(Solution().permuteUnique([1,1,2]))


