class Solution:

    #Idea: Power of 2 mean: number has format: 1 and following 0
    #      a - 1, flip right most 1 of a to 0 and flip all following 0 to 1
    # Sample: a = 6: 110 --> a - 1 = 5: 101 -> a & a - 1 will remove right most 1 of a
    #Due to power of 2 has only one 1 bit --> a & a - 1 = 0
    #TC: O(1)
    #SC: O(1)
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and  n & (n - 1) == 0
print(Solution().isPowerOfTwo(16))