from random import randrange


class Solution:
    def quickSort(self, nums):
        #pick any index move all less than to left and move all greater than to right
        #recusively do left and right

        def quickSort(nums, start, end):
            if start >= end:
                return

            pivot = randrange(start, end + 1)
            randVal = nums[pivot]
            #move less than to left
            left = start
            for i in range(start, end + 1):
                if nums[i] < randVal:
                    nums[left],nums[i] = nums[i], nums[left]
                    left += 1
            right = end
            for i in range(end, start - 1, -1):
                if nums[i] > randVal:
                    nums[right], nums[i] = nums[i], nums[right]
                    right -= 1
            #from left to right equal to pivot
            quickSort(nums, start, left - 1)
            quickSort(nums, right + 1, end)

        quickSort(nums, 0, len(nums) - 1)
nums = [3,6,1,2,9,4]
Solution().quickSort(nums)
print(nums)