from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        insertIndex = 1 #maintain index of unique number only
        for i in range(1, n):
            if nums[i] != nums[i - 1]:  #at index i, if I see it different from previous number, it mean first time I see that number --> Uniqye --> add to array at insertIndex
                nums[insertIndex] = nums[i]
                insertIndex += 1
        return insertIndex

nums = [1,1,2]
print(Solution().removeDuplicates(nums))