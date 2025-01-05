
class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:

        #Find longest subsequence string
        #Backtrack, append element have greater dp
        #Remaining + path revert is the result

        m = len(s1)
        n = len(s2)
        dp = [[0] * (n  + 1 ) for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        i = m
        j = n
        path = []
        while i > 0 and j > 0:
            if s1[i - 1] == s2[j - 1]:
                path.append(s1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                path.append(s1[i - 1])
                i -= 1
            else:
                path.append(s2[j - 1])
                j -= 1
        path.reverse()
        return s1[:i] + s2[:j] + ''.join(path)

str1 = 'abac'
str2 = 'cab'
ans = Solution().shortestCommonSupersequence(str1, str2)
print(ans)