


class Solution:
    def inversionCount(self, arr):

        def mergeTwoSortedList(nums1, nums2):
            nonlocal ans
            m = len(nums1)
            n = len(nums2)
            merege = []
            i = 0
            j = 0
            while i < m and j < n:
                if nums1[i] <= nums2[j]:
                    merege.append(nums1[i])
                    i += 1
                else:
                    merege.append(nums2[j])
                    ans += len(nums1) - i
                    j += 1
            while i < m:
                merege.append(nums1[i])
                i += 1
            while j < n:
                merege.append(nums2[j])
                j += 1
            return merege
        #merge sort
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
            left = mergeSort(nums[0:len(nums) // 2])
            right = mergeSort(nums[len(nums) // 2: len(nums)])
            return mergeTwoSortedList(left, right)
        ans = 0
        sortArray = mergeSort(arr)
        print(sortArray)
        return ans
arr = [4,3,2,1]
print(Solution().inversionCount(arr))