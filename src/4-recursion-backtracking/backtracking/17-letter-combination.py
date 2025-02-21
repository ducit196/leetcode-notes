from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno','pqrs', 'tuv','wxyz']
        n = len(digits)
        ans = []
        def choose(i, currentSolution):
            if i == n:
                ans.append(''.join(currentSolution))
                return
            for letter in keyboard[int(digits[i])]:
                print(letter)
                currentSolution.append(letter)
                choose(i + 1, currentSolution)
                currentSolution.pop()
        choose(0,[])
        return ans
print(Solution().letterCombinations("23"))