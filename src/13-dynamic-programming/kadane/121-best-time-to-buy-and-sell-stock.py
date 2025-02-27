from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two  pointer
        # n = len(prices)
        # left = 0
        # ans = 0
        # for right in range(1, n):
        #     if prices[left] < prices[right]:
        #         ans = max(ans, prices[right] - prices[left])
        #     else:
        #         left = right
        # return ans

        #Kadane like, keep track min prices and max profit
        n = len(prices)
        minPrice = prices[0]
        ans = 0
        for i in range(1, n):
            minPrice = min(minPrice, prices[i])
            ans = max(prices[i] - minPrice, ans)
        return ans


prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))