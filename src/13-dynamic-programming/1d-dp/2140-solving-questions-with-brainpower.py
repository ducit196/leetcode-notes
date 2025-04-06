from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[n - 1] = questions[n - 1][0]
        for i in range(n - 2, -1, -1):
            point, skip = questions[i]
            if i + skip + 1 < n:
                dp[i] = point + dp[i + skip + 1]
            else:
                dp[i] = point
            dp[i] = max(dp[i], dp[i + 1])
        return max(dp)


questions = [[12,46],[78,19],[63,15],[79,62],[13,10]]
print(Solution().mostPoints(questions))


