from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counterS = Counter(s)
        counterT = Counter(t)
        ans = 0
        for k,v in counterT.items():
            if counterS[k] < v:
                ans += v - counterS[k]
        return ans
s = "bab"
t = "aba"
print(Solution().minSteps(s, t))