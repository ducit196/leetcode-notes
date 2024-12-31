from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        #Number of ways to reach i = dp[i - 1] + dp[i - 2]
        #Base case: dp[0] = 1, dp[1] = 1

        #Bottom up
        # dp = [0] * (n + 1)
        # dp[0] = 1
        # dp[1] = 1
        # for i in range(2, n + 1):
        #     dp[i] = dp[i -1] + dp[i - 2]
        # return dp[n]
        #Optimize space
        # dp, dpPrev1, dpPrev2 = 0, 1, 1
        # for i in range(2, n + 1):
        #     dp = dpPrev2 + dpPrev1
        #     dpPrev2 = dpPrev1
        #     dpPrev1 = dp
        # return dpPrev1

        #Top down
        @cache
        def dp(i):
            if i < 2:
                return 1
            return dp(i - 2) + dp(i - 1)
        return dp(n)

