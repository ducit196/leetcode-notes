class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        #If s1[i] == s2[j] --> dp[i][j] = dp[i- 1][j - 1] + 1
        #Otherwise dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n  +1 ) for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]
text1 = "abcde"
text2 = "ace"
print(Solution().longestCommonSubsequence(text1, text2))
