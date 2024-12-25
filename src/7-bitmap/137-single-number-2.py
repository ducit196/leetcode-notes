from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Count number of bit at each element
        #It could be multiples of 3 but 1 element occur once --> bit of once element is count % 3
        #Consolidate the ans
        #TC: O(n)
        #SC: O(1)
        ans = 0
        for i in range(32):
            bitCount = 0
            for num in nums:
                if num < 0:
                    num = num & (2**32 - 1)
                bitCount += (num >> i) & 1
            bitCount = bitCount % 3 #Unbalance element is a bit of the once element
            ans = ans | bitCount % 3 << i
        if ans >= 2**31:
            ans = ans - 2**32
        return ans

print(Solution().singleNumber([-2,-2,1,1,4,1,4,4,-4,-2]))