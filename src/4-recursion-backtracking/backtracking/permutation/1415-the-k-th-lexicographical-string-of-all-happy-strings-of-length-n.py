
class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        ans = []
        def choose(start, currentPath):
            if len(currentPath) == n:
                ans.append(''.join(currentPath))
                return
            for c in 'abc':
                if len(currentPath) == 0 or c != currentPath[-1]:
                    currentPath.append(c)
                    choose(start + 1, currentPath)
                    currentPath.pop()
        choose(0, [])
        return ans[k - 1] if k <= len(ans) else ""
print(Solution().getHappyString(1,3))