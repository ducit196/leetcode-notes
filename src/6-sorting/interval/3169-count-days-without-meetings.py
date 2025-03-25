from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        n = len(meetings)
        meetings.sort()
        end = meetings[0][1]
        ans = 0
        for i in range(1, n):
            if meetings[i][0] > end:
                ans += (meetings[i][0] - end - 1)
            end = max(end, meetings[i][1])
        ans += (meetings[0][0] - 1)
        ans += (days - meetings[-1][1])
        return ans


meetings  = [[3,49],[23,44],[21,56],[26,55],[23,52],[2,9],[1,48],[3,31]]
print(Solution().countDays(57, meetings))