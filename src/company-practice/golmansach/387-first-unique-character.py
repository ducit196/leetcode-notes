class Solution:
    def firstUniqChar(self, s: str) -> int:
        wordFeq = [0] * 26
        for c in s:
            wordFeq[ord(c) - 97] += 1
        for i,c in enumerate(s):
            if wordFeq[ord(c) - 97] == 1:
                return i
        return -1
