class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        setNum1 = 0
        setNum2 = 0
        num1Tmp = num1
        num2Tmp = num2
        while num2Tmp != 0:
            num2Tmp &= num2Tmp - 1  # Right most 1
            setNum2 += 1
        while num1Tmp != 0:
            num1Tmp &= num1Tmp - 1
            setNum1 += 1

        diff = setNum1 - setNum2
        if diff == 0:
            return num1
        elif diff > 0:
            for i in range(diff):
                num1 &= num1 - 1
        else:
            for i in range(-diff):
                num1 |= (num1 + 1)

        return num1
num1 = 1
num2 = 12
print(Solution().minimizeXor(num1, num2))