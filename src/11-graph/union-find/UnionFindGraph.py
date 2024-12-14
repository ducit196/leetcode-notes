
class UnionFindGraph:
    def __init__(self, n: int):
        self.n = n
        self.parent = [-1] * n
    #TC: Add - O(n), query - O(n)
    #SC: O(n)

    #find root of i
    def find(self, i: int) -> int:
        while self.parent[i] != -1: #need optimize here, parent[3] = 1, parent[1] = 0 --> directly set parent[3] = 0
            i = self.parent[i]
        return i
    #union
    def union(self, i: int, j: int):
        self.parent[j] = i          #need optimize here, higher tree should be parented to reduce complexity --> add height arrays



    #add and edge (i, j)
    def add(self, i: int, j: int):
        u = self.find(i)
        v = self.find(j)
        if u != v:          #union if i and j has different root
            self.union(u, v)

    def query(self, i: int, j: int) ->bool:
        return self.find(i) == self.find(j) #i and j have same root --> connected component
obj = UnionFindGraph(5)
obj.add(0, 1)
obj.add(2, 4)
print(obj.query(0, 4))
obj.add(1, 2)
print(obj.query(0, 4))