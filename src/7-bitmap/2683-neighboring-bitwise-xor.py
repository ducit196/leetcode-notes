from typing import List


class Solution:
    def doesValidArrayExist(self, nums: List[int]) -> bool:
        n = len(nums)
        #Diver[i] = ori[i] ^ ori[i + 1] -> ori[i + 1] = ori[i] ^ diver[i]
        #Check in case start = 0
        ori = [0]
        for i in range(n):
            ori.append(ori[i] ^ nums[i])
        if ori[0] == ori[-1]:
            return True
        ori = [1]
        for i in range(n):
            ori.append(ori[i] ^ nums[i])
        return ori[0] == ori[-1]