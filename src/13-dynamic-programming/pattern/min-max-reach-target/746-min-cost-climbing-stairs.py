from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #Top down
        # n = len(cost)
        # def minCost(i):
        #     if i < 0:
        #         return 0
        #     return cost[i] + min(minCost(i - 1), minCost(i - 2))
        # return min(minCost(n - 1), minCost(n - 2))


        #Bottom up
        n = len(cost)
        dp = [0] * (n + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n + 1):
            costI = cost[i] if i < n else 0
            dp[i] = min(dp[i - 1], dp[i - 2]) + costI
        return dp[-1]

cost = [10,15,20]
print(Solution().minCostClimbingStairs(cost))