class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0 
        right = 46341
        ans = 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
print(Solution().mySqrt(8))