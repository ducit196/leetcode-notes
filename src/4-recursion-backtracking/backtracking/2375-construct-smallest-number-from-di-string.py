class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        ans = []

        def choose(currentIndex, currentCount):
            if currentIndex != n:
                if pattern[currentIndex] == 'I':
                    choose(currentIndex + 1, currentIndex + 1)
                else:
                    currentCount = choose(currentIndex + 1, currentCount)
            ans.append(str(currentCount + 1))
            return currentCount + 1

        choose(0, 0)
        return ''.join(ans[::-1])

print(Solution().smallestNumber('IIIDIDDD'))