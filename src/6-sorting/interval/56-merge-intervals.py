from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def isOverlap(a, b):
            return a[1] >= b[0]

        intervals.sort()
        result = []
        cur = intervals[0]

        for inv in intervals[1:]:
            if isOverlap(cur, inv):
                cur[1] = max(cur[1], inv[1])
            else:
                result.append(cur)
                cur = inv
        result.append(cur)
        return result


intervals = [[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(intervals))


