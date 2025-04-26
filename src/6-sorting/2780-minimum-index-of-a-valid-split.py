from collections import Counter, defaultdict
from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = Counter(nums)
        dominant, totalDomtFreq = count.most_common()[0]
        countDomtFreq = 0
        for i in range(len(nums)):
            if nums[i] == dominant:
                countDomtFreq += 1
            if countDomtFreq > (i + 1) // 2 and (totalDomtFreq - countDomtFreq) > (len(nums) - i - 1) // 2:
                return i
        return -1
print(Solution().minimumIndex([1,2,2,2]))