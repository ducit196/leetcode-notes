from typing import List


class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        #use next greater element
        n = len(nums)
        ans = [0] * n
        monoStack = []
        for i in range(n):
            while monoStack and nums[i] > nums[monoStack[-1]]:
                index = monoStack.pop()
                ans[index] = i - index
            monoStack.append(i)
        return ans