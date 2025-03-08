from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k:
            return -1
        def calBouquet(day):
            ans = 0
            consecutive = 0
            for i in range(n):
                if day >= bloomDay[i]:
                    consecutive += 1
                    if consecutive == k:
                        ans += 1
                        consecutive = 0
                else:
                    consecutive = 0
            return ans


        left = min(bloomDay)
        right = max(bloomDay)
        #binary search from left to right
        ans = -1
        while left <= right:
            mid = left + (right - left) // 2
            bouquet = calBouquet(mid)
            if bouquet >= m:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3
print(Solution().minDays(bloomDay,2, 3))