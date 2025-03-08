

class Solution:
    def coloredCells(self, n: int) -> int:
        ans = 1
        for i in range(n):
            ans += 4 * i
        return ans
print(Solution().coloredCells(10))