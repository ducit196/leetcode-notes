from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def feasible(threshold):
            cnt = 1
            curSum = 0
            for num in  nums:
                curSum += num
                if curSum > threshold:
                    cnt += 1
                    curSum = num
                if cnt > k:
                    return False
            return True

        left = max(nums)
        right = sum(nums)
        ans = 0
        while left <= right:
            mid = left + (right - left) // 2
            if feasible(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
nums = [7,2,5,10,8]
k = 2
print(Solution().splitArray(nums, k))