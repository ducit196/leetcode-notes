from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        freq = [0] * (n + 1)
        ans = [0] * n
        count = 0   #sum up common pref
        for i in range(n):
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                count += 1
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                count += 1
            ans[i] = count
        return ans
