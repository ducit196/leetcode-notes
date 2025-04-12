from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == len(set(nums)):
            return 0
        ans = 0
        i = 0
        while i < n - 2:
            if len(nums[i + 2: n]) == len(set(nums[i + 2: n])):
                break
            ans += 1
            i += 3
        if i < n - 1 and len(nums[i:n]) != len(set(nums[i:n])):
            ans += 1
        return ans
nums = [4,5,6,4,4]
print(Solution().minimumOperations(nums))