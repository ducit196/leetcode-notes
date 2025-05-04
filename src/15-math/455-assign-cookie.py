from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        left = 0
        cnt = 0
        for childG in g:
            while s[left] < childG:
                left += 1
                if left == len(s):
                    return cnt
            cnt += 1
            left += 1
        return cnt

g = [1,2,3]
s = [1,1]
print(Solution().findContentChildren(g, s))