from typing import List


class Solution:

    #Apply union find
    #If 2 string are similar, union
    #Number of root element(element = -1) --> number of group

    #TC: O(n2)
    #SC: O(n)


    def numSimilarGroups(self, strs: List[str]) ->int:
        n = len(strs)
        parent = [-1] * n

        def union(i: int, j):
            parent[i] = j

        def find(i: int) ->int:
            root = i
            while parent[root] != -1:
                root = parent[root]
            while i != root:
                u = parent[i]
                parent[i] = root
                i = u
            return root
        def add(i: int, j: int):
            u = find(i)
            v = find(j)
            if u != v:
                union(u, v)
        for i in range(n):
            for j in range(i + 1, n):
                if i != j and self.isSimilar(strs[i], strs[j]):
                    add(i, j)
        count = 0
        for i in range(n):
            if parent[i] == -1:
                count = count + 1
        return count
    def isSimilar(self, a: str, b: str) ->bool:
        if a == b:
            return True
        diffPos = []
        for i in range(len(a)):
            if a[i] != b[i]:
                diffPos.append(i)
        if len(diffPos) > 2:
            return False
        return a[diffPos[0]] == b[diffPos[1]] and a[diffPos[1]] == b[diffPos[0]]

strs = ["blw","bwl","wlb"]
print(Solution().numSimilarGroups(strs))