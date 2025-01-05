from functools import cache

from show_recursion_tree import show_recursion_tree


class Solution:

    def fibonacci(self, n: int) -> int:
        @show_recursion_tree
        @cache
        def dp(i):
            if i < 2:
                return i
            return dp(i - 1) + dp(i - 2)
        dp(n)
print(Solution().fibonacci(8))