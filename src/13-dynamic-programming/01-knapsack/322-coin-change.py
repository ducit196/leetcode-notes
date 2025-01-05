import math
from itertools import count
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        #Top down
        #Idea: each time change a coin, deduce amount then + 1 way
        # Find min
        # memo = {}
        # def dp(amt):
        #     if amt == 0:
        #         return 0
        #     if amt in memo:
        #         return memo[amt]
        #     ans = math.inf
        #     for coin in coins:
        #         if amt >= coin:
        #             ans = min(ans, dp(amt - coin) + 1)
        #             memo[amt] = ans
        #     return ans
        # res = dp(amount)
        # if res == math.inf:
        #     return -1
        # return res

        #Bottom up
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        for amt in range(1, amount + 1):
            for coin in coins:
                if amt >= coin:
                    dp[amt] = min(dp[amt], dp[amt - coin] + 1)
        if dp[amount] == math.inf:
            return -1
        return dp[amount]

coins = [1,3,5]
ans = Solution().coinChange(coins, 11)
print(ans)