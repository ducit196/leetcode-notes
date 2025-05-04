from heapq import heappush
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        for start, end in intervals:
            if len(heap) == 0 or end < heap[0]:
                heappush(heap, end)
        return len(heap)
intervals = [[7,10],[2,4]]
print(Solution().minMeetingRooms(intervals))