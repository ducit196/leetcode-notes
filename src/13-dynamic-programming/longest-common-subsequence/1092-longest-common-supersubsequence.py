
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # s[i] == s[j] --> dp[i][j] = dp[i - 1][j - 1] + 1
        # else dp[i][j] = max(dp[i- 1][j], dp[i][j - 1])
        m = len(str1)
        n = len(str2)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        print(dp)

str1 = "abac"
str2 = "cab"
print(Solution().shortestCommonSupersequence(str1, str2))