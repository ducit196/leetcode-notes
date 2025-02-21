from typing import List


class Solution:
    def binaryCombination(self, n: int) -> List[List[int]]:
        ans = []
        def choose(start, path):
            if start == n:
                ans.append(path.copy())
                return
            path.append(0)
            choose(start + 1, path)
            path.pop()
            path.append(1)
            choose(start + 1, path)
            path.pop()
        choose(0, [])
        return ans
print(Solution().binaryCombination(3))