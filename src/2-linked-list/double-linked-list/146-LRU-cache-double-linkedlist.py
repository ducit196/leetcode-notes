from os import remove


class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        #update node to latest hit cache
        self.remove(node)
        self.addTail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.val = value
            self.addTail(node)
            return
        elif len(self.cache) == self.cap:
            remove(self.head.next)
        node = ListNode(key, value)
        self.addTail(node)
        self.cache[key] = node


        self.addTail(ListNode())
    def addTail(self, node):
        tempPrev = self.tail.prev
        tempPrev.next = node
        node.prev = tempPrev
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)