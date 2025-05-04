import math
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}
        def coinChange(amt):
            if amt == 0:
                return 0
            if amt in mem:
                return mem[amt]
            ans = math.inf
            for c in coins:
                if c <= amt:
                    ans = min(ans, coinChange(amt - c) + 1)
            mem[amt] = ans
            return ans
        result = coinChange(amount)
        return -1 if result == math.inf else result
coins = [2]
amount = 3
print(Solution().coinChange(coins, amount))