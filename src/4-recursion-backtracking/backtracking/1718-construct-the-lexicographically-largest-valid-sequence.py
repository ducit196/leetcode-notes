from typing import List


class Solution:
    def constructDistancedSequence(self, target: int) -> List[int]:
        #Initiate ans = 2 * target - 1 (1 orcurr only once)
        n = 2 * target - 1
        ans = n * [0]
        #used = set()
        used = 0
        def choose(i):
            nonlocal used
            if i == n:
                return True
            if ans[i]:  #filled
                return choose(i + 1)
            for j in range(target, 0, -1):
                if used >> j & 1 == 1: #j is filled
                    continue

                nxt = i + j if j > 1 else i
                if nxt >= n or ans[nxt] != 0:   #invalid next
                    continue
                ans[i] = ans[nxt] = j
                used = used | 1 << j   #mark j as used
                if choose(i + 1):
                    return True
                used = used & ~(1 << j) #unused j
                ans[i] = ans[nxt] = 0
            return False
        choose(0)
        return ans

print(Solution().constructDistancedSequence(5))