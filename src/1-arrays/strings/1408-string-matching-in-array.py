from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        #check if s1 is substring of s2
        def isSubString(s1, s2):
            n = len(s1)
            m = len(s2)
            #Calculate first window hashing(length = n)
            s1Hash = 0
            s2Hash = 0
            for i in range(n):
                s1Hash += pow(2, ord(s1[i]) - 97)
                s2Hash += pow(2, ord(s2[i]) - 97)
            for i in range(m - n):
                if s1Hash == s2Hash and s1 == s2[i: i + n]:
                    return True
                #Rehashing s2
                s2Hash = s2Hash - pow(2, ord(s2[i]) - 97) + pow(2, ord(s2[i + n]) - 97)
            #Compare last window
            if s1Hash == s2Hash and s1 == s2[m - n: m]:
                return True
            return False

        n = len(words)
        ans = []
        words.sort(key=lambda x:len(x))
        for i in range(n - 1):
            for j in range(i + 1, n):
                if isSubString(words[i], words[j]):
                    ans.append(words[i])

        return ans

words = ["mass","as","hero","superhero"]
ans = Solution().stringMatching(words)
print(ans)