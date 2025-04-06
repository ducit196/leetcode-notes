from collections import defaultdict
from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        n = len(transactions)
        transList = [trans.split(',') for trans in transactions]
        ans = []
        seen = defaultdict(list)
        for trans in transList:
            seen[trans[0]].append(trans)
        print(seen)
        for name, group in seen.items():
            m = len(group)
            group.sort()
            cityTime = defaultdict(int)
            for i in range(m - 1):
                if int(group[i][1]) - max <= 60 and group[i + 1][3] != group[i][3] or int(group[i][2]) > 1000:
                    ans.append(group[i])

        return ans
transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
print(Solution().invalidTransactions(transactions))