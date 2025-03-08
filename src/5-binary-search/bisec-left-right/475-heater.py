import math
from typing import List



class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
            def bisecRight(arr, target):
                left = 0
                right = len(arr) - 1
                ans = len(arr)
                while left <= right:
                    mid = left + (right - left) // 2
                    if arr[mid] > target:
                        ans = mid
                        right = mid - 1
                    else:
                        left = mid + 1
                return ans
            s = set()
            #house = [1,2,3,4]
            #heaters = [1,4]
            heaters.sort()
            ans = 0
            for house in houses:
                iRight = bisecRight(heaters, house)
                minRadius = math.inf
                if iRight < len(heaters):
                    minRadius = min(minRadius, heaters[iRight] - house)
                iLeft = iRight - 1
                if iLeft >= 0:
                    minRadius = min(minRadius, house - heaters[iLeft])
                ans = max(ans, minRadius)
            return ans
houses = [1,2,3,4]
heaters = [1,4]
print(Solution().findRadius(houses, heaters))