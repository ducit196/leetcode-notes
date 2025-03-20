from typing import List


class Solution:


    def longestNiceSubarray(self, nums: List[int]) -> int:
        def allZeroPair(l, r):
            for i in range(l, r + 1):
                for j in range(i + 1, r + 1):
                    if nums[i] & nums[j] != 0:
                        return False
            return True

        left = 0
        ans = 1
        for right in range(len(nums)):
            while left < right and not allZeroPair(left, right):
                left += 1
            ans = max(right - left + 1, ans)
        return ans
nums = [744437702,379056602,145555074,392756761,560864007,934981918,113312475,1090,16384,33,217313281,117883195,978927664]
print(Solution().longestNiceSubarray(nums))