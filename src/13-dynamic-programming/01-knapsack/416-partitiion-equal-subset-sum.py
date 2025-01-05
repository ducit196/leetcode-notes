from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #For each i, either put to subset 1 or subset 2
        #Check if equal
        #Base case i = -1 --> return false
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        #find all possible sum(nice solution)
        # mem = {0}
        # for num in nums:
        #     possibleSum = list(mem)
        #     for p in possibleSum:
        #         mem.add(num + p)
        # return target in mem

        #0-1 knapsack problem
        def dp(i, s):
            if i == 0:
                if s == 0:
                    return True
                else:
                    return False
            return dp(i - 1, s) or dp(i - 1, s - nums[i])
        return dp(len(nums) - 1, target)

nums = [1,2,5]
print(Solution().canPartition(nums))