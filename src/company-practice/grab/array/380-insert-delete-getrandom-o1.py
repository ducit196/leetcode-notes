from random import choice


class RandomizedSet:
    #Use map for O(1) insert,delete
    #Use a list for O(1) access
    #Once deleted, swap last element with deleted element then pop()
    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.list.append(val)
            self.dict[val] = len(self.list) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.dict:
            idx = self.dict[val]
            self.dict[self.list[-1]] = idx
            self.list[idx], self.list[-1] = self.list[-1], self.list[idx]
            self.list.pop()
            del self.dict[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return choice(self.list)
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()