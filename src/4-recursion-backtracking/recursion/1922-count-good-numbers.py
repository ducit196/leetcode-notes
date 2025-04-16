

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        #even: 5 choices
        #odd: 4 choices
        ans = 1
        for i in range(n):
            if i % 2 == 0:
                ans *= 5
            else:
                ans *= 4
            ans = ans % (10 ** 9 + 7)
        return ans
print(Solution().countGoodNumbers(50))