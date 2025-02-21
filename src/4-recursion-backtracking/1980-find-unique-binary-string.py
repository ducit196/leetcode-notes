from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def binaryToNum(s):
            ans = 0
            j = 0
            for i in range(len(s) - 1, -1, -1):
                ans += int(s[i]) * 2 ** j
                j += 1
            return ans

        def numsToBinary(i, n):
            ans = []
            while i > 0:
                ans.append(str(i % 2))
                i //= 2
            while n - len(ans) > 0:
                ans.append('0')
            ans.reverse()
            return "".join(ans)

        n = len(nums)
        for i in range(n):
            nums[i] = binaryToNum(nums[i])
        for i in range(2 ** n - 1):
            if i not in nums:
                return numsToBinary(i, n)

nums = ["01","10"]
print(Solution().findDifferentBinaryString(nums))