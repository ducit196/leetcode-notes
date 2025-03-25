from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def threeInterval(intervals):
            intervals.sort()
            end = intervals[0][1]
            cutCount = 0
            for i in range(1, len(intervals)):
                if intervals[i][0] >= end:
                    cutCount += 1
                end = max(end, intervals[i][1])
            return cutCount >= 2


        #check if can merge into 3 interval
        horizontal = []
        vertical = []
        for startX, startY, endX, endY in rectangles:
            horizontal.append([startY, endY])
            vertical.append([startX, endX])
        return threeInterval(horizontal) or  threeInterval(vertical)




rec = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
print(Solution().checkValidCuts(1, rec))

