
class Solution:
    def selectionSort(self, nums: list[int]) -> list[int]:
        #find min and move it to begin of array
        n = len(nums)
        for i in range(n):
            minIndex = i
            minVal = nums[i]
            for j in range(i + 1, n):
                if nums[j] < minVal:
                    minIndex = j
                    minVal = nums[j]
            nums[i], nums[minIndex] = nums[minIndex], nums[i]
        print(nums)
Solution().selectionSort([1,5,43,6,2])