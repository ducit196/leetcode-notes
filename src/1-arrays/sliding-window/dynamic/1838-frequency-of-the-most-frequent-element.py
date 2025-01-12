from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        left = 0
        sum = 0
        ans = 0
        for right in range(n):
            sum += nums[right]
            while nums[right] * (right - left + 1) > sum + k:   #While invalid(), shrink left until valid again
                sum -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans

nums = [3,9,6]
k = 2
print(Solution().maxFrequency(nums, k))