
from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # binary search from max weight --> could take all days, each day 1 element
        # To sum(weght) --> only 1 day needed
        # Monotinic here, If I can shif W goods in 3 days --> I can ship in 3 ++ days
        def feasible(target):
            day = 1
            curSum = 0
            for w in weights:
                curSum += w
                if curSum > target:
                    day += 1
                    curSum = w
            return day <= days


        left = max(weights)
        right = sum(weights)
        ans = 0
        while left <= right:
            mid = left + (right - left) // 2
            if feasible(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
weights = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]
days = 5
print(Solution().shipWithinDays(weights, days))