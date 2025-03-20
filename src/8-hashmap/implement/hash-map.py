
class MyHashMap:

    def __init__(self):
        self.size = 0
        self.bucket = [[] for i in range(self.size)]
        self.loadFactor = 0.75
    def getBucketIndex(self, k):
        return k % len(self.bucket)

    def put(self, key: int, value: int) -> None:
        if self.get(key) == -1:
            self.bucket[self.getBucketIndex(key)].append((key, value))
            self.size += 1
        else:
            for i, (k,v) in enumerate(self.bucket[self.getBucketIndex(key)]):
                if k == key:
                    self.bucket[self.getBucketIndex(key)][i] = (key, value)
        if self.size / len(self.bucket) >= 0.75:
            self.rehashing()

    def rehashing(self):
        oldBucket = self.bucket
        self.size = 0
        self.bucket = [[] for i in range(len(oldBucket) * 2)]
        for bucket in oldBucket:
            for k,v in bucket:
                self.put(k, v)
    def get(self, key: int) -> int:
        for k,v in self.bucket[self.getBucketIndex(key)]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        for k,v in self.bucket[self.getBucketIndex(key)]:
            if k == key:
                self.bucket[self.getBucketIndex(key)].remove((k, v))
                self.size -= 1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)