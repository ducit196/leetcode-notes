
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        #first window
        numberOfWhite = 0
        for i in range(k):
            numberOfWhite += 1 if blocks[i] == 'W' else 0
        ans = numberOfWhite
        for i in range(k, n):
            numberOfWhite -= 1 if blocks[i - k] == 'W' else 0
            numberOfWhite += 1 if blocks[i] == 'W' else 0
            ans = min(ans, numberOfWhite)
        return ans
blocks = "WWBBBWBBBBBWWBWWWB"
k = 16
print(Solution().minimumRecolors(blocks, k))