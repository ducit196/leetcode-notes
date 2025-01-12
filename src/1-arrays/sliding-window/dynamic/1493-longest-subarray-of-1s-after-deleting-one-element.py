from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        zeroCount = 0
        ans = 0
        for right in range(n):
            if nums[right] == 0:
                zeroCount += 1
            while zeroCount > 1 and left < right:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            ans = max(ans, right - left)
        return ans
nums = [0,1,1,1,0,1,1,0,1]
print(Solution().longestSubarray(nums))