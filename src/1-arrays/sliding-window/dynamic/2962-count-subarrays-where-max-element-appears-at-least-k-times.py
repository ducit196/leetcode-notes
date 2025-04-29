from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # maxNum = max(nums)
        # left = 0
        # ans = 0
        # maxCnt = 0
        # for i in range(n):
        #     if nums[i] == maxNum:
        #         maxCnt += 1
        #     while maxCnt >= k:
        #         print(i)
        #         ans += n - i
        #         if nums[left] == maxNum:
        #             maxCnt -= 1
        #         left += 1
        # return ans
        #bruce force
        n = len(nums)
        maxNum = max(nums)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                print(nums[i:j + 1])
                if sum(1 for v in nums[i:j + 1] if v == maxNum) >= k:
                    ans += 1
        return ans



nums = [1,3,2,3,3]
k = 2
print(Solution().countSubarrays(nums, k))