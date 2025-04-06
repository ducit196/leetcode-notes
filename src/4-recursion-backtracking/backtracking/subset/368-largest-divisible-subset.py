from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # This solution quite good but still got TLE
        #Timecomplexity 2 ^ n --> n <= 1000 ---> impossible to use backtring even can optimize
        # --->> ask interviewer constrain to determine we can use backtracking or not
        # This pattern can see the longest increasing subsequence in DP
        nums.sort()
        n = len(nums)
        currentMax = 0
        ans = []
        def choose(start, path):
            nonlocal currentMax
            nonlocal ans
            print(path)
            if len(path) > currentMax:
                currentMax = len(path)
                ans = path.copy()

            for i in range(start, n):
                lastPathElement = path[-1] if len(path) > 0 else 1
                if nums[i] % lastPathElement != 0:
                    continue
                if len(path) + n - i <= currentMax: #prunning if the rest of element + currentPath can not greater than currentMax
                    break
                path.append(nums[i])
                choose(i + 1, path)
                path.pop()
        choose(0, [])
        return ans
nums = [1,2,4,8]
print(Solution().largestDivisibleSubset(nums))