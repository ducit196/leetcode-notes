import math
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #find peak and valley
        n = len(prices)
        valley = prices[0]
        peak = prices[0]
        ans = 0
        for i in range(1, n):
            if prices[i] < peak:
                ans += peak - valley
                valley = prices[i]
                peak = valley
            else:
                peak = prices[i]
        ans += peak - valley
        return ans
prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))