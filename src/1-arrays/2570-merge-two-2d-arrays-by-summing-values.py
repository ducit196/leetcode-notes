from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []
        seen = {}
        m = len(nums1)
        n = len(nums2)
        if m < n:
            nums1,nums2 = nums2,nums1
            m,n = n,m
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i][0] < nums2[j][0]:
                if nums1[i][0] not in seen:
                    seen[nums1[i][0]] = nums1[i][1]
                else:
                    seen[nums1[i][0]] += nums1[i][1]
                i += 1
            else:
                if nums2[j][0] not in seen:
                    seen[nums2[j][0]] = nums2[j][1]
                else:
                    seen[nums2[j][0]] += nums2[j][1]
                j += 1
        while i < m:
            if nums1[i][0] not in seen:
                seen[nums1[i][0]] = nums1[i][1]
            else:
                seen[nums1[i][0]] += nums1[i][1]
            i += 1
        for k, v in seen.items():
            ans.append([k, v])
        return ans

nums1 = [[1,3],[4,3]]
nums2 = [[2,4],[3,6],[5,5]]
print(Solution().mergeArrays(nums1, nums2))