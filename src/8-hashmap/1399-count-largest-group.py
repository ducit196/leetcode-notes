from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = defaultdict(int)
        curSum = 0

        def sumNumber(x):
            ans = 0
            while x > 0:
                ans += x % 10
                x //= 10
            return ans

        for i in range(1, n + 1):
            if i % 10 == 0:
                curSum = sumNumber(i)
            else:
                curSum += 1
            count[curSum] += 1

        print(count)
        maxValue = max(count.values())
        return sum(1 for k, v in count.items() if v == maxValue) #python count ip
