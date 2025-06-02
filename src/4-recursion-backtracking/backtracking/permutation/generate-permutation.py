
class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        def checkValid(x):
            oddSum = 0
            evenSum = 0
            for i, s in enumerate(x):
                if i % 2 == 0:
                    oddSum += int(s)
                else:
                    evenSum += int(s)
            return oddSum == evenSum


        n = len(num)
        ans = 0
        sorted(num)
        used = [0] * n
        def choose(start, curPath):
            nonlocal ans
            if start == n:
                print(curPath)
                if checkValid(curPath):
                    ans += 1
                return
            for i in range(n):
                if used[i] == 1:
                    continue
                if i > 0 and num[i] == num[i - 1] and used[i - 1] == 0:
                    continue
                used[i] = 1
                curPath.append(num[i])
                choose(start + 1, curPath)
                used[i] = 0
                curPath.pop()

        choose(0, [])
        print(ans)
num = '112'
Solution().countBalancedPermutations(num)