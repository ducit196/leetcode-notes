


#
# Note: The class, method and parameter have been specified. Please do not modify
#
#
#
# @param s String
# @param t String
# @return Boolean
#
class Solution:

    def backspaceCompare(self, s, t) :
        def backspace(word):
            ans = []
            for c in word:
                if c != '#':
                    ans.append(c)
                elif c == '#' and len(ans) > 0:
                    ans.pop()

            return ''.join(ans)
        return backspace(s) == backspace(t)
print(Solution().backspaceCompare("a#c","b"))
