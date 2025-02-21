from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def checkContain(s, d):
            sCount = Counter(s)
            dCount = Counter(d)
            for k,v in sCount.items():
                if dCount[k] < v:
                    return False
            return True
        minLength = 100000
        ans = ''
        left = 0
        for right in range(len(s)):
            while left <= right and checkContain(t, s[left:right + 1]):
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    ans = s[left:right + 1]
                left += 1
        return ans

s = "cabwefgewcwaefgcf"
t = "cae"
print(Solution().minWindow(s, t))