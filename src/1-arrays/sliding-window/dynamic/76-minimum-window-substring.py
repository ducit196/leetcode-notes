import math
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def checkInclude(c1, c2):
            for k,v in c2.items():
                if c1[k] < v:
                    return False
            return True
        n, m = len(s), len(t)
        if n < m:
            return ''
        countT = Counter(t)
        print(countT)
        countS = Counter(s[0:m])

        ansLength =  math.inf
        ansIndex = 0
        if checkInclude(countS, countT):
            return t

        left = 0

        for right in range(m, n):
            countS[s[right]] += 1
            while left <= right and checkInclude(countS, countT):
                d = right - left
                if d < ansLength:
                    ansLength = d
                    ansIndex = left
                countS[s[left]] -= 1
                left += 1
        if ansLength != math.inf:
            return s[ansIndex: ansIndex + ansLength + 1]
        return ''

s = "abc"
t = "b"
print(Solution().minWindow(s, t))