from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        #Repace 0 with -1 --> balance array have prefix sum = 0
        #Use a map to store first occur of prefix sum
        #For example at element i. Prefix sum = -2, If element i + 10 prefix sum = -2 also --> From i -> i + 10 maintain a balance array
        n = len(nums)
        for i in range(n):
            nums[i] = -1 if nums[i] == 0 else 1
        seen = {0: -1}
        preSum = 0
        ans = 0
        for i in range(n):
            preSum += nums[i]
            if preSum in seen:
               ans = max(ans, i - seen[preSum])
            else:
                seen[preSum] = i
        return ans
nums = [0,1,0,0,1,0,0]
print(Solution().findMaxLength(nums))