from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #To reach last position arr[m - 1][n - 1]. dp[i][j] = dp[i - 1][j] + dp[i][j - 1] except for oibstacle cell
        #TC: O(m * n)
        #SC: O(m * 2)
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for i in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j - 1 >= 0 and obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i][j - 1]
                    continue
                if j == 0 and i - 1 >= 0 and obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j]
                    continue
                if obstacleGrid[i][j] != 1 and i != 0 and j != 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
ans = Solution().uniquePathsWithObstacles(obstacleGrid)
print(ans)