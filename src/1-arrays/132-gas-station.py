from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cirleGas = gas * 2
        cirleCost = cost * 2
        print(cirleGas)
        n = len(gas)
        for i in range(n):
            curEng = gas[i]
            canComplete = True
            for j in range(i, i + n):
                if curEng < cirleCost[j]:
                    canComplete = False
                    break
                curEng = curEng - cirleCost[j] + cirleGas[j + 1]
            if canComplete:
                return i
        return -1

gas = [1,2,3,4,5]

cost = [3,4,5,1,2]

print(Solution().canCompleteCircuit(gas, cost))