from random import randrange, choice


class RandomizedSet:

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
            self.list[-1], self.list[idx] = self.list[idx], self.list[-1]
            self.list.pop()
            del self.dict[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(0)
param_1 = obj.insert(1)
param_2 = obj.remove(0)
param_2 = obj.insert(2)
param_2 = obj.remove(1)
param_3 = obj.getRandom()