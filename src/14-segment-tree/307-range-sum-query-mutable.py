from typing import List
from unittest.mock import right


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)

        #Build the leaf
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]

        #Build inter node
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index: int, val: int) -> None:
        index += self.n
        self.tree[index] = val
        while index > 0:
            left = index
            right = index
            if index % 2 == 0: #index is left node
                right = index + 1
            else:
                left = index - 1
            self.tree[index // 2] = self.tree[left] + self.tree[right]
            index = index // 2
    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        left += self.n
        right += self.n
        while left <= right:
            if left % 2 == 1:   #left is right child node
                sum += self.tree[left]
                left += 1       #Move to right of parent
            if right % 2 == 0:  #right is in left child
                sum += self.tree[right]
                right -= 1      #Move to left of parent
            left = left // 2
            right = right // 2
        return sum

numArray = NumArray([1, 3, 5])
print(numArray.sumRange(0, 2))
numArray.update(1, 2)