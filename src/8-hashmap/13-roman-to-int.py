

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        #previous always greater than
        n = len(s)
        i = 0
        ans = 0
        while i < n:
            if i < n -1 and dic[s[i]] < dic[s[i + 1]]:
                ans += dic[s[i + 1]] - dic[s[i]]
                i += 2
            else:
                ans += dic[s[i]]
                i += 1
        return ans
s = "MCMXCIV"
print(Solution().romanToInt(s))