
class Solution:
    def clearDigits(self, s: str) -> str:
        ans = []
        for i in range(len(s)):
            if s[i].isalpha():
                ans.append(s[i])
            elif s[i].isdigit():
                ans.pop()
        return ''.join(ans)





print(Solution().clearDigits("cb23"))