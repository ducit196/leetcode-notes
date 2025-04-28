from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        curSum = 0
        left = 0
        for i in range(n):
            curSum += nums[i]
            while curSum * (i - left + 1) >= k:
                curSum -= nums[left]
                left += 1
            ans += (i - left + 1)
        return ans
nums = [2,1,4,3,5]
k = 10
print(Solution().countSubarrays(nums, k))