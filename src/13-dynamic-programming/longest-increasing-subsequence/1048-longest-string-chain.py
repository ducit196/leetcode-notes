from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        #Sort by lenght
        #Write a function to check predecessor
        def checkPredecessor(s1, s2):
            i = 0
            j = 0
            addEle = False
            while i < len(s1) and j < len(s2):
                if s1[i] == s2[j]:
                    i += 1
                    j += 1
                elif addEle == False:
                    j += 1
                    addEle = True
                else:
                    return False
            return True


        #common form for longest increasing subsequen, each i, find max 0 -> i - 1 that satisfy condtion
        words.sort(key=lambda x: len(x))
        n = len(words)
        dp = [1] * n
        for i in range(n):
            for j in range(i - 1, -1, -1):
                if len(words[i]) == len(words[j]) + 1 and checkPredecessor(words[j], words[i]) and dp[j] + 1 > dp[i]:   #add tail condtion
                    dp[i] = dp[j] + 1
        return max(dp)

words = ["a","b","ab","bac"]
ans = Solution().longestStrChain(words)
print(ans)