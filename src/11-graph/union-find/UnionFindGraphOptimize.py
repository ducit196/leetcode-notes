class UnionFindGraphOptimize:
    #Optimize union: When union, higher component should be parented --> add a height arrays to maintain
    #Optimize find: parent[3] = 1, parent[1] = 0 --> update parent[3] = 0 once find
    # TC: add - apx O(1), query - apx O(1)
    # SC: O(n)

    def __init__(self, n: int):
        self.n = n
        self.parent = [-1] * n
        self.height = [1] * n
    # find root of i
    def find(self, i: int) -> int:
        root = i
        #find root
        while self.parent[root] != -1:
            root = self.parent[root]

        #from i to root, update parent = root for all
        while i != root:
            u = self.parent[i]
            self.parent[i] = root
            i = u

        return root

    # union
    def union(self, i: int, j: int):
        if self.height[i] > self.height[j]:
            self.parent[j] = i
        elif self.height[i] < self.height[j]:
            self.parent[i] = j
        else:
            self.parent[i] = j
            self.height[j] = self.height[j] + 1
    # add and edge (i, j)
    def add(self, i: int, j: int):
        u = self.find(i)
        v = self.find(j)
        if u != v:
            self.union(u, v)

    def query(self, i: int, j: int) -> bool:
        return self.find(i) == self.find(j)  # i and j have same root --> connected component


obj = UnionFindGraphOptimize(5)
obj.add(0, 1)
obj.add(2, 4)
print(obj.query(0, 4))
obj.add(1, 2)
print(obj.query(0, 4))