from typing import List


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
    #Create segment tree is orccurence of each element. from 0 --> max instruction
    #Each instruction, count less than and greater than. Find min cost and update to ans
    # +1 occurence to segment tree
        n = max(instructions) + 1
        tree = [0] * (2 * n)
        def update(x):
            x += n
            tree[x] += 1
            while x > 0:
                left = x
                right = x
                if x % 2 == 0:
                    right = x + 1
                else:
                    left = x - 1
                tree[x // 2] = tree[left] + tree[right]
                x = x // 2


        def rangeSum(l, r):
            sum = 0
            l += n
            r += n
            while l <= r:
                if l % 2 == 1:
                    sum += tree[l]
                    l += 1
                if r % 2 == 0:
                    sum += tree[r]
                    r -= 1
                l = l // 2
                r = r // 2
            return sum
        ans = 0
        for x in instructions:
            #Range sum 0 ->x
            leftSum = rangeSum(0, x - 1)
            #Rang sum x + 1, n - 1
            rightSum = rangeSum(x + 1, n - 1)
            #find min
            ans += min(leftSum, rightSum)
            update(x)
        return ans % 1000000007
instructions = [1,2,3,6,5,4]
print(Solution().createSortedArray(instructions))
