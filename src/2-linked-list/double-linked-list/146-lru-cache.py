from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.q = deque()
        self.cap = capacity
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.q.remove(key)
        self.q.append(key)
        return self.cache[key]
    def put(self, key: int, value: int) -> None:
        #update key
        if key in self.cache:
            self.cache[key] = value
            self.q.remove(key)
            self.q.append(key)
        #
        elif len(self.cache) == self.cap:
            del self.cache[self.q.popleft()]
            self.cache[key] = value
            self.q.append(key)
        else:
            self.cache[key] = value
            self.q.append(key)

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
