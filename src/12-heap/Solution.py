from typing import List


class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        def heapify_down(arr: List[int], n: int, i: int):
        #max heap
            while True:
                maximum = i
                leftChild = 2 * i + 1
                rightChild = 2 * i + 2
                if leftChild < n and arr[leftChild] > arr[maximum]:
                    maximum = leftChild
                if rightChild < n and arr[rightChild] > arr[maximum]:
                    maximum = rightChild
                if maximum != i:
                    arr[maximum], arr[i] = arr[i], arr[maximum]
                    i = maximum     #deep down
                else:
                    break
        #Build a max heap
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify_down(arr, n, i)
        #Looping from last to first
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            heapify_down(arr, i, 0)
        return arr
arr = [5,2,3,1]
ans = Solution().sortArray(arr)
print(ans)