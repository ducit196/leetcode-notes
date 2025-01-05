import math
from typing import List
from show_recursion_tree import show_recursion_tree
from print_btree import print_btree


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        #Base case: i == n --> last worker is assgined --> find min distance
        #For each worker, assign to 1 not used bike.
            #Assign to next worker
            #backtrack used bike

        #Use bitmask for used bike, because number of bike <= 10
        @show_recursion_tree
        def manhattanDist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        n, m = len(workers), len(bikes)
        def choose(iw, usedBike):
            if iw == n:
                return 0
            ans = math.inf
            for b in range(m):
                if usedBike >> b & 1 == 1:
                    continue
                newUsedBike = usedBike | (1 << b)
                ans = min(ans, choose(iw + 1, newUsedBike) + manhattanDist(workers[iw], bikes[b]))
            return ans
        return choose(0, 0)
        # def manhattanDist(p1, p2):
        #     return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        # n, m = len(workers), len(bikes)
        # usedBike = set()
        # ans = math.inf
        # def choose(iw, usedBike, currentDist):
        #     nonlocal ans
        #     if iw == n:
        #         ans = min(ans, currentDist)
        #         return
        #     for b in range(m):
        #         if b in usedBike:
        #             continue
        #         else:
        #             usedBike.add(b)
        #             choose(iw + 1, usedBike, currentDist + manhattanDist(workers[iw], bikes[b]))
        #             usedBike.pop()
        # choose(0, usedBike, 0)
        # return ans
workers = [[0,0],[1,1],[2,0]]
bikes = [[1,0],[2,2],[2,1]]
ans = Solution().assignBikes(workers, bikes)
print(ans)
