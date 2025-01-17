from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])
        ans = [[0] * n for i in range(m)]
        direction = [(-1,0), (-1,1), (-1, -1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(m):
            for j in range(n):
                liveCount = 0
                for x,y in direction:
                    dx = i + x
                    dy = j + y
                    if 0 <= dx < m and 0 <= dy < n and board[dx][dy] == 1:
                        liveCount += 1

                if board[i][j] == 0:
                    if liveCount == 3:
                        ans[i][j] = 1
                    else:
                        break
                if board[i][j] == 1 and (liveCount < 2 or liveCount > 3):
                    ans[i][j] = 0
                else:
                    ans[i][j] = 1
        return ans
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(Solution().gameOfLife(board))
