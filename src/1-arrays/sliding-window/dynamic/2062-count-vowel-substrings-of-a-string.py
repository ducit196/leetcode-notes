from collections import defaultdict


class Solution:
    def countVowelSubstrings(self, s: str) -> int:
        # Exactly 5 = at most 5 - at most 4
        def isVowel(c):
            return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'

        n = len(s)

        #Using shrinkable pattern
        #But shrinkable need find amost condition to check invalid/valid
        #Exactly 5 = atmost 5 - atmost 4
        def countAtmost(goal):
            left = 0
            ans = 0
            seen = defaultdict(int)
            for right in range(n):
                if not isVowel(s[right]):
                    left = right + 1
                    seen = defaultdict(int)
                    continue
                seen[s[right]] += 1
                while left <= right and len(seen) > goal:
                    seen[s[left]] -= 1
                    if seen[s[left]] == 0:
                        del seen[s[left]]
                    left += 1
                ans += right - left + 1
            return ans

        return countAtmost(5) - countAtmost(4)
word = "cuaieuouac"
print(Solution().countVowelSubstrings(word))