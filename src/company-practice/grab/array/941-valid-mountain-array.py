from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        #find max
        #walk up
        #walk down
        #O(n) time
        #O(1) space
        maxIndex = arr.index(max(arr))
        if maxIndex == 0 or maxIndex == len(arr) - 1:
            return False
        for i in range(0, maxIndex):
            if arr[i] >= arr[i + 1]:
                return False
        for i in range(len(arr) - 1, maxIndex, -1):
            if arr[i] >= arr[i - 1]:
                return False
        return True