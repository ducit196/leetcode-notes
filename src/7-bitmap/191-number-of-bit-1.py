class Solution:
    def hammingWeight(self, n: int) -> int:

        # def getBit(n: int, k: int) -> int:
        #     return (n >> k ) & 1
        # count = 0
        # for i in range(32):
        #     if getBit(n, i) == 1:
        #         count += 1
        # return count

        #Not rely on constranin
        # count = 0
        # while n != 0:
        #     if n & 1 == 1:
        #         count += 1
        #     n = n >> 1

        #Optimize, change right most 1 bit to zero
        #a & a - 1 --> a right most 1 bit will be zero
        # 1100 = 12
        # 1011 = 11
        # --> 12 & 11 = 1000
        count = 0
        while n > 0:
            n = n & (n - 1)
            count += 1
        return count
print(Solution().hammingWeight(11))