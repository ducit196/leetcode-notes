
class Solution:
    def arrangeCoins(self, n: int):
        left = 1
        right = 65535
        ans = 1
        while left <= right:
            mid = left + (right - left) // 2
            currentCoin = ((mid + 1) * mid) // 2
            if currentCoin <= n:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
print(Solution().arrangeCoins(8))