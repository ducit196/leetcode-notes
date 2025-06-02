from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def choose(curPath, openCnt, closeCnt):
            if len(curPath) == 2 * n:
                ans.append(''.join(curPath))
                return
            if openCnt < n:
                curPath.append('(')
                choose(curPath, openCnt + 1, closeCnt)
                curPath.pop()
            if closeCnt < openCnt:
                curPath.append(')')
                choose(curPath, openCnt, closeCnt + 1)
                curPath.pop()  # can use curentPath is String, so no need to backtrack because String is immutable

        choose([], 0, 0)
        return ans
print(Solution().generateParenthesis(3))