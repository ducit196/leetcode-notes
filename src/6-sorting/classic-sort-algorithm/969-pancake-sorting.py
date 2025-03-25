from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # Find max fip to the head
        # Flip 1 more time too the last
        def flip(k):
            i = 0
            while i < k / 2:
                arr[i], arr[k - i] = arr[k - i], arr[i]
                i += 1

        n = len(arr)
        ans = []
        for i in range(n - 1, -1, -1):
            # find max pos
            maxVal = 0
            maxPos = 0
            for j in range(i):
                if arr[j] > maxVal:
                    maxVal = arr[j]
                    maxPos = j
            ans.append(maxPos + 1)
            flip(maxPos)
            ans.append(i + 1)
            flip(i)
        return ans
arr = [3,2,4,1]
print(Solution().pancakeSort(arr))
