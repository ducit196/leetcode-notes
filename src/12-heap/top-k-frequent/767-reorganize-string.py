from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    def reorganizeString(self, s: str) -> str:
        #using heap to get most frequent element
        #but next element don't add same, so we keep track prev element
        n = len(s)
        heap = [(-v, k) for k, v in Counter(s).items()]
        heapify(heap)
        prevFreq, preChar = 0, ''
        ans = []
        while heap:
            freq, char = heappop(heap)
            ans.append(char)
            if prevFreq < -1:
                heappush(heap, (prevFreq + 1, preChar))
            prevFreq, preChar = freq, char
        if len(ans) == n:
            return ''.join(ans)
        return ""
s = "aabbcc"
print(Solution().reorganizeString(s))

