from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        d = [0] * n
        preCount = 0
        preSum = 0
        for i in range(n):
            d[i] += i * preCount - preSum   # i * preCount = number of step to move number of precount ball from 0 to i index
                                            #But not all ball in 0 position, --> number step = i * preCount - preSum
            if int(boxes[i]) == 1:
                preCount += 1
                preSum += i
        subSum = 0
        subCount = 0
        for i in range(n - 1, -1, -1):
            d[i] += subSum - i * subCount    #Sub sum is total step to all ball to 0 index, but my destination at ith
                                            # --> need to minus number of step from i - 1 to 0 = i * subCount
                                            #Last number of step = subSum - i * subCount
            if int(boxes[i]) == 1:
                subCount += 1
                subSum += i
        return d

boxes = "001011"
print(Solution().minOperations(boxes))