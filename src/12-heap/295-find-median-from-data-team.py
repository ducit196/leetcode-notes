from heapq import heapify, heappop, heappush


class MedianFinder:

    #Max heap store low number
    #Min heap store high number
    #Need to balance
    # if k = 2*1 then take one from max heap and 1 from min heap
    # if k = 2*i + 1 then let max heap have more than 1 element

    def __init__(self):
        self.max = []
        self.min = []
    def addNum(self, num: int) -> None:
        heappush(self.max, -num)
        heappush(self.min, -heappop(self.max)) #Min heap always have largest number
        if len(self.min) > len(self.max):
            heappush(self.max, -heappop(self.min))
    def findMedian(self) -> float:
        if len(self.max) == len(self.min):
            return (self.min[0] + -self.max[0]) / 2
        else:
            return -self.max[0]
# Your MedianFinder object will be instantiated and called as such:

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
param_2 = obj.findMedian()
print(param_2)