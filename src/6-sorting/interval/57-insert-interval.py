from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #binary search
        #First element newInterval[0] >=
        #First element newIntrerval[1] >=
        def isOverlap(a, b):
            return a[1] >= b[0]
        n = len(intervals)
        def bicsecLeft(k):
            left = 0
            right = n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if intervals[mid][0] < k:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        if n == 0:
            return newInterval
        startMerge = bicsecLeft(newInterval[0])
        intervals.insert(startMerge, newInterval)

        #merge interval
        res = []
        for interval in intervals:
            # If res is empty or there is no overlap, add the interval to the result
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            # If there is an overlap, merge the intervals by updating the end of the last interval in res
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res

intervals = [[1,5]]
newInterval = [2,3]
print(Solution().insert(intervals, newInterval))