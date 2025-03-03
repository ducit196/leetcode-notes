from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findPosition(isFirst):
            left = 0
            right = len(nums) - 1
            ans = -1
            while left <= right:
                mid = left + (right- left) // 2
                if nums[mid] == target:
                    ans = mid
                    if isFirst:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return ans
        return [findPosition(True), findPosition(False)]
nums = [5,7,7,8,8,10]
target = 8
print(Solution().searchRange(nums, target))