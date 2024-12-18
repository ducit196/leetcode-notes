from collections import defaultdict
from typing import List

from Tools.scripts.texi2html import findwordend


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #This is find connect component(same group) pattern
        #Union all pair of vertices satisfy problem
        #Keep track
        #Count number of root(parent[i] = -1)
        #TC: O(n2) - n = number of account
        #SC: O(n)
        n = len(accounts)
        parent = [-1] * n
        emailRoot = [set(accounts[i][1:]) for i in range(n)]

        def find(i: int) ->int:
            root = i
            while parent[root] != -1:
                root = parent[root]
            while i != root:
                u = parent[i]
                parent[i] = root
                i = u
            return root


        def isSameUser(account1: List[str], account2: List[str]):
            accTemp = account2[1:]
            for i in range(1, len(account1)):
                if account1[i] in accTemp:
                    return True
            return False
        for i in range(n):
            for j in  range(i + 1, n):
                if i != j and isSameUser(accounts[i], accounts[j]):
                    ri = find(i)
                    rj = find(j)
                    if ri != rj:
                        parent[ri] = rj
                        emailRoot[rj].update(emailRoot[ri])
        ans = []
        for i in range(n):
            if parent[i] == -1:
                ans .append([accounts[i][0]] + list(sorted(emailRoot[i])))
        return ans
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
ans = Solution().accountsMerge(accounts)
print(ans)