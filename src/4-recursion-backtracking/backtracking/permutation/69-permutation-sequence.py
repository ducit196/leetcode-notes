class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = []
        def choose(start, currentPath):
            if len(currentPath) == n:
                ans.append(''.join(currentPath))
                return
            for i in range(1, n + 1):
                if str(i) not in currentPath:
                    currentPath.append(str(i))
                    choose(start + 1, currentPath)
                    currentPath.pop()
            print(currentPath)

        choose(1, [])
        return ans[k - 1]
print(Solution().getPermutation(3,3))