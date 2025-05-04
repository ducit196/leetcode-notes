


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for i in range(n)]
        ans = 0
        for i in range(n):
            dp[i][i] = True
            ans += 1
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans += 1
        for l in range(1, n):
            for i in range(n - l):
                j = i + l
                if s[i] == s[j] and dp[i + 1][j - 1] == True:
                    dp[i][j]  = True
                    ans += 1
        print(dp)
        return ans
s = "aaa"
print(Solution().countSubstrings(s))