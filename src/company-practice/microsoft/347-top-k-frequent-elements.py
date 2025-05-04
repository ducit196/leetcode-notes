from typing import List, Counter


class Solution:

    #Top k frequent element using bucket sort.
    #Use frequent as index of bucket
    #reverse loop to get element
    #use when number of nums is small
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        bucket = [[] for i in range(n + 1)]
        ans = []
        for word, freq in count.items():
            bucket[freq].append(word)
        for i in range(n, 0, -1):
            if bucket[i]:
                for w in bucket[i]:
                    ans.append(w)
                    if len(ans) == k:
                        return ans
