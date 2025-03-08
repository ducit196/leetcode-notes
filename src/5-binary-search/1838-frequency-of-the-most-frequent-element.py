from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        #Brute force TLE
        # n = len(nums)
        # nums.sort(reverse=True)
        # ans = 0
        # for i in range(n):
        #     t = k
        #     j = i + 1
        #     while j < n and t + nums[j] >= nums[i]:
        #         t -= nums[i] - nums[j]
        #         j += 1
        #     ans = max(ans, j - i)
        # return ans

        n = len(nums)
        nums.sort()
        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i + 1] = preSum[i] + nums[i]
        ans = 0
        for i in range(n - 1, -1, -1):
            #min j
            left = 0
            right = i
            while left <= right:
                mid = left + (right - left) // 2
                currentAns = i
                currentSum = preSum[i] - preSum[mid]
                if currentSum + k >= nums[i] * (i - mid + 1):
                    currentAns = mid
                    right = mid - 1
                else:
                    left = mid + 1
            ans = max(ans, i - currentAns)
        return ans + 1


nums = [3,6,9]
k = 2
print(Solution().maxFrequency(nums, k))