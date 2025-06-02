from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        #Kadane, max of max sum and abs(min sum)
        # currentMaxSum = 0
        # currentMinSum = 0
        # maxSum = 0
        # minSum = 0
        # for i in nums:
        #     currentMaxSum = max(i, currentMaxSum + i)
        #     currentMinSum = min(i, currentMinSum + i)
        #
        #     maxSum = max(maxSum, currentMaxSum)
        #     minSum = min(minSum, currentMinSum)
        # return max(maxSum, abs(minSum))

        #return max sum
        currenMax = 0
        maxSum = 0
        for i in nums:
            currenMax = max(i, currenMax + i)
            maxSum = max(currenMax, maxSum)
        return maxSum
nums = [1,-3,2,3,-4]
print(Solution().maxAbsoluteSum(nums))