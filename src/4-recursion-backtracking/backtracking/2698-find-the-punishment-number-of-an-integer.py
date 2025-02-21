class Solution:
    def punishmentNumber(self, n: int) -> int:
        def isPunishmentNumber(k):
            square = str(k * k)
            length = len(square)
            found = False
            def choose(i, curSum):
                nonlocal found
                if found:
                    return
                if i == length:
                    if curSum == k:
                        found = True
                    return
                for j in range(i, length):
                    take = int(square[i:j + 1])
                    if curSum + take > k:
                        break
                    choose(j + 1, curSum + take)
            choose(0, 0)
            return found
        ans = 0
        for i in range(1, n + 1):
            if isPunishmentNumber(i):
                ans += i * i
        return ans
print(Solution().punishmentNumber(34))

