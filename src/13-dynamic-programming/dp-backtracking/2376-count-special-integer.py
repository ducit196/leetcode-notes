from functools import cache

from show_recursion_tree import show_recursion_tree


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        digits = []
        while n > 0:
            digits.append(n % 10)
            n //= 10
        digits.reverse()

        #DP
        #This patter to check how to count how many number from 0 -> n
        @show_recursion_tree
        @cache
        def dp(i, tight, usedMask, leadingZero):
            if i == len(digits):
                return 1
            ans = 0
            maxDigit = digits[i] if tight else 9   #max digit can choose is this number is tight
                                                   #sample I have 135. If previous number is 1 --> tight --> max = 3 else max = 9
            for d in range(maxDigit + 1):
                if (usedMask >> d) & 1:
                    continue
                nextTight = tight and d == maxDigit
                nextLeadingZero = leadingZero and d == 0

                newUsedMask = usedMask
                if not nextLeadingZero:
                    newUsedMask = usedMask | (1 << d)
                ans += dp(i + 1, nextTight, newUsedMask, nextLeadingZero)
            return ans
        return dp(0, True, 0, True) - 1

print(Solution().countSpecialNumbers(20))