from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        ans = []
        for i in range(n):
            if i < n - 1 and intervals[i][1] >= intervals[i + 1][0]:
                merge = [intervals[i][0], intervals[i + 1][1]]
                intervals[i + 1] = merge
            else:
                ans.append(intervals[i])
        return ans

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(intervals))


