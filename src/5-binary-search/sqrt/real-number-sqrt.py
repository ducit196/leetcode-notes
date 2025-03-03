
class Solution:
    def mySqrt(self, x: int, p: int):
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
        #fractional handle
        increment = 0.1
        for i in range(p):
            while ans * ans <= x:
                ans += increment
            #loop end at ans > x
            ans -= increment
            increment /= 10
        return round(ans, p)
print(Solution().mySqrt(8, 4))