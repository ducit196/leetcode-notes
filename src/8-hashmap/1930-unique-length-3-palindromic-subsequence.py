class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        #For every char, append first and last occur in in string
        n = len(s)
        seen = {}
        ans = 0
        for i in range(n):
            if s[i] in seen:
                u,v = seen[s[i]]
                seen[s[i]] = (u, i)
            else:
                seen[s[i]] = (i, 0)
        for l,r in seen.values():
            if (l - r) < -1:
                countSet = set()
                for c in s[l + 1:r]:
                    countSet.add(c)
                ans += len(countSet)
        return ans
s = "aabca"
ans = Solution().countPalindromicSubsequence(s)
print(ans)