from typing import List


class NumMatrix:
    #Idea: calcluate prefix sum by rơ
    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.preSum = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(0, m):
            for j in range(0, n):
                self.preSum[i + 1][j + 1] = matrix[i][j] + self.preSum[i + 1][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2 + 1):
            sum += self.preSum[i + 1][col2 + 1] - self.preSum[i + 1][col1]
            #Prefix sum from i to j = prefixSum[j] - prefixSum[i - 1]
        return sum


# Your NumMatrix object will be instantiated and called as such:
matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(2, 1, 4, 3)
print(param_1)