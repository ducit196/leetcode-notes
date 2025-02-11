from typing import List


class Solution:
    def rotation(self, grid: List[List[int]]):
        #Last row of ori matrix will become first column of des matrix and so on
        #TC: = O(n**2)
        #SC: = O(n**2)
        # n = len(grid)
        # ans = [[0] * n for i in range(n)]
        # for i in range(n - 1, -1, -1):
        #     for j in range(n):
        #         ans[j][n - i - 1] = grid[i][j]
        # return ans

        #4 ways exchange: 1 = 2, 2 = 3, 3 = 4, 4= 1
        size = len(grid) - 1
        for i in range(len(grid) // 2):
            for j in range(i, size - i):
                (grid[i][j], grid[~j][i], grid[~i][~j], grid[j][~i]) = (grid[~j][i], grid[~i][~j], grid[j][~i], grid[i][j])
                # 1,2,3,4 = 2, 3, 4, 1
        return grid


        #  1,  2,  3,  4
        #  5,  6,  7,  8
        #  9, 10, 11, 12
        # 13, 14, 15, 16


grid = [[1,2,3,4], [5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(Solution().rotation(grid))