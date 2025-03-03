from inspect import stack
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums * 2
        monoStack = []
        ans = [-1] * n
        for i in range(len(nums)):
            while monoStack and nums[i] > nums[monoStack[-1]]:
                lastIndex = monoStack.pop()
                ans[lastIndex % n] = nums[i]
            monoStack.append(i)
        return ans

nums = [1,2,3,4,3]
print(Solution().nextGreaterElements(nums))