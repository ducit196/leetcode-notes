from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        current = 0
        up, left = 0,0
        right = n - 1
        down = n - 1
        ans = [[0] * n for i in range(n)]
        while current < n*n:
            #Travel left to right
            for col in range(left, right + 1):
                current += 1
                ans[up][col] = current
            #Travel top to down
            for row in range(up + 1, down + 1):
                current += 1
                ans[row][right] = current
            #Travel Right to left
            if up != down:  #Make sure that we are in different row, make sure don't retravel the row that we traverse left to right
                for col in range(right - 1, left - 1, -1):
                    current += 1
                    ans[down][col] = current
            #Travel down to up
            if left != right:  # make sure that we are in different col, make sure don't retraverse top dwon
                for row in range(down - 1, up, -1):
                    current += 1
                    ans[row][left] = current
            right -= 1
            down -= 1
            left += 1
            up += 1
        return ans
print(Solution().generateMatrix(3))
