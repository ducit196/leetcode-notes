class Solution:
    def splitNum(self, num: int) -> int:
        s = str(num)
        sorted(s)
        s = ''.join(sorted(s))
        firstNum = 0
        secondNum = 0
        i = 0
        while i < len(s):
            firstNum = firstNum * 10 + int(s[i])
            i += 1
            if i == len(s):
                break
            secondNum = secondNum * 10 + int(s[i])
            i += 1
        return firstNum + secondNum
print(Solution().splitNum(4325))
