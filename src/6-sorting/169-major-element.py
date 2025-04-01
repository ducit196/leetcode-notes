from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote = 0
        candidate = -1
        for i in range(len(nums)):
            if vote == 0:
                candidate = nums[i]
                vote += 1
            else:
                if nums[i] == candidate:
                    vote += 1
                else:
                    vote -= 1
        count = 0
        for i in range(len(nums)):
            count += 1 if nums[i] == candidate else 0
        return candidate if count > len(nums) // 2 else -1