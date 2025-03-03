# Longest Common Subsequence
Main idea: if at position (i,j) s1[i] == s2[j] --> dp[i][j] = dp[i - 1][j -1] + 1  
           Else choose result of previous of s1 or s2 dp[i][j = max(dp[i - 1][j], dp[i][j - 1])

```plaintext
    #Because in recursive have i - 1, j - 1 -->  use + 1 dp array
    dp = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(1, n + 1)
        for j in range(1, n + 1)
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i -1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]
```
dp[i][j] is length of LCS of s1[:i] and s2[:j]
