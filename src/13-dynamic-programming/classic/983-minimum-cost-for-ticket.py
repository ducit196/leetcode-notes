import math
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # If the day is not traveled, set cost from previous At every day, consider 1 of 3 options and find min cost:
        # If I choose 1 day pass: --> cost = previous day cost + cost[0]
        # If I choose 7 days pass: cost = max of day 1 to 6 days before
        # If I choose 30 days pass: cost = max of day 1 to 29 days before
        #TC: O(n)
        #SC: O(n)
        n = max(days)
        dp = [0] * (n + 1)
        for i in range(n + 1):
            if i not in days:
                dp[i] = dp[i - 1]
            else:
                mindp = math.inf
                mindp = min(mindp, dp[i - 1] + costs[0])
                if i - 6 > 0:
                    mindp = min(mindp, max(dp[0: i - 6], default = 0) + costs[1])   #Max from first day to 7 days before in clude
                else:
                    mindp = min(mindp, costs[1])   #Max from first day to 7 days before in clude
                if i - 29 > 0:
                    mindp = min(mindp, max(dp[0: i - 29], default = 0) + costs[2])
                else:
                    mindp = min(mindp, costs[2])   #Max from first day to 7 days before in clude
                dp[i] = mindp
        return dp[-1]
days = [1,5,8,10,13,20,29,31,37,48,52,53,54,61,63,64,65,67,72,73,74,79,81,84,85,86,87,88,91,94,98,100,108,112,115,116,120,121,123,131,132,135,137,139,141,145,147,152,163,165,166,173,174,178,179,182,187,198,202,203,204,206,208,210,212,213,216,224,230,234,237,239,240,242,247,249,250,257,259,261,263,265,266,272,273,274,275,279,280,281,284,288,292,293,297,298,300,301,304,306,309,318,323,326,328,330,332,335,336,339,341,342,345,350,351,362,365]
costs = [15,8,3]
print(Solution().mincostTickets(days, costs))