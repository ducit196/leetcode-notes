from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # ans = [-1] * len(nums1)
        # for i in range(len(nums1)):
        #     traversed = False
        #     for j in range(len(nums2)):
        #         if nums2[j] == nums1[i]:
        #             traversed = True
        #         if nums2[j] > nums1[i] and traversed:
        #             ans[i] = nums2[j]
        #             break
        # return ans
        n = len(nums2)
        seen = {}
        for i in range(n):
            seen[nums2[i]] = -1
        monoStack = []

        for i in range(n):
            while monoStack and nums2[i] > nums2[monoStack[-1]]:
                index = monoStack.pop()
                seen[nums2[index]] = nums2[i]
            monoStack.append(i)
        for i in range(len(nums1)):
            nums1[i] = seen[nums1[i]]
        return nums1


nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(Solution().nextGreaterElement(nums1, nums2))