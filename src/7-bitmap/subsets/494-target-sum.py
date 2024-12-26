from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # n = len(nums)
        # ans = 0
        # for i in range(1 << n):
        #     currentSum = 0
        #     for j in range(n):
        #         if (i >> j) & 1 == 1:
        #             currentSum += nums[j]
        #         else:
        #             currentSum -= nums[j]
        #     if currentSum == target:
        #         ans += 1
        # return ans
        a = 11
        print(~a + 1)
        num = -2
        num & (2 ** 32 - 1)
        print(num)
        return 1


nums = [1,1,1,1,1]
target = 3
ans = Solution().findTargetSumWays(nums, target)
print(ans)
