from linecache import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #Idea: one by one check if 1 word is in dict, if have --> dp for remaining
        n = len(s)
        mem = {}
        def dp(i):
            if i == n:
                return True
            if i in mem:
                return mem[i]
            for j in range(i, n):
                if s[i:j + 1] in wordDict and dp(j + 1):
                    mem[i] == True
                    return True
            mem[i] = False
            return False
        return dp(0)
s = "leetcode"
wordDict = ["leet","code"]
print(Solution().wordBreak(s, wordDict))