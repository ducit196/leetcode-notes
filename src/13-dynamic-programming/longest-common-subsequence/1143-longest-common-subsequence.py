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
        #prin lcs
        i, j = m, n
        ans = []
        while i > 0 and j > 0:
            if text1[i - 1] == text2[j - 1]:
                ans.append(text1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
        ans.reverse()
        print(ans)

        return dp[m][n]


text1 = "abac"
text2 = "cab"
print(Solution().longestCommonSubsequence(text1, text2))

