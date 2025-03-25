from typing import List


class Solution:
    #traver boundary, BFS ->  if O --> #
    #remaning O -> x, # flip back O
    #TC: O(m x N)
    #SC: O(m x n)
    def solve(self,board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])
        def dfs(i: int, j: int):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            board[i][j] = "#"
            # 4 direction
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
        #Traver bound
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and board[i][j] == 'O':
                    dfs(i, j)
        #flip
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(board)
Solution().solve(board)
print(board)