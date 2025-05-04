import math


class Solution:
    def numSquares(self, n: int) -> int:
        def listPerfectSquareLessThanX(x):
            ans = [1]
            for i in range(2, int(math.sqrt(x))):
                if i * i <= x:
                    ans.append(i)
            return ans

        dp = [math.inf] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            perfectList = listPerfectSquareLessThanX(i)
            if perfectList[-1] == i:
                dp[i] = 1
            for p in perfectList:
                dp[i] = min(dp[i], dp[i - p] + 1)
        return dp[-1]
print(Solution().numSquares(12))