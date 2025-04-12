
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        n = len(s)
        seen = set()
        left = 0
        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            ans = max(ans, right - left + 1)
            seen.add(s[right])
        return ans


s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))
