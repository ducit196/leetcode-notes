from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        R, C = len(matrix), len(matrix[0])
        up, left = 0, 0
        right = C - 1
        down = R - 1
        while len(result) < R * C:
            #Travel left to right
            for col in range(left, right + 1):
                result.append(matrix[up][col])
            #Travel top to down
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])
            #Travel Right to left
            if up != down:  #Make sure that we are in different row, make sure don't retravel the row that we traverse left to right
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])
            #Travel down to up
            if left != right:  # make sure that we are in different col, make sure don't retraverse top dwon
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])
            right -= 1
            down -= 1
            left += 1
            up += 1
        return result
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().spiralOrder(matrix))