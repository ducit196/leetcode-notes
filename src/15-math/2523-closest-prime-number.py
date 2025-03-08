import math
from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        #sieve
        sieve = [1] * (right + 1)
        sieve[0], sieve[1] = 0, 0
        for i in range(2, int(math.sqrt(right) + 1)):
            if sieve[i] == 1:
                j = i
                while i * j <= right:
                    sieve[i * j] = 0
                    j += i
        primes = []
        for i in range(left, len(sieve)):
            if sieve[i] == 1:
                primes.append(i)
        if len(primes) < 2:
            return [-1, -1]
        curMin = math.inf
        ans = [-1, -1]
        for i in range(1, len(primes)):
            if primes[i] - primes[i - 1] < curMin:
                curMin = primes[i] - primes[i - 1]
                ans = [primes[i - 1], primes[i]]
        return ans
print(Solution().closestPrimes(11,19))
