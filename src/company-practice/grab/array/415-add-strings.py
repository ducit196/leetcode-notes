class Solution:
    def addStrings(self, s1: str, s2: str) -> str:
        i = len(s1) - 1
        j = len(s2) - 1
        carry = 0
        ans = []
        while i >= 0 or j >= 0 or carry:
            operan1 = int(s1[i]) if i >= 0 else 0
            operan2 = int(s2[j]) if j >= 0 else 0
            curSum = operan1 + operan2 + carry
            ans.append(str(curSum % 10))
            carry = curSum // 10
            j -= 1
            i -= 1
        return ''.join(ans[::-1])
s1 = "11"
s2 = "123"
print(Solution().addStrings(s1, s2))