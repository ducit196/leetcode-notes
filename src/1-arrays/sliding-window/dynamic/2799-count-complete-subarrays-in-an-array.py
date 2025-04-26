from collections import defaultdict, Counter
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        #Unique value
        n = len(nums)
        uniqVal = Counter(nums)
        curSet = defaultdict(int)
        ans = 0
        left = 0
        for i in range(n):
            curSet[nums[i]] += 1
            while len(curSet) == len(uniqVal):
                print(curSet)
                ans += (n - i)
                curSet[nums[left]] -= 1
                if curSet[nums[left]] == 0:
                    del curSet[nums[left]]
                left += 1
        return ans
nums = [5,5,5,5]
print(Solution().countCompleteSubarrays(nums))