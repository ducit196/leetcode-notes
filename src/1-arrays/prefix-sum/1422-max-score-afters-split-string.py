
class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        preSum = [0] * (n + 1)
        for i in range(0, n):
            preSum[i + 1] = preSum[i] + int(s[i])
        ans = 0
        for i in range(1, n):
            ans = max(ans, i - preSum[i] + preSum[n] - preSum[i])
        return ans
s = "00111"
print(Solution().maxScore(s))