from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        zeroCnt1 = nums1.count(0)
        zeroCnt2 = nums2.count(0)
        if (zeroCnt2 == 0 and sum2 < sum1 + zeroCnt1) or (zeroCnt1 == 0 and sum1 < sum2 + zeroCnt2):
            return -1
        return max(sum1 + zeroCnt1, sum2 + zeroCnt2)


nums1 = [20,0,18,11,0,0,0,0,0,0,17,28,0,11,10,0,0,15,29]
nums2 = [16,9,25,16,1,9,20,28,8,0,1,0,1,27]
print(Solution().minSum(nums1, nums2))