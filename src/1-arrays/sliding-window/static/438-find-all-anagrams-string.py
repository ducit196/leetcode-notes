from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # fixed sliding window
        def isAnagram(s1, s2):
            return sorted(s1 )== sorted(s2)
        ans = []
        n = len(s)
        m = len(p)
        nHash = 0
        mHash = 0
        for i in range(m):
            nHash += ord(s[i])
            mHash += ord(p[i])
        if nHash == mHash and isAnagram(s[0: m], p):
            ans.append(0)
        for i in range(1, n - m + 1):
            nHash = nHash + ord(s[i + m - 1]) - ord(s[i - 1])
            if nHash == mHash and isAnagram(s[i: i + m], p):
                ans.append(i)
        return ans

s = "abab"
p = "ab"
print(Solution().findAnagrams(s, p))