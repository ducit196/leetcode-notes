from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        #TC: O(n)
        #SC: O(n)
        vowel = set(list("aeiou"))
        n = len(words)
        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i + 1] = preSum[i] +  (1 if words[i][0] in vowel and words[i][-1] in vowel else 0)
        ans = []
        for i, j in queries:
            ans.append(preSum[j + 1] - preSum[i] )
        return ans

words = ["aba","bcb","ece","aa","e"]

queries = [[0,2],[1,4],[1,1]]
ans = Solution().vowelStrings(words, queries)
print(ans)
