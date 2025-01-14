from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        count = Counter(s)
        for (k,v) in count.items():
            if v > 2:
                count[k] = 2 if v % 2 == 0 else 1
        return sum(count.values())
s = "abaacbcbb"
print(Solution().minimumLength(s))