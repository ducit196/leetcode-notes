from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        for i in range(1 << n):
            current = []
            for j in range(n):
                if (i >> j) & 1 == 1:
                    current.append(nums[j])
            ans.add(tuple(current))
        return [list(subset) for subset in ans]

print(Solution().subsetsWithDup([2,1,2]))