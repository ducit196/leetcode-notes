from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        ans = []
        currentSolution = []
        def choose(i, currentSolution):
            if i == n:
                ans.append(" ".join(currentSolution))
                return
            for j in range(i + 1, n):
                if s[i: j + 1] in wordDict:
                    currentSolution.append(s[i: j + 1])
                    choose(j + 1, currentSolution)
                    currentSolution.pop()
        choose(0, currentSolution)
        return ans

s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
ans = Solution().wordBreak(s, wordDict)
print(ans)
