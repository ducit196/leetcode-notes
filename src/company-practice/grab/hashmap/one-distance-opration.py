



class Solution:

    def is_one_edit_distance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False
        diff = 0

        #same length
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] != t[i]:
                    diff += 1
                if diff > 1:
                    return False
        return True
        if len(s) < len(t):
            s, t = t, s
        #s >= t
        j = 0
        diff = 0
        for i in range(len(s)):
            if i == len(t):
                return True
            if s[i] == t[j]:
                j += 1
                continue
            else:
                diff += 1
            if diff > 1:
                return False
        return True
test_cases = [
    ("abc", "ab", True),        # delete 'c'
    ("abc", "adc", True),       # replace 'b' with 'd'
    ("abc", "abcd", True),      # insert 'd'
    ("abc", "abc", False),      # same strings → 0 edits
    ("", "a", True),            # insert 1 char
    ("", "", False),            # both empty → 0 edits
    ("a", "", True),            # delete 1 char
    ("abc", "aXbc", False),     # insert in middle → 2 edits
    ("abcdef", "abqdef", True), # replace in middle
    ("abcdef", "abcdeg", False) # replace + insert → 2 edits
]
for s1, s2, expected in test_cases:
    result = Solution().is_one_edit_distance(s1, s2)
    print(f"is_one_edit_distance('{s1}', '{s2}') = {result} | Expected: {expected} | {'✅' if result == expected else '❌'}")
