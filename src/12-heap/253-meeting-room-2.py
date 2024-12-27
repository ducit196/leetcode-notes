from heapq import heappush, heapreplace
from typing import List


class Solution:
    #Idea: sort the start time of interval
    #Use a min heap to store end time of meeting
    #If next meeting start before top of heap --> need a new room, add stop of new meeting
    #Else min we can use the same meeting room, just replace ending time
    #TC: O(NlogN)
    #SC: O(n)
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        heap = []
        for start, end in intervals:
            if (heap and start < heap[0]) or len(heap) == 0:
                heappush(heap, end)
            heapreplace(heap, end)
        return len(heap)

intervals = [[0,30],[15,20],[5,10]]
print(Solution().minMeetingRooms(intervals))
