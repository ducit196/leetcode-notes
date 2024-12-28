from typing import List


class MinHeap:
    def __init__(self, heap: List[int]):
        self.heap = heap

    def heap_up(self, i: int):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[parent] > self.heap[i]:
                self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
                i = parent
            else:
                break
    def heap_dow(self,i: int):
        n = len(self.heap)
        while True:
            smallest = i
            leftChild = 2 * i + 1
            rightChild = 2 * i + 2
            if leftChild < n and self.heap[leftChild] < self.heap[smallest]:
                smallest = leftChild
            if rightChild < n and self.heap[rightChild] < self.heap[smallest]:
                smallest = rightChild
            if smallest != i:   #parent is not smallest --> swap then dive down
                self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
                i = smallest
            else:
                break


    def heappify(self):
        n = len(self.heap)

        # for i in range(n - 1, n // 2 - 1, -1):
        #     self.heap_up(i)
        #heap down from right most leaf back to root
        for i in range(n // 2 - 1, -1, -1):
            self.heap_dow(i)
    def heap_push(self, val: int):
        self.heap.append(val)
        self.heap_up(len(self.heap) - 1)

    def heap_pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0] #swap root and last element
        self.heap.pop() #pop last element(the min val)
        self.heap_dow(0)

heap = [2,4,1,9,3]
minHeap = MinHeap(heap)
minHeap.heappify()
print(minHeap.heap)
minHeap.heap_push(0)
print(minHeap.heap)
minHeap.heap_pop()
print(minHeap.heap)