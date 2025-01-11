from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        # Brute force
        # for i in range(k):
        #     tmp = nums[-1]
        #     for j in range(n - 1, 0, -1):
        #         nums[j] = nums[j - 1]
        #     nums[0] = tmp

        # Auxiliary array
        # tmp = [0] * n
        # for i in range(n):
        #     tmp[(i + k) % n] = nums[i]  #After rotate k time, nums[i] move to nums[(i + k) % n]
        # nums[:] = tmp

        # Reverse array, no extra
        def reverseArr(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # After reverse array k times
        # Array will be: reverse all element, reverse first k element, reverse last k element
        reverseArr(0, n - 1)
        reverseArr(0, k - 1)
        reverseArr(k, n - 1)
nums = [1,2,3,4,5,6,7]
k = 3
print(Solution().rotate(nums, k))