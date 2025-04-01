from collections import defaultdict
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        lastPosition = defaultdict(int)
        for i,c in enumerate(s):
            lastPosition[c] = i
        print(lastPosition)
        end = lastPosition[s[0]]
        ans = []
        lastAns = 0
        for i in range(1, n):
            if i > end:
                ans.append(i - lastAns)
                lastAns = i
                end = lastPosition[s[i]]
                continue
            if lastPosition[s[i]] > end:
                end = lastPosition[s[i]]
        ans.append(n - lastAns)
        return ans

s = "ababcbacadefegdehijhklij"
print(Solution().partitionLabels(s))