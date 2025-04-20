from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        #union all == to a group
        #check if any == in different group --> False. Otherwise True
        #Use parent =  26 length array
        parent = [-1] * 26
        def union(i, j):
            parent[i] = j
        def find(i):
            root = i
            while parent[root] != -1:
                root = parent[root]
            #path compression
            while i != root:
                tmp = parent[i]
                parent[i] = root
                i = tmp
            return root
        for first,second,third,forth in equations:
            if second == '=':
                pFirst = find(ord(first) - 97)
                pForth = find(ord(forth) - 97)
                if pFirst != pForth:
                    union(pFirst, pForth)
        for first,second,third,forth in equations:
            if second == '!':
                if parent[ord(first) - 97] != parent[ord(forth) - 97]:
                    return False
        return True
equations = ["b==a","a==b"]
print(Solution().equationsPossible(equations))