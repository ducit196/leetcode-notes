from itertools import count


class Solution:
    def findComplement(self, num: int) -> int:
        #Count binary length of num
        #XOR with mask: n ^ count - 1
        count = 0
        temp = num
        while temp > 0:
            temp = temp >> 1
            count += 1
        return num ^ ((1 << count) - 1)
print(Solution().findComplement(5))