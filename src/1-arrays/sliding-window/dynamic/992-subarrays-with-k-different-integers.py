from collections import defaultdict
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        n = len(nums)

        def countAtMostGoal(goal):
            if goal == 0:
                return 0
            ans = 0
            uniqueCount = defaultdict(int)
            left = 0
            for right in range(n):
                uniqueCount[nums[right]] += 1
                while len(uniqueCount) > goal and left < right:
                    uniqueCount[nums[left]] -= 1
                    if uniqueCount[nums[left]] == 0:
                        del uniqueCount[nums[left]]
                    left += 1
                ans += right - left + 1 #Number of substring end at right from left to right  [1,2,3] -> 3: 123,23,3
            return ans
        return countAtMostGoal(k) - countAtMostGoal(k - 1)
nums = [1,2,1,2,3]
k = 2
print(Solution().subarraysWithKDistinct(nums, k))