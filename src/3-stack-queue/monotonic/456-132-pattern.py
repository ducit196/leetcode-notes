from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        #From right assum second largest number is - infiniti
        n = len(nums)
        secondLargest = float('-inf')
        monoStack = []
        for i in range(n - 1, -1, -1):
            if nums[i] < secondLargest:
                return True
            while monoStack and nums[i] > monoStack[-1]:
                print(monoStack[-1])
                secondLargest = monoStack.pop() #find second largest number
            monoStack.append(nums[i])
        return False