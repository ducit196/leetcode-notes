import math


class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        #Base case:
            #if i == 0 --> dp[i][j] = j #inser all character of string 2
            #if j == 0 --> dp[i][j] = i #delete all character of string 1

        #If s1[i] = s2[j] --> dp[i][j] = dp[i - 1][j - 1]
        #Other wise we have 3 cases: find min of 3 cases then + 1
            #Insert:
                #S1 = adc    --> s1 insert: acb --> dp[i][j] = dp[i][j - 1]
                #S2 = abc
            #Delete:
                #S1 = abc   --> s1 delete c --> dp[i][j] = dp[i - 1][j]
                #S2 = ab
            #Replace:
                #s1 = abe  --> s1 replace e --> dp[i][j] = d[i - 1][j - 1]
                #s2 = abc
        #TC: O(m * n)
        #SC: O(m * n)
        m = len(s1)
        n = len(s2)
        dp = [[math.inf] * (n + 1) for i in range(m + 1)]
        for i in range(0, m + 1):
            for j in range(0, n + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i

                elif s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        return dp[m][n]
word1 = "horse"
word2 = "ros"
print(Solution().minDistance(word1, word2))
