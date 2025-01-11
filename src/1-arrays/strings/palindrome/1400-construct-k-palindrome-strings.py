from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        count = Counter(s)
        oddCount = 0
        for v in count.values():
            if v % 2 != 0:
                oddCount += 1
        return  oddCount <= k       #if oddCount > k --> can not construct
s = "annabelle"
k = 2
ans = Solution().canConstruct(s, k)
print(ans)