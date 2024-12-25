from turtledemo.penrose import start


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        #Because a & a - 1 --> flip right most bit 1 to 0
        #Find the pre common, then result common prefix shift left number of left over 0
        #TC: O(log(n))
        #SC: O(1)
        cnt = 0
        while left != right:
            left >>= 1
            right >>=1
            cnt += 1
        return left << cnt
        cnt = 0
        while left != right:
            left >>= 1
            right >>= 1
            cnt += 1
        return left << cnt

ans = Solution().rangeBitwiseAnd(6, 7)
print(ans)