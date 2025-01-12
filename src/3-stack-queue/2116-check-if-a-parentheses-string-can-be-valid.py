
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        #Maintain 2 stack, 1 for unlocked element, it can be close or open
        #1 stack for open bracket
        #If we see a close bracket --> try to pop open bracket, else pop unlocked else return false
        #Check for remaining open bracket. (* -> can be valid, bit *) can not be valid --> open bracket index < unlocked index

        n = len(s)
        if n % 2 != 0:
            return False
        openBracket = []
        unlockedBracket = []
        for i in range(n):
            if locked[i] == '0':
                unlockedBracket.append(i)
            elif s[i] == '(':
                openBracket.append(i)
            elif openBracket:
                openBracket.pop()   #Try to pop open bracket first
            elif unlockedBracket:
                unlockedBracket.pop()   #No open bracket, can pop wildcard bracket
            else:
                return False
        #Check for remaining open bracket. (* --> valid *) not valid
        while openBracket and unlockedBracket and openBracket[-1] < unlockedBracket[-1]:
            openBracket.pop()
            unlockedBracket.pop()
        return not openBracket




s = ")("
locked = "00"
print(Solution().canBeValid(s, locked))