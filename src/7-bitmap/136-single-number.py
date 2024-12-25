from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # mapCount = {}
        # for num in nums:
        #     if num not in mapCount:
        #         mapCount[num] = 1
        #     else:
        #         mapCount[num] += 1
        # for k, v in  mapCount.items():
        #     if v == 1:
        #         return k

        #Counter
        # counts = Counter(nums)
        # for k, v in counts.items():
        #     if v == 1:
        #         return k;

        #Bit manipilation
        # A ^ A == 0, --> Final result is single element
        ans = 0
        for num in nums:
            ans = ans ^ num
        return ans

nums = [2,2,1]
print(Solution().singleNumber(nums))