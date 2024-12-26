from unittest.mock import right


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # sumS = 0
        # for i in range(len(s)):
        #     sumS += ord(s[i])
        # sumT = 0
        # for i in range(len(t)):
        #     sumT += ord(t[i])
        # added = sumT - sumS
        # return chr(added)
        ans = 0
        for charS in s:
            ans = ans ^ ord(charS)
        for charT in t:
            ans = ans ^ ord(charT)
        return chr(ans)

s = "abcd"
t = "abcde"
print(Solution().findTheDifference(s, t))