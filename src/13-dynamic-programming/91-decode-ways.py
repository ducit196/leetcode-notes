class Solution:
    def numDecodings(self, s: str) -> int:

        # Idea: at each position i there are 2 possible way:
        #   If str[i] is not 0 --> ans += number ways of i + 1
        #   If str[i] == 1 or str[i] == 1 and str[i + 1] <= 6 --> ans += number of ways if i + 2
        #Topdown
        # n = len(s)
        # def dfs(i: int) -> int:
        #     if i == n:
        #         return 1
        #     ans = 0
        #     if s[i] != '0':
        #         ans += dfs(i + 1)
        #     if i < n - 1 and s[i] == '1' or s[i] == '2' and s[i + 1] <= '6':
        #         ans += dfs(i + 2)
        #     return ans
        # return dfs(0)
        #Bottom up
        n = len(s)
        dp = [0 for i in range(n + 1)]
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            if s[i] != '0':
                dp[i] += dp[i + 1]
            if i < n - 1 and (s[i] == '1' or s[i] == '2' and s[i] <= '6'):
                dp[i] += dp[i + 2]
        return dp[0]

print(Solution().numDecodings('226'))