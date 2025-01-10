from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        #Compute max frequency of all word
        def calFreq(s):
            freq = [0] * 26
            for i in range(len(s)):
                freq[ord(s[i]) - 97] += 1
            return freq

        freq = [0] * 26

        for i in range(len(words2)):
            freqTemp = [0] * 26
            for j in range(len(words2[i])):
                freqTemp[ord(words2[i][j]) - 97] += 1
            for i in range(26):
                freq[i] = max(freq[i], freqTemp[i])
        ans = []
        for w in words1:
            wFreq = calFreq(w)
            isSuper = True
            for i in range(26):
                if freq[i] > wFreq[i]:
                    isSuper = False
                    break
            if isSuper:
                ans.append(w)
        return ans


words1 = ["google","leetcode"]
words2 = ["lo","eo"]
ans = Solution().wordSubsets(words1, words2)
print(ans)