from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        #backtracking
        def sumXor(arr):
            sumXor = 0
            for i in arr:
                sumXor ^= i
        return sumXor

        ans = 0
        n = len(nums)
        def choose(start, curPath):
            nonlocal ans
            ans += sumXor(curPath)
            for i in range(start, n):
                curPath.append(nums[i])
                choose(i + 1, curPath)
                curPath.pop()
        choose(0, [])
        return ans

nums = [1,3]
print(Solution().subsetXORSum(nums))
