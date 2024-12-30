
class Solution:
    memo = {}
    def fib(self, n: int) -> int:
        # if n < 2:
        #     return n
        # if n not in self.memo:
        #     self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        #     return self.memo[n]
        # else:
        #     return self.memo[n]
        if n < 2:
            return n
        prevPrev = 0
        prev = 1
        for i in range(2, n + 1):
            current = prev + prevPrev
            prevPrev = prev
            prev = current
        return prev


print(Solution().fib(8))