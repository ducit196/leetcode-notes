import math
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seen = {}
        left = 0
        totalComb = 0
        ans = 0
        for i in range(n):
            if nums[i] not in seen:
                seen[nums[i]] = (1, 0)
            else:
                curFreq, curComb = seen[nums[i]]
                newComb = math.comb(curFreq + 1, 2)
                seen[nums[i]] = (curFreq + 1, newComb)
                totalComb += (newComb - curComb)
            while totalComb >= k:
                ans += n - i
                print(f"{left} : {i}")
                if nums[left] in seen:
                    curFreq, curComb = seen[nums[left]]
                    newComb = 0 if curFreq - 1 < 2 else math.comb(curFreq - 1, 2)
                    seen[nums[left]] = (curFreq - 1, newComb)
                    totalComb += (newComb - curComb)
                    left += 1
        return ans

nums = [3,1,4,3,2,2,4]
print(Solution().countGood(nums, 2))