from typing import List


class Solution:
    def maxArea(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        left = 0
        right = n - 1
        while left < right:
            ans = max(ans, min(nums[left], nums[right]) * (right - left))
            if nums[left] <= nums[right]:   #Greedy, find better solution
                left += 1
            else:
                right -= 1
        return ans


        #brute force
        # for i in range(n - 1):
        #     for j in range(n):
        #         ans = max(ans, min(nums[i], nums[j]) * (j - i))
        # return ans