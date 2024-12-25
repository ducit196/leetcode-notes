class Solution:
    def reverseBits(self, n: int) -> int:
        left = 0
        right = 31
        def setBit(n: int, k: int, v: int) ->int:
            if v == 1:  #set to 1
                return n | (1 << k)
            else:
                return n & (~(1 << k))

        def flip(n: int, k: int):
            return n ^ (1 << k)

        while left < right:
            lBit = (n >> left ) & 1
            rBit = (n >> right ) & 1
            if lBit != rBit:
                #Swap
                n = flip(n, left)
                n = flip(n, right)
            left += 1
            right -= 1
        return n

n = 0o0000010100101000001111010011100
print(Solution().reverseBits(n))




# Solution 1: 2 pointer, swap left and right
# Solution 2: Flip if left and right different
