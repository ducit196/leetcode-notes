from heapq import heapify
from typing import List


class HeapSort:
    #Build a max heap --> top element is max
    #Loop from last to first
        #each i swap with root element --> i is max element.
        #heapify_down root element  in e element --> root is max of i element
    def heapify_down(self, arr: List[int], n: int, i: int):
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
    def heap_sort(self, arr: List[int]):
        n = len(arr)
        #Build a max heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(arr, n, i)
        #Looping from last to first
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify_down(arr, i, 0)

arr = [5,2,3,1]
HeapSort().heap_sort(arr)
print(arr)

