from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSubFix(s1, s2):
            n = len(s1)
            m = len(s2)
            s1Hash = 0
            s2PrefixHash = 0
            s2SubfixHash = 0
            for i in range(n):
                s1Hash += pow(2, ord(s1[i]) - 97)
                s2PrefixHash += pow(2, ord(s2[i]) - 97)
                s2SubfixHash += pow(2, ord(s2[m - n + i]) - 97)
                if s1Hash != s2PrefixHash or s1Hash != s2SubfixHash:
                    return False
            if s2[:n] == s1 and s2[m - n:] == s1:
                return True
        n = len(words)
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if len(words[i]) <= len(words[j]) and  isPrefixAndSubFix(words[i], words[j]):
                    ans += 1
        return ans