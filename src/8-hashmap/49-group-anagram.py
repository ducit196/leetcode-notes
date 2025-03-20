from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strs:
            seen[''.join(sorted(s))].append(s)
        return list(seen.values())
strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))