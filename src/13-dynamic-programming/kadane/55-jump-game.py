from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #Kadane at each element, find max reach
        maxReach = 0
        n = len(nums)
        for i in range(n):
            if i > maxReach:
                return False
            maxReach = max(i, maxReach + nums[i])
            if maxReach > n - 1:
                return True
        return True

nums = [2,3,1,1,4]
print(Solution().canJump(nums))