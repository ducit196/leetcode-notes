class Solution:
    def permutation(self, s: str):
        n = len(s)
        ans = []

        def choose(i, currentSolution):
            if i == n:
                ans.append(currentSolution.copy())
                return
            for j in range(n):
                if s[j] not in currentSolution:
                    currentSolution.append(s[j])
                    choose(i + 1, currentSolution)
                    currentSolution.pop()

        choose(0, [])
        return ans
print(Solution().permutation("AAB"))