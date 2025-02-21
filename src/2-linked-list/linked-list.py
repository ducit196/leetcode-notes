from time import sleep


class Node:
    def __init__(self, val = 0, nextNode=None):
        self.val = val
        self.nextNode = nextNode

class MyLinkedList:
    def __init__(self):
        self.head = Node()  #dummy node
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        cur = self.head
        for i in range(index + 1):
            cur = cur.nextNode
        return  cur.val



    def addAtHead(self, val: int) -> None:
        newNode = Node(val, self.head.nextNode)
        self.head.nextNode = newNode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return -1
        prev = self.head
        for i in range(index):
            prev = prev.nextNode
        #add a node between prev and prev.next
        newNode = Node(val, prev.nextNode)
        prev.nextNode = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return -1
        prev = self.head
        for i in range(index):
            prev = prev.nextNode
        prev.nextNode = prev.nextNode.nextNode
        self.size -= 1

obj = MyLinkedList()
print(obj.get(0))
obj.addAtHead(23)
print(obj.get(0))
obj.addAtTail(12)
print(obj.get(1))
obj.addAtIndex(1,2321)
print(obj.get(2))
obj.deleteAtIndex(1)