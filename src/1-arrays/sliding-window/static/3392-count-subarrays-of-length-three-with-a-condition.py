from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        #fixed sliding window
        n = len(nums)
        cnt = 0
        curSum = 0
        for i in range(3):
            curSum += nums[i]
        for i in range(3, n):
            print(f'[-8,8,-8,4]{nums[i - 2] * 1.5} : {curSum}')
            if nums[i - 2] * 1.5 == curSum:
                cnt += 1
            curSum -= nums[i - 3]
            curSum += nums[i]
        print(f'{nums[n - 2] * 1.5} : {curSum}')
        if nums[n - 2] * 1.5 == curSum:
                cnt += 1
        return cnt
nums = [-8,8,-8,4]
print(Solution().countSubarrays(nums))