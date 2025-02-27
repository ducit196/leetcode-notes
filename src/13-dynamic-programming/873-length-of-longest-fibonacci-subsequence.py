from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        #Bruce force O(n2
        # n = len(arr)
        # seen = set(arr)
        # ans = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         prevPrev = arr[i]
        #         prev = arr[j]
        #         current = prev + prevPrev
        #         currentLength = 2
        #         while current in seen:
        #             currentLength += 1
        #             prevPrev = prev
        #             prev = current
        #             current = prev + prevPrev
        #         ans = max(ans, currentLength)
        # return ans if ans > 2 else 0
        n = len(arr)
        dp = [[0] * n for i in range(n)]
        ans = 0
        for cur in range(2, n):
            left = 0
            right = cur - 1
            while left < right:
                if arr[left] + arr[right] > arr[cur]:
                    right -= 1
                elif arr[left] + arr[right] < arr[cur]:
                    left += 1
                else:
                    dp[right][cur] = dp[left][right] + 1
                    ans = max(ans, dp[right][cur])
                    left += 1
                    right -= 1
        return ans + 2 if ans else 0


arr = [1,3,7,11,12,14,18]
print(Solution().lenLongestFibSubseq(arr))
