import math
from collections import Counter
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        #if x + 1 say same color --> x 

        count = Counter(answers)
        ans = 0
        for k,v in count.items():
            ans += math.ceil(v / (k + 1)) * (k + 1)
        return ans
answers = [1,1,1,2]
print(Solution().numRabbits(answers))