class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        k = len(part)
        ans = []
        for i in range(len(s)):
            ans.append(s[i])
            while len(ans) >= k and part == ''.join(ans[-k:]):
                del ans[-k:]
        return ''.join(ans)

s = "daabcbaabcbc"
part = "abc"
print(Solution().removeOccurrences(s, part))