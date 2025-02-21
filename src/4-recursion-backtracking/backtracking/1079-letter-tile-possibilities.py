class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        # permutation of each subset
        n = len(tiles)
        # Subset list
        subSet = []
        for status in range(1, 1 << n):
            current = []
            for i in range(n):
                if status >> i & 1 == 1:
                    current.append(tiles[i])
                subSet.append(current)
        print(subSet)
        # permutation of all subset
        ans = set()
        for sub in subSet:
            # if tuple(sub) not in ans:
            for perm in self.permutation(sub):
                ans.add(tuple(perm))
        print(ans)
        return len(ans)

    def permutation(self, nums: List[int]):
        n = len(nums)
        ans = []

        def choose(i, currentSolution):
            if i == n:
                ans.append(currentSolution.copy())
                return
            for j in range(n):
                if nums[j] not in currentSolution:
                    currentSolution.append(nums[j])
                    choose(i + 1, currentSolution)
                    currentSolution.pop()

        choose(0, [])
        return ans   
